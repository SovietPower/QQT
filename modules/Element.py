# -*- coding: utf-8 -*-

'''
定义地图元素基本类，地图元素包括地图本身元素（如地面、河流）与表面元素（如墙、道具）。
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

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

# ! 图片加载

class Element(object):
	'''地图元素或道具元素。'''
	map = None

	def __init__(self) -> None:
		self.image = None
		self.pos = (0, 0) # 像素位置，用于输出
		self.grid_pos = (0, 0) # 格子位置

		self.size = (1, 1) # 地图元素大小
		self.image_offset = (0, 0) # 图像输出偏移量

		self.canPassPlayer, self.canHidePlay = 0, 0 # 通过/遮蔽玩家
		self.canPassBombEffect, self.canHideBombEffect = 0, 0 # 通过/遮蔽火焰

	def update(self, screen):
		screen.blit(self.image, (self.pos[0]+self.image_offset[0], self.pos[1]+self.image_offset[1]))


class NotDestroyable(Element):
	'''不可摧毁的地图元素。'''
	def __init__(self) -> None:
		super().__init__()

	def Get_Attacked(self, val=1):
		pass

class Destroyable(Element):
	'''可摧毁的地图元素。'''

	def __init__(self) -> None:
		super().__init__()

		self.map_surface = Element.map.surface

		self.hp = 1 # 几次被摧毁
		self.item = None # 隐藏的随机道具，可被设为None
		# 并非所有Destroyable都有隐藏道具，~~比如道具类本身~~（道具设为另一类Destroyable_Item）默认值应为None

	def Get_Attacked(self, val=1):
		self.hp -= val
		if self.hp<=0:
			self.Delete()

	def Delete(self):
		x, y = self.grid_pos[0], self.grid_pos[1]
		if self.item:
			# 将地图该位置元素替换为道具
			self.map_surface[x][y] = self.item
		else:
			self.map_surface[x][y] = None









