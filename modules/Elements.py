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

Element_Table = {
	'sea': {
		'w1': 'Wall_Sea1',
		'w2': 'Wall_Sea2',

		's1': 'Stone_Sea1',
		's2': 'Stone_Sea2',
		's3': 'Stone_Sea3',
		's4': 'Stone_Sea4',
		's5': 'Stone_Sea5',
		's5': 'Stone_Sea5',
		's6': 'Stone_Sea6',
		's7': 'Stone_Sea7',
		's8': 'Stone_Sea8',
		's9': 'Stone_Sea9',
		's10': 'Stone_Sea10',
		's11': 'Stone_Sea11',
		's12': 'Stone_Sea12',

		'd1': 'Door_Sea1'
	}
}
def ID_to_Element(mode, id, grid_pos=(0,0)):
	s = Element_Table[mode][id]+'(grid_pos)'
	return eval(s)

class Wall(Destroyable):
	def __init__(self, grid_pos=(0,0)) -> None:
		super().__init__()
		self.grid_pos = grid_pos # 若未定义pos，需进行设置
		self.pos = Grid_to_XY(grid_pos)
		self.item = Rand_Item(self.grid_pos)

class Stone(NotDestroyable):
	def __init__(self, grid_pos=(0,0)) -> None:
		super().__init__()
		self.grid_pos = grid_pos # 若未定义pos，需进行设置
		self.pos = Grid_to_XY(grid_pos)


class Wall_Sea1(Wall):
	def __init__(self, grid_pos=(0,0), type='wall_sea1') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-5, -12)

class Wall_Sea2(Wall):
	def __init__(self, grid_pos=(0,0), type='wall_sea2') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-6, -12)

class Stone_Sea1(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea1') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-5, -10)

class Stone_Sea2(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea2') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-5, -10)

class Stone_Sea3(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea3') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -11)

class Stone_Sea4(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea4') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-5, -14)

class Stone_Sea5(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea5') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-5, -10)

class Stone_Sea6(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea6') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-5, -10)

class Stone_Sea7(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea7') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -15)

class Stone_Sea8(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea8') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -16)

class Stone_Sea9(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea9') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -20)

class Stone_Sea10(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea10') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -20)

class Stone_Sea11(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea11') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -5)

class Stone_Sea12(Stone):
	def __init__(self, grid_pos=(0,0), type='stone_sea12') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -15)

class Door_Sea1(Stone):
	def __init__(self, grid_pos=(0,0), type='door_sea1') -> None:
		super().__init__(grid_pos)
		self.image = cfg.element_image[type]
		self.image_offset = (-2, -17)






