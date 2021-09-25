# -*- coding: utf-8 -*-

'''
定义人物角色（能力值）
角色用来存放少量信息辅助生成玩家，目前只用来给玩家传递name。
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame
from random import randint
from itertools import cycle
from threading import Timer
pygame.init()

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

IMAGE_CHANGE_SPEED = 9 # 多少次移动后，改变移动图像

# ! 导入父目录的cfg
sys.path.append(PATH_FA)
import cfg
# from cfg import *

# ! Sprite专有图片加载

# ! Sprite所需函数


hero_list = [k for k in cfg.hero_image.keys()]
def Rand_Hero():
	return hero_list[randint(0, len(hero_list)-1)]

hero_colors = ['red']
def Rand_Color():
	return hero_colors[randint(0, len(hero_colors)-1)]

class Hero(object):
	def __init__(self, name=None, color=None):
		if name==None: name=Rand_Hero()
		if color==None: color = Rand_Color()
		self.name, self.color = name, color




