# -*- coding: utf-8 -*-

'定义一些基本函数'

__author__={
	'name': 'SovietPower'
}

from functools import cmp_to_key
import os, sys, pygame, random
from random import randint
from threading import Timer
from itertools import cycle

from pygame import image
pygame.init()

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

WIDTH, HEIGHT = cfg.WIDTH, cfg.HEIGHT

GRID_SCALE = cfg.GRID_SCALE
GRID_X, GRID_Y = cfg.GRID_X, cfg.GRID_Y
GRID_OFFSET_X, GRID_OFFSET_Y = cfg.GRID_OFFSET_X, cfg.GRID_OFFSET_Y

# ! 基本函数
def Get_Grid(pos):
	'''根据像素坐标获取所在格子。注意参数为tuple。'''
	return ((int(pos[0])-GRID_OFFSET_X)//GRID_SCALE+1, (int(pos[1])-GRID_OFFSET_Y)//GRID_SCALE+1)

def Grid_to_XY(pos):
	'''返回指定格子的像素坐标。注意参数为tuple。'''
	return (GRID_OFFSET_X+GRID_SCALE*(pos[0]-1), GRID_OFFSET_Y+GRID_SCALE*(pos[1]-1))

'''随机炸弹类型'''
bomb_list = [k for k in cfg.bomb_image.keys()]
def random_bomb():
	return bomb_list[randint(0, len(bomb_list)-1)]

def set_images(images):
	'''定义循环动画'''
	l = (pygame.image.load(i).convert_alpha() for i in images)
	return cycle(l)
def set_images_inverted(images):
	l = []
	for i in images:
		tmp = pygame.image.load(i).convert_alpha()
		l.append(pygame.transform.flip(tmp, True, False))
	return cycle(l)
def set_loaded_images(images):
	'''在main.py处已convert cfg中的预加载图片资源，因此不需要该函数，直接取cycle()即可。'''
	l = (i.convert_alpha() for i in images)
	return cycle(l)

def Dis_Square(p1, p2):
	return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

def Rand_Grid():
	'''返回随机格子'''
	return (randint(1, GRID_X), randint(1, GRID_Y))

def Rand_Pos(rect):
	'''根据rect大小，返回地图中的随机合法位置'''
	return (GRID_OFFSET_X+random.randint(20, WIDTH-rect.width), GRID_OFFSET_Y+random.randint(20, HEIGHT-rect.height))

def Get_Pos_Away(rect, p_obj):
	'''根据rect大小，返回地图中的随机合法位置，但要与点p有一定距离'''
	p = 0
	while True:
		p = (random.randint(GRID_OFFSET_X, WIDTH-rect.width), random.randint(GRID_OFFSET_Y, HEIGHT-rect.height))
		if Dis_Square(p, p_obj)>40000: break
	return p

def Fix_Rect(rect):
	'''保证Rect不越界'''
	rect.left = min(max(0, rect.left), WIDTH-rect.width)
	rect.top = min(max(0, rect.top), HEIGHT-rect.height)

'''旋转对象'''
def Rotate(image, rect, angle):
	"""Rotate the image while keeping its center."""
	# Rotate the original image without modifying it.
	# `rotozoom` usually looks nicer than `rotate`.
	new_image = pygame.transform.rotozoom(image, angle, 1)
	# Get a new rect with the center of the old rect.
	new_rect = new_image.get_rect(center=rect.center)
	Fix_Rect(new_rect)
	return new_image, new_rect

def Sprite_Rotate(self, time):
	self.total_time += time
	if self.total_time>=30:
		self.total_time = 0
		self.rotate_cnt = (self.rotate_cnt+1)%36
		self.print_image, self.rect = Rotate(self.image, self.rect, 10*self.rotate_cnt) # 不要用同一物体旋转多次，而是调角度























