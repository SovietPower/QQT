# -*- coding: utf-8 -*-

'''
定义炸弹及炸弹特效。
炸弹类自身含当前所有恰好爆炸的炸弹，以及爆炸效果出现的位置。
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

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

IMAGE_CHANGE_SPEED = 15 # 多少次变化后，改变泡泡图像

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

# ! Sprite专有图片加载

# ! Sprite所需函数


class Bomb(pygame.sprite.Sprite):

	map_bomb = None # 最好避免与函数重名

	# 使用set, map而不是group记录爆炸效果，可保证每个格子上最多有两个爆炸效果对象（共两种），且type为0的效果会优先于type为1的效果、后出现的效果优先于早出现的效果。
	# effect_group = pygame.sprite.Group()
	effect_pos = set()
	effect_map = [[([],[]) for j in range(GRID_Y+1)] for i in range(GRID_X+1)]
	map_player = None # 当前玩家地图，处于攻击效果处的玩家都会受到伤害

	def __init__(self, type, player, grid_pos, time=3):
		pygame.sprite.Sprite.__init__(self)
		self.type = type
		self.images = set_loaded_images(cfg.bomb_image[type])
		self.image_sizes = cycle(((x.get_width(), x.get_height()) for x in cfg.bomb_image[type]))

		self.image = next(self.images)
		self.image_size = next(self.image_sizes)
		self.rect = self.image.get_rect()

		self.belong = player # 所属玩家
		self.power = player.bomb_power

		self.x, self.y = Grid_to_xy(grid_pos)
		self.x += GRID_SCALE; self.y += GRID_SCALE
		self.grid_x, self.grid_y = grid_pos
		self.bomb_queue = []

		self.destroyed = False
		self.move_cnt = IMAGE_CHANGE_SPEED

		self.timer = Timer(time, self.Blast_pre)
		self.timer.start()

	'''类方法。不需要self实例！'''
	def Init():
		'''初始化类属性'''
		Bomb.effect_pos = set()
		Bomb.effect_map = [[[None, None] for j in range(GRID_Y+1)] for i in range(GRID_X+1)]

	def Update_effect(screen):
		'''由于效果消失是另一线程，可能会出现从pos中移除(x,y)时，恰好已迭代到该位置的情况。
		另一线程会在当前迭代set时修改set，所以应迭代set.copy()，但也要注意特判。'''
		for x, y in Bomb.effect_pos.copy():
			val = 0
			if Bomb.effect_map[x][y][0]:
				val = Bomb.effect_map[x][y][0].power
				Bomb.effect_map[x][y][0].update(screen)
			elif Bomb.effect_map[x][y][1]:
				val = Bomb.effect_map[x][y][1].power
				Bomb.effect_map[x][y][1].update(screen)
			if val:
				for p in Bomb.map_player[x][y]:
					p.Get_Attacked(val)

	'''实例方法'''
	def update(self, screen):
		'''更新某炸弹的图像'''
		self.move_cnt -= 1
		if not self.move_cnt:
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.images)
			self.image_size = next(self.image_sizes)
		screen.blit(self.image, (self.x-(GRID_SCALE+self.image_size[0])/2, self.y-self.image_size[1]))

	def Blast_pre(self):
		'''Blast(BFS)前的准备工作，及收尾工作'''
		if self.destroyed: return

		head = 0
		self.bomb_queue = [self]
		while head<len(self.bomb_queue):
			self.bomb_queue[head].Blast(self.bomb_queue)
			head+=1
		for b in self.bomb_queue:
			x, y = b.grid_x, b.grid_y
			self.map_bomb[x][y] = None

			if self.effect_map[x][y][0]:
				self.effect_map[x][y][0].Delete()
			self.effect_pos.add((x, y)) # 注意Delete完后再add
			self.effect_map[x][y][0] = Bomb_Effect((x, y), 'center')
			# self.effect_group.add(Bomb_Effect((x.grid_x, x.grid_y), 'center'))

	def Blast(self, queue): # 要传入当前炸弹的queue，才能实现在当前炸弹处连锁
		if self.destroyed: return
		self.destroyed = True

		self.timer.cancel()
		self.kill()
		self.belong.bomb_rest+=1

		self.Travel(queue, 'up', 0, -1)
		self.Travel(queue, 'down', 0, 1)
		self.Travel(queue, 'left', -1, 0)
		self.Travel(queue, 'right', 1, 0)
		# self.Bomb_down(); self.Bomb_left(); self.Bomb_up(); self.Bomb_right()
		# self.bomb_queue.append(self)

	def Travel(self, queue, towards, vx, vy): # 遍历爆炸范围
		x, y = self.grid_x+(self.power+1)*vx, self.grid_y+(self.power+1)*vy
		for i in range(self.power):
			x-=vx; y-=vy # 改变进入顺序，优化图片断层
			if x<1 or x>GRID_X or y<1 or y>GRID_Y: continue
			if not self.map_bomb[x][y]:
				type = int(i==0)
				if self.effect_map[x][y][type]:
					self.effect_map[x][y][type].Delete()
				self.effect_pos.add((x, y)) # 注意Delete完后再add
				self.effect_map[x][y][type] = Bomb_Effect((x, y), towards, type=type)
				# self.effect_group.add(Bomb_Effect((x, y), towards, type=i==0)) # i=0时为最远范围
			else:
				queue.append(self.map_bomb[x][y])



class Bomb_Effect(pygame.sprite.Sprite):

	def __init__(self, grid_pos, towards, type=0, power=1):
		pygame.sprite.Sprite.__init__(self)

		pos = Grid_to_xy(grid_pos)
		self.image = cfg.bomb_effect_image[towards][type]
		self.pos = pos
		self.grid_x, self.grid_y = grid_pos
		self.to = towards
		self.type = type
		self.power = power # 单次伤害

		self.timer = Timer(1, self.Delete)
		self.timer.start()

	def Begin(self):
		Timer(1, self.Disappear).start()

	def Delete(self):
		self.timer.cancel()
		x, y, type = self.grid_x, self.grid_y, self.type
		Bomb.effect_map[x][y][type] = None
		if not Bomb.effect_map[x][y][type^1]:
			assert (x, y) in Bomb.effect_pos, f'{x},{y},{type}'
			Bomb.effect_pos.remove((x, y))

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

