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
def random_hero():
	return hero_list[randint(0, len(hero_list)-1)]

class Hero(object):
	def __init__(self, name=None, color=None):
		if name==None: name=random_hero()
		# if color==None: color = random_color()
		self.name, self.color = name, color




