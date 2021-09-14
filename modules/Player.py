# -*- coding: utf-8 -*-

'''
定义玩家
定义时根据所选角色，保存其图片、数值。
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame
from random import randint
from itertools import cycle
from threading import Timer
pygame.init()

from .Basic import * # 好像直接引用.的所有模块不太好
from .Hero import *
from .Item import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

IMAGE_CHANGE_SPEED = 9 # 多少次移动后，改变移动图像

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

SPEED_basic = cfg.SPEED_basic
SPEED_delta = cfg.SPEED_delta
SPEED_min = cfg.SPEED_min

SPEED_banana = 6

WIDTH, HEIGHT = cfg.WIDTH, cfg.HEIGHT
GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

Way = (1, 0, -1, 0, 1) # 对应右上左下的移动（注意x轴是横向！）

# ! Sprite专有图片加载

# ! Sprite所需函数


class Player(pygame.sprite.Sprite):
	def __init__(self, hero=Hero(), pos=None, bomb_type=random_bomb(), hp=1):
		pygame.sprite.Sprite.__init__(self)
		self.hero = hero
		self.bomb_type = bomb_type

		'''图像'''
		name = hero.name
		self.name = name
		self.move_up_images = set_images(cfg.hero_image[name]['move_up'])
		self.move_down_images = set_images(cfg.hero_image[name]['move_down'])
		self.move_left_images = set_images(cfg.hero_image[name]['move_left'])
		self.move_right_images = set_images_inverted(cfg.hero_image[name]['move_left']) # 向右移动图片，使用左侧镜像。
		self.stop_image = (
			pygame.transform.flip((pygame.image.load(cfg.hero_image[name]['move_left'][0])), True, False).convert_alpha(),
			pygame.image.load(cfg.hero_image[name]['move_up'][0]).convert_alpha(),
			pygame.image.load(cfg.hero_image[name]['move_left'][0]).convert_alpha(),
			pygame.image.load(cfg.hero_image[name]['move_down'][0]).convert_alpha()
		)
		self.image = self.stop_image[0]
		self.rect = self.image.get_rect() # 46*57
		self.size = (self.rect.width, self.rect.height)

		if pos==None: pos = Get_pos(self.rect)
		# self.rect.center = pos # 不用rect判定，rect的坐标只能为int
		# ! 目前定义判定矩形大小为：18*18，如更改图片需更改此范围
		self.x, self.y = pos # (x, y)为人物判定下部正中心，用于确定所在格子
		self.grid_pos = Get_grid(pos)
		self.last_grid_pos = self.grid_pos

		'''数据'''
		data = cfg.hero_data[name]
		self.bomb_num, self.max_bomb_num = data[0], data[1]
		self.bomb_power, self.max_bomb_power = data[2], data[3]
		self.speed, self.max_speed = data[4]*SPEED_delta+SPEED_basic, data[5]*SPEED_delta+SPEED_basic
		self.bomb_rest = self.bomb_num
		self.hp = hp

		'''移动图像'''
		self.orientation = 0 # 0:right 1:up 2:left 3:down
		self.move_cnt = IMAGE_CHANGE_SPEED

		'''道具'''
		self.slow = 0 # 减速层数，当>0时为最低速
		self.slow_queue = [] # 储存玩家吃到的慢慢胶，用于取消吃到的减速状态（比如香蕉皮）

		self.get_banana = 0

		self.canAttack = True


	@property
	def pos(self):
		return (self.x, self.y)
	@pos.setter
	def pos(self, val):
		self.x, self.y = val
	@property
	def print_pos(self):
		# ! 由判定范围决定，如更改判定范围需更改此处
		return (self.x-self.size[0]/2, self.y+9-self.size[1]) # 加的数值为判定y/2

	@property
	def canControlMove(self): # 能控制移动动作（包括被禁锢、速度为0时）
		return not(self.get_banana)

	def update(self, screen, map):
		screen.blit(self.image, self.print_pos)

		'''香蕉皮。要在update处更新不能控制的移动效果，而不是move处'''
		if self.get_banana:
			nx, ny = self.Move_Banana() # 将要移动，而不是立刻移动
			ngx, ngy = Get_grid((nx, ny)) # new_grid_x
			if (ngx, ngy)!=self.grid_pos and not map.Can_Pass_Player(ngx, ngy):
				self.Get_Banana_End()
			else: self.x, self.y = nx, ny
			# print(nx, ny, self.x, self.y)
			# x+Way[self.orientation], y+Way[self.orientation+1]
			# if map.ground[nx][ny] # 遇到障碍时停止

		self.grid_pos = x,y = Get_grid((self.x, self.y))

		if self.last_grid_pos!=self.grid_pos:
			map.player[x][y].append(self)
			map.player[self.last_grid_pos[0]][self.last_grid_pos[1]].remove(self)
			self.last_grid_pos = self.grid_pos

			'''在进入新格子时，触发道具'''
			if isinstance(map.surface[x][y], Item):
				map.surface[x][y].Gotten(self)


	def Get_Attacked(self, val=1):
		self.hp -= val


	'''道具'''
	'''香蕉皮'''
	def Move_Banana(self): # 0:right 1:up 2:left 3:down
		nx, ny = self.x+SPEED_banana*Way[self.orientation], self.y+SPEED_banana*Way[self.orientation+1]
		# if self.orientation==0: nx+=SPEED_banana
		# elif self.orientation==1: ny-=SPEED_banana
		# elif self.orientation==2: nx-=SPEED_banana
		# else: ny+=SPEED_banana
		return (nx, ny)

	def Get_Banana(self):
		self.get_banana = 1

	def Get_Banana_End(self):
		for x in self.slow_queue: # 香蕉皮效果结束时才清除减速状态
			x.Expire_out() # 注意由于多线程，x可能Expire两次，要注意不能重复计算。
		self.slow_queue = []
		self.slow = 0
		self.get_banana = 0

	'''
	移动
	移动效果有三种策略，选择了3以还原原游戏效果：
	1.每次移动若干像素，与上次移动距离到达一定值时改变图片。贴墙时保持静止。
	2.每次移动若干像素，与上次移动时间间距到达一定值时改变图片。贴墙时仍可动作。
	3.每次移动若干像素，并在移动次数到达一定值时改变图片。贴墙时仍可动作。
	静止时播放静止图片。
	'''
	def Get_Speed(self):
		if self.get_banana: return -1
		if not self.slow: return self.speed
		else: return SPEED_min

	def Move_up(self, min=GRID_OFFSET_Y+20):
		'''若speed不为-1，则表示可以移动（有移动动作即可，包括speed=0）'''
		speed = self.Get_Speed()
		if speed==-1: return # 为-1，表示异常状态，无移动动作（如香蕉皮）

		if self.orientation!=1 and not self.get_banana:
			self.orientation = 1
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_up_images)
		self.move_cnt-=1
		if not self.move_cnt:
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_up_images)
		if self.y>min:
			self.y -= speed
		# else:
		# 	self.image = self.stop_image # 为向上移动停止，不加也可
	def Move_down(self, max=GRID_OFFSET_Y+HEIGHT-20):
		speed = self.Get_Speed()
		if speed==-1: return

		if self.orientation!=3:
			self.orientation = 3
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_down_images)
		self.move_cnt-=1
		if not self.move_cnt:
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_down_images)
		if self.y<max:
			self.y += speed
	def Move_left(self, min=GRID_OFFSET_X+20):
		speed = self.Get_Speed()
		if speed==-1: return

		if self.orientation!=2:
			self.orientation = 2
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_left_images)
		self.move_cnt-=1
		if not self.move_cnt:
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_left_images)
		if self.x>min:
			self.x -= speed
	def Move_right(self, max=GRID_OFFSET_Y+WIDTH-20):
		speed = self.Get_Speed()
		if speed==-1: return

		if self.orientation!=0:
			self.orientation = 0
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_right_images)
		self.move_cnt-=1
		if not self.move_cnt:
			self.move_cnt = IMAGE_CHANGE_SPEED
			self.image = next(self.move_right_images)
		if self.x<max:
			self.x += speed
	def Set_stop(self):
		self.image = self.stop_image[self.orientation]


