# -*- coding: utf-8 -*-

'''
定义地图道具。注意道具也属于Element类。
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


# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y


# hash_table = {
# 	# 1: lambda: Add_Bomb_Number(),
# 	# 2: lambda: Add_Bomb_Power(),
# 	# 3: lambda: Add_Speed(),
# 	# 4: lambda: Random_Item(), # 问号道具
# 	5: (lambda: Slow())(),
# 	6: (lambda: Banana())()
# }
def ID_to_Item(id, grid_pos=(0,0)):
	# return hash_table[id] # 不能预先定义好Hash_table，因为在最初时哈希表内元素就应确定，而此时还没初始化map、element以及item。
	if id==5: return Slow(grid_pos)
	elif id==6: return Banana(grid_pos)

def rand_item(grid_pos=(0,0)):
	return ID_to_Item(randint(5, 5), grid_pos)

class Item(Destroyable):
	def __init__(self) -> None:
		super().__init__()

		self.canPassPlayer = 1
		self.canPassBombEffect = 1



class Slow(Item):
	'''慢慢胶，踩到的人速度变为最慢，持续10s。可被香蕉皮清除效果。
	注意同一个道具不允许多人同时获取，因为player只记录一个玩家！'''
	def __init__(self, grid_pos=(0,0)) -> None:
		super().__init__()

		self.image = cfg.item_image['slow1']
		self.grid_pos = grid_pos # 若未定义pos，需进行设置
		self.pos = Grid_to_xy(grid_pos)
		self.player = None

		self.map_surface[grid_pos[0]][grid_pos[1]] = self

	def Gotten(self, player):
		'''生效'''
		if not player.get_banana: # 香蕉皮的路上可被吃到，但不生效。
			self.timer = Timer(3, self.Expire) # 可能需要在上面
			self.timer.start()
			self.player = player
			player.slow += 1
			player.slow_queue.append(self) # 储存玩家吃到的慢慢胶，用于取消吃到的减速状态（比如香蕉皮）
		'''消失'''
		x, y = self.grid_pos
		self.map_surface[x][y] = None

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
		else: print('??', self.player.name)


class Banana(Item):
	'''香蕉皮。'''
	def __init__(self, grid_pos=(0,0)) -> None:
		super().__init__()

		self.image = cfg.item_image['slow1']
		self.grid_pos = grid_pos
		self.pos = Grid_to_xy(grid_pos)

		self.map_surface[grid_pos[0]][grid_pos[1]] = self

	def Gotten(self, player):
		'''生效'''
		player.Get_Banana()
		'''消失'''
		x, y = self.grid_pos
		self.map_surface[x][y] = None





