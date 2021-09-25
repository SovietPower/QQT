# -*- coding: utf-8 -*-

'''
定义地图道具。注意道具属于 Element->Destroyable_Item 类。
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame, json
from random import Random, randint
from itertools import cycle
from threading import Timer
pygame.init()

from .Basic import *
from .Element import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

IMAGE_CHANGE_SPEED = 25 # 多少帧后，浮动道具图像

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

SPEED_delta = cfg.SPEED_delta


Item_Table = {
	1: 'Add_Bomb_Number',
	2: 'Add_Bomb_Power',
	3: 'Add_Speed',
	4: 'Random_Attr', # 问号，增加随机属性
	5: 'Slow',
	6: 'Banana'
}

def ID_to_Item(id, grid_pos=(0,0)):
	# return hash_table[id] # 不能直接用预先定义好的Hash_table。在最初时哈希表内元素就应确定，而此时还没初始化map、element以及item。
	s = Item_Table[id] + '(grid_pos)'
	return eval(s) # eval

def Rand_Item(grid_pos=(0,0)):
	return ID_to_Item(randint(1, 3), grid_pos)

def Init_Pos_Image(self, grid_pos, name):
	self.image = cfg.item_image[name]
	self.grid_pos = grid_pos # 若未定义pos，需进行设置
	self.pos = Grid_to_XY(grid_pos)
	self.map_surface[grid_pos[0]][grid_pos[1]] = self


class Destroyable_Item(Element):
	'''可摧毁的道具元素。'''

	def __init__(self) -> None:
		super().__init__()

		self.map_surface = Element.map.surface

		self.hp = 1 # 几次被摧毁
		# self.item = None # 隐藏的随机道具，可被设为None

	def Get_Attacked(self, val=1):
		self.hp -= val
		if not self.hp:
			self.Delete()

	def Delete(self):
		x, y = self.grid_pos[0], self.grid_pos[1]
		self.map_surface[x][y] = None


class Item(Destroyable_Item):
	def __init__(self) -> None:
		super().__init__()

		self.canPassPlayer = 1
		self.canPassBombEffect = 1

		self.image_changes = cycle((0, 1, 2, 3, 2, 1))
		self.Image_Update()

	def Disappear(self):
		x, y = self.grid_pos
		self.map_surface[x][y] = None

	def Image_Update(self):
		'''更新该道具的图像输出位置效果'''
		self.move_cnt = IMAGE_CHANGE_SPEED
		self.image_change = next(self.image_changes)

	def update(self, screen):
		'''道具独有的绘制函数，用于上下浮动道具图片'''
		self.move_cnt -= 1
		if not self.move_cnt:
			self.Image_Update()
		screen.blit(self.image, (self.pos[0]+self.image_offset[0], self.pos[1]+self.image_offset[1]-self.image_change))

'''
数值修改时，使用delta加min判断。delta用于在数值改变时触发条件（如技能）（if无法处理增加值为负的情况），min用于限制边界（增加值超过1的情况）。
可能有负收益的道具，注意取max。
'''
class Add_Bomb_Number(Item):
	'''增加糖泡数量'''
	def __init__(self, grid_pos=(0,0), inc=1) -> None:
		super().__init__()
		Init_Pos_Image(self, grid_pos, 'AddBombNumber1')

		self.inc = inc # 增加数值

	def Gotten(self, player):
		delta = min(self.inc, player.max_bomb_num-player.bomb_num)
		if delta:
			player.bomb_num += delta
			player.bomb_rest += delta
		self.Disappear()
		cfg.Get_Item_Sound.play()

class Add_Bomb_Power(Item):
	'''增加糖泡威力'''
	def __init__(self, grid_pos=(0,0), inc=1) -> None:
		super().__init__()
		Init_Pos_Image(self, grid_pos, 'AddBombPower1')

		self.inc = inc # 增加数值

	def Gotten(self, player):
		delta = min(self.inc, player.max_bomb_power-player.bomb_power) if self.inc>0 else max(self.inc, 1-player.bomb_power)
		if delta:
			player.bomb_power += delta
		self.Disappear()
		cfg.Get_Item_Sound.play()

class Add_Speed(Item):
	'''增加玩家速度'''
	def __init__(self, grid_pos=(0,0), inc=1) -> None:
		super().__init__()
		Init_Pos_Image(self, grid_pos, 'AddSpeed1')

		self.inc = inc # 增加数值

	def Gotten(self, player):
		delta = min(self.inc, player.max_speed-player.speed) if self.inc>0 else max(self.inc, 2-player.speed)
		if delta:
			player.speed += delta
		self.Disappear()
		cfg.Get_Item_Sound.play()

class Random_Attr(Item):
	'''随机改变玩家某属性'''
	def __init__(self, grid_pos=(0,0), inc=0) -> None:
		super().__init__()
		Init_Pos_Image(self, grid_pos, 'RandomAttr1')

		if not inc: inc = randint(1, 2) # 注意默认参数赋值为random没用，会在定义时被确定
		if randint(1, 5)<=2: inc*=-1 # 2/5
		self.inc = inc # 增加数值

	def Gotten(self, player):
		x = randint(1, 3)
		if x==1:
			delta = min(self.inc, player.max_bomb_num-player.bomb_num) if self.inc>0 else max(self.inc, 1-player.bomb_num)
			# 注意对正负分别讨论。1为最小值。
			if delta:
				player.bomb_num += delta
				player.bomb_rest += delta
		elif x==2:
			delta = min(self.inc, player.max_bomb_power-player.bomb_power) if self.inc>0 else max(self.inc, 1-player.bomb_power)
			if delta:
				player.bomb_power += delta
		elif x==3:
			self.inc *= SPEED_delta
			delta = min(self.inc, player.max_speed-player.speed) if self.inc>0 else max(self.inc, 2-player.speed)
			if delta:
				player.speed += delta

		self.Disappear()
		cfg.Get_Item_Sound.play()


class Slow(Item):
	'''慢慢胶，踩到的人速度变为最慢，持续10s。可被香蕉皮清除效果。
	注意同一个道具不允许多人同时获取，因为player只记录一个玩家！
	# todo 生效与拾起（Gotten）应独立开。拾起会增加道具。
	'''
	def __init__(self, grid_pos=(0,0)) -> None:
		super().__init__()
		Init_Pos_Image(self, grid_pos, 'Slow1')

		self.player = None

	def Gotten(self, player):
		'''生效'''
		if not player.get_banana: # 香蕉皮的路上可被吃到，但不生效。
			self.timer = Timer(3, self.Expire) # 可能需要在上面
			self.timer.start()
			self.player = player
			player.slow += 1
			player.slow_queue.append(self) # 储存玩家吃到的慢慢胶，用于取消吃到的减速状态（比如香蕉皮）

		'''消失'''
		self.Disappear()

	def Expire_out(self):
		'''失效（外部引起）'''
		self.timer.cancel()
		self.Expire()

	def Expire(self):
		'''失效'''
		if self in self.player.slow_queue:
			# 注意由于多线程，x可能Expire两次，要注意不能重复计算。
			self.player.slow_queue.remove(self)
			self.player.slow -= 1
		# else: print('??', self.player.name)


class Banana(Item):
	'''香蕉皮。'''
	def __init__(self, grid_pos=(0,0)) -> None:
		super().__init__()
		Init_Pos_Image(self, grid_pos, 'Banana1')

	def Gotten(self, player):
		'''生效'''
		player.Get_Banana()

		'''消失'''
		self.Disappear()





