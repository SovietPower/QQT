# -*- coding: utf-8 -*-

'定义一些基本函数'

__author__={
	'name': 'SovietPower'
}

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

# ! Sprite专有图片加载

# ! 基本函数
'''根据像素坐标获取所在格子'''
def Get_grid(pos):
	return ((int(pos[0])-GRID_OFFSET_X)//GRID_SCALE+1, (int(pos[1])-GRID_OFFSET_Y)//GRID_SCALE+1)

'''返回指定格子的像素坐标'''
def Grid_to_xy(pos):
	return (GRID_OFFSET_X+GRID_SCALE*(pos[0]-1), GRID_OFFSET_Y+GRID_SCALE*(pos[1]-1))

'''随机炸弹类型'''
bomb_list = [k for k in cfg.bomb_image.keys()]
def random_bomb():
	return bomb_list[randint(0, len(bomb_list)-1)]

'''定义循环动画'''
def set_images(images):
	l = (pygame.image.load(i).convert_alpha() for i in images)
	return cycle(l)
def set_images_inverted(images):
	l = []
	for i in images:
		tmp = pygame.image.load(i).convert_alpha()
		l.append(pygame.transform.flip(tmp, True, False))
	return cycle(l)
def set_loaded_images(images):
	l = (i.convert_alpha() for i in images)
	return cycle(l)

def Dis_square(p1, p2):
	return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

def Get_pos(rect):
	'根据rect大小，返回地图中的随机合法位置'
	return (GRID_OFFSET_X+random.randint(20, WIDTH-rect.width), GRID_OFFSET_Y+random.randint(20, HEIGHT-rect.height))

def Get_pos_away(rect, p_obj):
	'根据rect大小，返回地图中的随机合法位置，但要与点p有一定距离'
	p = 0
	while True:
		p = (random.randint(GRID_OFFSET_X, WIDTH-rect.width), random.randint(GRID_OFFSET_Y, HEIGHT-rect.height))
		if Dis_square(p, p_obj)>40000: break
	return p

def Fix_rect(rect):
	'保证Rect不越界'
	rect.left = min(max(0, rect.left), WIDTH-rect.width)
	rect.top = min(max(0, rect.top), HEIGHT-rect.height)

'''旋转对象'''
def rotate(image, rect, angle):
	"""Rotate the image while keeping its center."""
	# Rotate the original image without modifying it.
	# `rotozoom` usually looks nicer than `rotate`.
	new_image = pygame.transform.rotozoom(image, angle, 1)
	# Get a new rect with the center of the old rect.
	new_rect = new_image.get_rect(center=rect.center)
	Fix_rect(new_rect)
	return new_image, new_rect

def Sprite_rotate(self, time):
	self.total_time += time
	if self.total_time>=30:
		self.total_time = 0
		self.rotate_cnt = (self.rotate_cnt+1)%36
		self.print_image, self.rect = rotate(self.image, self.rect, 10*self.rotate_cnt) # 不要用同一物体旋转多次，而是调角度























