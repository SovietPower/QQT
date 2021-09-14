# -*- coding: utf-8 -*-

'绘制地图'

import os, sys, pygame, random
pygame.init()

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

# ! 导入父目录的cfg
sys.path.append(PATH_FA)
from cfg import *


# ! 字体加载

# ! 图片加载
background = pygame.image.load(os.path.join(PATH, 'pics\\background_pvz2.png'))

# ! 音乐加载

# ! 某些常量

# ! 某些变量


class StartSreen(object):
	def __init__(self):
		pass





