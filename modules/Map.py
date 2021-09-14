# -*- coding: utf-8 -*-

'''
定义地图。
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
from .Elements import *
from .Item import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)


# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

# ! 图片加载

def rand_map(mode=randint(1,1), id=randint(1,1)):
	str_m = ''
	if mode==1: str_m = 'sea'
	return str_m+str(id)

class Map(object):
	def __init__(self, map_id=rand_map()):
		'''地图用4个matrix存'''
		# 地图本身就有、不可破坏的，如地板砖、河流
		self.ground = [[None for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# 地图中的表层元素，如石头、可破坏墙、草丛
		self.surface = [[None for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# 某格是否存在玩家
		self.player = [[[] for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# 某格是否存在炸弹
		self.bomb = [[None for j in range(GRID_Y+2)] for i in range(GRID_X+2)]

	def update_map_element(self):
		'''先定义初始化并定义一个map，再更新地图元素，以便确保Element类的map已被初始化好。'''
		# with open(os.path.join(PATH, 'maps\\'+map_id+'.json')) as f:
		# 	ground, elements, player_pos = json.load(f)

		self.surface[3][3] = Slow((3, 3))
		self.surface[3][5] = Banana((3, 5))
		self.surface[3][7] = Wall_sea1((3, 7))
		self.surface[3][8] = Wall_sea1((3, 8))

		self.pos = [[(0,0) for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		for i in range(GRID_X+2):
			self.pos[i][0] = Grid_to_xy((i, 0))
			for j in range(1, GRID_Y+2):
				self.pos[i][j] = (self.pos[i][j-1][0], self.pos[i][j-1][1]+GRID_SCALE)

	def Can_Pass_Player(self, x, y):
		return x>0 and x<=GRID_X and y>0 and y<=GRID_Y
		return (self.ground[x][y]!=None and self.ground[x][y].canPassPlayer) and (self.surface[x][y]==None or self.surface[x][y].canPassPlayer)

	def Print(self, screen, map):
		for i in range(1, GRID_X+1):
			for j in range(1, GRID_Y+1):
				x = map[i][j]
				if x:
					print(i, j, x)
					x.update(screen)

	def update(self, screen):
		self.Print(screen, self.ground)
		self.Print(screen, self.surface)





