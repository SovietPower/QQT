# -*- coding: utf-8 -*-

'''
定义炸弹及炸弹特效。
炸弹类自身含当前所有恰好爆炸的炸弹，以及爆炸效果出现的位置。

爆炸特效设定：每格最多存4种特效：横向0、纵向0、横向1、纵向1，同向的0可以覆盖同向的1，反之不能，都要输出。如果1要输出则要后于0。此外center覆盖一切，会清空其它特效。
唉但是因为多线程，以及一点点的效率问题，依旧会有bug。
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame
from random import randint
from itertools import cycle
from threading import Timer
pygame.init()

from .Basic import *
from .Element import *
from .Item import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

IMAGE_CHANGE_SPEED = 18 # 18 # 多少次变化后，改变泡泡图像

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y


def towards_to_id(towards, type):
	return (0 if(towards=='left' or towards=='right') else 1)+type*2

class Bomb(pygame.sprite.Sprite):

	map_bomb = None # 最好避免与函数重名

	# 使用set, map而不是group记录爆炸效果，可保证每个格子上最多有两个爆炸效果对象（共两种），且type为0的效果会优先于type为1的效果、后出现的效果优先于早出现的效果。
	# effect_group = pygame.sprite.Group()
	effect_pos = set()
	effect_map = None

	map_ground = None # 当前地图本身，用于停止爆炸延伸、触发特殊效果
	map_surface = None # 当前地图表面，用于摧毁地图元素、停止爆炸延伸
	map_player = None # 当前玩家地图，处于攻击效果处的玩家都会受到伤害

	def __init__(self, type, player, grid_pos, attack_val=1, time=3):
		pygame.sprite.Sprite.__init__(self)

		# self.type = type
		self.images = cycle(cfg.bomb_image[type])
		self.image_sizes = cycle(cfg.bomb_image_size[type])

		shadow_type = cfg.Bomb_to_Shadow_Image(type)
		self.images_shadow = cycle(cfg.bomb_shadow_image[shadow_type])
		self.image_shadow_sizes = cycle(cfg.bomb_shadow_image_size[shadow_type])

		self.Image_Update()

		self.rect = self.image.get_rect()
		# self.move_cnt = IMAGE_CHANGE_SPEED

		self.belong = player # 所属玩家
		self.power = player.bomb_power # 攻击距离
		self.attack_val = attack_val # 伤害（默认1）

		self.x, self.y = Grid_to_XY(grid_pos) # x, y为所在格子右下角像素坐标。
		self.x += GRID_SCALE; self.y += GRID_SCALE
		self.grid_x, self.grid_y = grid_pos
		self.bomb_queue = []

		self.destroyed = False

		self.timer = Timer(time, self.Blast_pre)
		self.timer.start()

	'''类方法。不需要self实例！'''
	def Init(map):
		'''初始化类属性'''
		Bomb.effect_pos = set()
		Bomb.effect_map = [[[None, None, None, None] for j in range(GRID_Y+1)] for i in range(GRID_X+1)]

		Bomb.map_ground = map.ground
		Bomb.map_surface = map.surface
		Bomb.map_player = map.player
		Bomb.map_bomb = map.bomb

	def Update_effect(screen):
		'''由于效果消失是另一线程，可能会出现从pos中移除(x,y)时，恰好已迭代到该位置的情况。
		另一线程会在当前迭代set时修改set，所以应迭代set.copy()，但也要注意特判。'''
		for x, y in Bomb.effect_pos.copy():
			val = 0 # val可改为+=，但要注意伤害特效的覆盖问题，可能要在travel时判断
			ok = 0 # 用于在0的之后输出1，总之是把所有1的输出放在所有0下面
			if Bomb.effect_map[x][y][0]:
				val = Bomb.effect_map[x][y][0].power
				Bomb.effect_map[x][y][0].update(screen)
			elif Bomb.effect_map[x][y][2]:
				ok = 1
			if Bomb.effect_map[x][y][1]:
				val = Bomb.effect_map[x][y][1].power
				Bomb.effect_map[x][y][1].update(screen)
			elif Bomb.effect_map[x][y][3]:
				val = Bomb.effect_map[x][y][3].power
				Bomb.effect_map[x][y][3].update(screen)
			if ok:
				val = Bomb.effect_map[x][y][2].power
				Bomb.effect_map[x][y][2].update(screen)

			'''此处为更新爆炸伤害'''
			# ! 注意此处爆炸伤害只对可穿过元素生效（通过遍历爆炸效果区域）。不可穿过元素在遍历时生效。
			if val:
				for p in Bomb.map_player[x][y]:
					p.Get_Attacked(val)
				if isinstance(Bomb.map_surface[x][y], Destroyable_Item):
					Bomb.map_surface[x][y].Get_Attacked(val)

			# 在此处而不是effect消失时移除位置，更优（应该）。
			# 注意不能用not val来判断，因为多线程，以及上面代码的运行效率很低，会导致其它线程此时加入的effect在此处被删除。只能O(4)判断，这个判断效率还是很高的，所以应该基本不会有线程问题。
			if Bomb.effect_map==[None, None, None, None]:
				Bomb.effect_pos.remove((x, y))

	'''实例方法'''
	def Image_Update(self):
		'''更新该炸弹的图像'''
		self.move_cnt = IMAGE_CHANGE_SPEED
		self.image = next(self.images)
		self.image_size = next(self.image_sizes)
		self.image_shadow = next(self.images_shadow)
		self.image_shadow_size = next(self.image_shadow_sizes)

	def update(self, screen):
		'''输出并更新该炸弹的图像'''
		self.move_cnt -= 1
		if not self.move_cnt:
			self.Image_Update()
		screen.blit(self.image_shadow, (self.x-(GRID_SCALE+self.image_shadow_size[0])/2, self.y-self.image_shadow_size[1]/2))
		screen.blit(self.image, (self.x-(GRID_SCALE+self.image_size[0])/2, self.y-self.image_size[1]))
		# 多张图片的底部是对齐的。

	def Blast_pre(self):
		'''Blast(BFS)前的准备工作，及收尾工作'''
		if self.destroyed: return

		head = 0
		self.bomb_queue = [self]
		while head<len(self.bomb_queue):
			self.bomb_queue[head].Blast(self.bomb_queue)
			head+=1
		cfg.Blast_music.play()
		for b in self.bomb_queue:
			x, y = b.grid_x, b.grid_y
			self.map_bomb[x][y] = None

			for e in self.effect_map[x][y]:
				if e: # 注意不要用x，会覆盖上面x的定义！与C不同。
					e.Delete()
			self.effect_pos.add((x, y)) # 注意Delete完后再add
			self.effect_map[x][y][0] = Bomb_Effect((x, y), 0, 'center')
			# self.effect_map[x][y] = [Bomb_Effect((x, y), 0, 'center'), None, None, None]
			# self.effect_group.add(Bomb_Effect((x.grid_x, x.grid_y), 'center'))

	def Blast(self, queue): # 要传入当前炸弹的queue，才能实现在当前炸弹处连锁
		if self.destroyed: return
		self.destroyed = True

		self.timer.cancel()
		self.kill()
		self.belong.bomb_rest = min(self.belong.bomb_rest+1, self.belong.bomb_num) # 限制恢复糖泡边界，便于添加道具

		self.Travel(queue, 'up', 0, -1)
		self.Travel(queue, 'down', 0, 1)
		self.Travel(queue, 'left', -1, 0)
		self.Travel(queue, 'right', 1, 0)
		# self.Bomb_down(); self.Bomb_left(); self.Bomb_up(); self.Bomb_right()
		# self.bomb_queue.append(self)

	def Travel(self, queue, towards, vx, vy):
		'''遍历爆炸范围。其中self为当前炸弹。'''
		x, y = self.grid_x, self.grid_y
		# x, y = self.grid_x+(self.power+1)*vx, self.grid_y+(self.power+1)*vy # 想改变进入顺序，优化图片断层，但用set遍历这就没有意义了。而且有限制爆炸范围的情况，不能直接倒序。
		for i in range(1, self.power+1):
			x+=vx; y+=vy
			if x<1 or x>GRID_X or y<1 or y>GRID_Y: continue
			if not isinstance(Bomb.map_surface[x][y], Destroyable) and not isinstance(Bomb.map_surface[x][y],NotDestroyable):
				if not self.map_bomb[x][y]:
					type = int(i==self.power)
					id = towards_to_id(towards, type)
					if self.effect_map[x][y][id]: # 更新该处为最新的特效
						self.effect_map[x][y][id].Delete()
					self.effect_pos.add((x, y)) # 注意Delete完后再add
					self.effect_map[x][y][id] = Bomb_Effect((x, y), id, towards, type=type)
				else:
					queue.append(self.map_bomb[x][y])
			else:
				print(x, y, Bomb.map_surface[x][y])
				Bomb.map_surface[x][y].Get_Attacked(self.attack_val)
				break



class Bomb_Effect(pygame.sprite.Sprite):

	def __init__(self, grid_pos, id, towards, type=0, power=1):
		pygame.sprite.Sprite.__init__(self)

		pos = Grid_to_XY(grid_pos)
		self.image = cfg.bomb_effect_image[towards][type]
		self.pos = pos
		self.grid_x, self.grid_y = grid_pos
		self.id = id
		self.power = power # 单次伤害

		self.timer = Timer(0.5, self.Delete)
		self.timer.start()

	# def Begin(self):
	# 	Timer(1, self.Disappear).start()

	def Delete(self):
		self.timer.cancel()
		x, y, id = self.grid_x, self.grid_y, self.id
		Bomb.effect_map[x][y][id] = None
		# 不在此处移除位置pos了
		# if Bomb.effect_map[x][y]==[None, None, None, None]: # 没办法4个元素只能O(4)判断
		# 	assert (x, y) in Bomb.effect_pos, f'{x},{y},{id}'
		# 	Bomb.effect_pos.remove((x, y))

	def update(self, screen):
		screen.blit(self.image, self.pos)

	def Disappear(self):
		self.Delete()




	# def Bomb_up(self):
	# 	for i in range(1, self.power+2):
	# 		x, y = self.grid_x, self.grid_y-i
	# 		if y<1: break # todo
	# 		if not self.map.bomb[x][y]:
	# 			self.effect_group.add(Bomb_Effect((x, y), 'up'))
	# 		else:
	# 			self.bomb_queue.append(self.map.bomb[x][y])
	# def Bomb_down(self):
	# 	for i in range(self.power+1, 0, -1): # 改变进入顺序，优化断层
	# 		x, y = self.grid_x, self.grid_y+i
	# 		if y>GRID_Y: continue # todo
	# 		if not self.map.bomb[x][y]:
	# 			self.effect_group.add(Bomb_Effect((x, y), 'down'))
	# 		else:
	# 			self.bomb_queue.append(self.map.bomb[x][y])
	# def Bomb_left(self):
	# 	for i in range(self.power+1, 0, -1): # 改变进入顺序，优化断层
	# 		x, y = self.grid_x-i, self.grid_y
	# 		if x<1: continue # todo
	# 		if not self.map.bomb[x][y]:
	# 			self.effect_group.add(Bomb_Effect((x, y), 'left'))
	# 		else:
	# 			self.bomb_queue.append(self.map.bomb[x][y])
	# def Bomb_right(self):
	# 	for i in range(1, self.power+2):
	# 		x, y = self.grid_x+i, self.grid_y
	# 		if x>GRID_X: continue # todo
	# 		if not self.map.bomb[x][y]:
	# 			self.effect_group.add(Bomb_Effect((x, y), 'right'))
	# 		else:
	# 			self.bomb_queue.append(self.map.bomb[x][y])

