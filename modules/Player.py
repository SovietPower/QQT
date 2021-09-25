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

SPEED_banana = 7

WIDTH, HEIGHT = cfg.WIDTH, cfg.HEIGHT
GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

Way = (1, 0, -1, 0, 1) # 对应右上左下的移动（注意x轴是横向！）

# ! Sprite专有图片加载

# ! Sprite所需函数

'''
变量更新说明：
x, y表示像素位置，实时更新。
grid_pos表示格子位置，在update处由x, y更新，几为实时更新。

'''

class Player(pygame.sprite.Sprite):
	map = None

	def __init__(self, hero=Hero(), grid_pos=None, player_name=None, bomb_type=random_bomb(), hp=1):
		# todo 因为函数默认值是不会随机的，所以bomb_type设为rand是不太有用的，炸弹可以设为默认糖泡。
		pygame.sprite.Sprite.__init__(self)
		self.hero = hero
		self.bomb_type = bomb_type
		self.player_name = player_name if player_name!=None else hero.name

		'''图像'''
		name = hero.name
		self.hero_name = name
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

		if grid_pos==None: grid_pos = Get_Grid()
		# self.rect.center = pos # 不用rect判定，rect的坐标只能为int
		# ! 目前定义判定矩形大小为：18*18，如更改图片需更改此范围
		self.x, self.y = Grid_to_XY(grid_pos) # (x, y)为人物判定下部正中心，用于确定所在格子
		self.grid_pos = grid_pos
		self.last_grid_pos = self.grid_pos

		'''数据'''
		data = cfg.hero_data[name]
		self.bomb_num, self.max_bomb_num = data[0], data[1] # ! 注意是num不是number
		self.bomb_power, self.max_bomb_power = data[2], data[3]
		self.speed, self.max_speed = data[4]*SPEED_delta+SPEED_basic, data[5]*SPEED_delta+SPEED_basic
		self.bomb_rest = self.bomb_num # 剩余炸弹数，注意在获得炸弹时更新
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

	'''更新图像、效果'''
	def update(self, screen, map): # 虽然Player本身含map，但还是传递map以保证update的统一性。
		screen.blit(self.image, self.print_pos)

		'''香蕉皮。要在update处更新不能控制的移动效果，而不是move处'''
		if self.get_banana:
			nx, ny = self.Move_Banana() # 将要移动，而不是立刻移动
			if nx!=-1: # 可移动
				self.x, self.y = nx, ny
			else:
				self.Get_Banana_End()

		self.grid_pos = x,y = Get_Grid((self.x, self.y))

		'''更新到达新格子产生影响'''
		if self.last_grid_pos!=self.grid_pos:
			map.player[x][y].append(self)
			map.player[self.last_grid_pos[0]][self.last_grid_pos[1]].remove(self)
			self.last_grid_pos = self.grid_pos

			'''在进入新格子时，触发道具'''
			if isinstance(map.surface[x][y], Item):
				map.surface[x][y].Gotten(self)

	def Get_Attacked(self, val=1):
		self.hp -= val

	Opt_to_Item = {
		pygame.K_1: 'Add_Bomb_Number',
		pygame.K_2: 'Add_Bomb_Power',
		pygame.K_3: 'Add_Speed',
		pygame.K_4: 'Random_Attr',
		pygame.K_5: 'Slow',
		pygame.K_6: 'Banana'
	}
	def Operate(self, key, map_surface):
		'''除移动、放泡外的其它按键操作'''
		if key in Player.Opt_to_Item.keys():
			self.Place(Player.Opt_to_Item[key], map_surface)
		# if key==pygame.K_1: self.Place('Slow', map_surface)

	'''放置道具'''
	def Place(self, obj, map_surface):
		x, y = self.grid_pos
		if not map_surface[x][y]:
			obj += "((x, y))"
			map_surface[x][y] = eval(obj) # eval!
			# if obj=='Slow': map_surface[x][y] = Slow((x, y))


	'''道具效果'''
	'''香蕉皮'''
	def Move_Banana(self): # 0:right 1:up 2:left 3:down
		if not self.Can_Move(self.x, self.y, SPEED_banana*Way[self.orientation], SPEED_banana*Way[self.orientation+1]):
			return (-1, -1)
		nx, ny = self.x+SPEED_banana*Way[self.orientation], self.y+SPEED_banana*Way[self.orientation+1]
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
	移动效果有三种策略，选择了3.以还原原游戏效果：
	1.每次移动若干像素，与上次移动距离到达一定值时改变图片。贴墙时保持静止。
	2.每次移动若干像素，与上次移动时间间距到达一定值时改变图片。贴墙时仍可动作。
	3.每次移动若干像素，并在移动次数到达一定值时改变图片。贴墙时仍可动作。
	静止时播放静止图片。
	'''
	def Get_Speed(self):
		if self.get_banana: return -1
		if not self.slow: return self.speed
		else: return SPEED_min

	def Can_Move(self, x, y, vx, vy):
		x, y = x+vx, y+vy
		sx = 0 if vx==0 else 1 if vx>0 else -1
		sy = 0 if vy==0 else 1 if vy>0 else -1
		gx, gy = Get_Grid((x+15*sx, y+15*sy)) # gx, gy应比位移量更大，以便保证与障碍间有足够距离。注意不应是15*v，否则间距就与速度有关了。
		# print(x, y, Get_Grid((x, y)), gx, gy)
		if (gx, gy)!=self.last_grid_pos and not Player.map.Can_Pass_Player(gx, gy):
			# 如果是目标格子是当前所在格子，且为不可经过（如炸弹），可经过。
			return 0
		return x>GRID_OFFSET_X+20 and x<GRID_OFFSET_X+WIDTH-20 and y>GRID_OFFSET_Y+20 and y<GRID_OFFSET_Y+HEIGHT-5

	def Move_up(self):
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
		if self.Can_Move(self.x, self.y, 0, -speed):
			self.y -= speed
		# else:
		# 	self.image = self.stop_image # 为向上移动停止，不加也可
	def Move_down(self):
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
		if self.Can_Move(self.x, self.y, 0, speed):
			self.y += speed
	def Move_left(self):
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
		if self.Can_Move(self.x, self.y, -speed, 0):
			self.x -= speed
	def Move_right(self):
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
		if self.Can_Move(self.x, self.y, speed, 0):
			self.x += speed
	def Set_stop(self):
		self.image = self.stop_image[self.orientation]


