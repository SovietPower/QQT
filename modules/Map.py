# -*- coding: utf-8 -*-

'''
定义地图。

# ! 注意 y为高度（行），x为宽度（列）。因为blit时 x为宽度，y为高度。所以制作地图时，是每列每列制作，不是按行。
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

WIDTH, HEIGHT = cfg.WIDTH, cfg.HEIGHT
GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

# !
ID_to_Mode = {
	1: 'sea'
}
Map_Pool = { # 每种地图类型拥有的地图
	'sea': [11]
}

def Rand_Mode():
	return ID_to_Mode[randint(1, 1)]

def Rand_Map(mode):
	return random.choice(Map_Pool['sea']) # random.choice()返回一个列表/元组/字符串的随机项

class Map(object):
	def __init__(self, map_mode=None, map_id=None):
		if map_mode==None: map_mode = Rand_Mode()
		if map_id==None: map_id = Rand_Map(map_mode)
		self.map_mode, self.map_id = map_mode, map_id
		self.map_name = map_mode+str(map_id)

		'''地图用4个matrix存'''
		# 地图本身就有、不可破坏的，如特殊地板砖、河流
		self.ground = [[None for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# 地图中的表层元素，如石头、可破坏墙、草丛
		self.surface = [[None for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# 某格是否存在玩家
		self.player = [[[] for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# 某格是否存在炸弹
		self.bomb = [[None for j in range(GRID_Y+2)] for i in range(GRID_X+2)]

	def update_map_element(self):
		'''先定义一个map并初始化，再更新地图元素，以便确保Element类的map已被初始化好。'''

		try:
			with open(os.path.join(PATH_FA, 'map\\'+self.map_name+'.json'), 'r', encoding='UTF-8') as f:
				tmp = json.load(f)
				ground, surface, player_pos = tmp[0], tmp[1], tmp[2]
		except:
			print("Map File Open Error!")

		self.player_num = 0
		self.player_pos = []
		for i in range(1, GRID_X+1): # 此为逐列操作
			for j in range(1, GRID_Y+1):
				# g = ground[i][j] # todo 目前暂未定义ground类型
				# if g: self.ground[i][j] = g

				e = surface[i][j]
				if e: self.surface[i][j] = ID_to_Element(self.map_mode, e, (i, j))

		for p in player_pos:
			self.player_num += 1
			self.player_pos.append(p)

		self.surface[3][3] = Slow((3, 3))
		self.surface[3][5] = Banana((3, 5))
		# self.surface[5][5] = Wall_sea1((5, 5))
		# self.surface[3][7] = Wall_sea1((3, 7))
		# self.surface[3][9] = Wall_sea1((3, 9))
		# self.surface[3][10] = Wall_sea1((3, 10))

		'''将格子(i, j)映射到其左上角坐标'''
		# self.pos = [[(0,0) for j in range(GRID_Y+2)] for i in range(GRID_X+2)]
		# for i in range(GRID_X+2):
		# 	self.pos[i][0] = Grid_to_xy((i, 0))
		# 	for j in range(1, GRID_Y+2):
		# 		self.pos[i][j] = (self.pos[i][j-1][0], self.pos[i][j-1][1]+GRID_SCALE)

	def Can_Pass_Player(self, x, y):
		'''参数为两个整数gx, gy'''
		if self.ground[x][y] and not self.ground[x][y].canPassPlayer:
			return 0
		if self.surface[x][y] and not self.surface[x][y].canPassPlayer:
			return 0
		if self.bomb[x][y]:
			return 0
		return x>0 and x<=GRID_X and y>0 and y<=GRID_Y
		# return (self.ground[x][y]!=None and self.ground[x][y].canPassPlayer) and (self.surface[x][y]==None or self.surface[x][y].canPassPlayer)

	def Print(self, screen, map, flag=0):
		# 注意i/x是列，j/y是行！
		for i in range(GRID_X, 0, -1): # 从右到左，以覆盖元素向左的阴影
			for j in range(1, GRID_Y+1): # 从上到下，以覆盖元素下部
				x = map[i][j]
				if x:
					x.update(screen)
				# if flag: # todo 人物在元素右边时会被遮蔽，人物的输出要保证严格从上到下
				# 	for p in self.player[i][j]:
				# 		p.update(screen, self)

	def update(self, screen):
		self.Print(screen, self.ground)
		self.Print(screen, self.surface, 1)





