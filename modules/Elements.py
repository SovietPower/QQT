# -*- coding: utf-8 -*-

'''
定义地图元素实例类，地图元素包括地图本身元素（如地面、河流）与表面元素（如墙、道具）。
分两个Element模块的原因是，Element的子类用到了Item，而Item用到了Element类，会导致循环调用两模块（模块在import时就会整个调用）。
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame, json
from random import randint
from itertools import cycle
from threading import Timer
pygame.init()

from .Basic import *
from .Element import *
from .Item import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

hash_table = {
	1: lambda: Wall_sea1(),
	2: lambda: Stone_sea1()
}
def ID_to_Element(id):
	return hash_table[id]


class Wall_sea1(Destroyable):
	def __init__(self, grid_pos=(0,0), type='wall_sea1') -> None:
		super().__init__()
		self.image = cfg.element_image[type]
		self.grid_pos = grid_pos # 若未定义pos，需进行设置
		self.pos = Grid_to_xy(grid_pos)
		self.item = rand_item(self.grid_pos)

class Stone_sea1(NotDestroyable):
	def __init__(self, grid_pos=(0,0), type='stone_sea1') -> None:
		super().__init__()
		self.image = cfg.element_image[type]
		self.grid_pos = grid_pos # 若未定义pos，需进行设置
		self.pos = Grid_to_xy(grid_pos)






