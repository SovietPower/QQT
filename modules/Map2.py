# -*- coding: utf-8 -*-

'绘制地图'

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame, random
pygame.init()

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)

# ! 导入父目录的cfg
sys.path.append(PATH_FA)
from cfg import *


# ! 字体加载
# print(pygame.font.get_fonts())

# ! 图片加载
ground = pygame.image.load(os.path.join(PATH, 'pics\\base.png'))
welcome = pygame.image.load(os.path.join(PATH, 'pics\\welcome.png'))
game_over = pygame.image.load(os.path.join(PATH, 'pics\\game_over.png'))
# background = pygame.image.load(os.path.join(PATH, 'pics\\background_night.png'))
background = pygame.image.load(os.path.join(PATH, 'pics\\background_pvz2.png'))
bird_dead = pygame.image.load(os.path.join(PATH, 'pics\\dead.png'))

Explode = []
for x in Explode_image: Explode.append(pygame.image.load(x))
Explode_cnt = len(Explode)

# ! 音乐加载

# ! 某些常量
MAP_DX = 200
MAP_WIDTH = background.get_width()-100

# ! 某些变量
'speed为常量'
ground_x, ground_speed = 0, 100
wing_sum, wing_speed = 0, 300

map_x, map_speed = MAP_DX, 200 # 若不乘time，则speed除50或更多
background_pos = [-MAP_DX, 0]




def CreateMap_Intro(screen, bird, time):
	'正式开始前的界面。鸟的动作是确定、不可操作的。'
# 地图
	screen.fill((255, 255, 255))
	screen.blit(background, background_pos) # 430*760
	screen.blit(ground, (ground_x, 600)) # 地面高168
	screen.blit(welcome, (77, 180)) # 276*400 x:430/2-276/2=215-138=77 y:760/2-400/2=180
# 提示
	color = (30, 30, 30)
	tip = my_font.render('操作说明：', True, color)
	tip1 = my_font.render('按E开始，按Up/Left/Right使小鸟飞', True, color)
	tip2 = my_font.render('按R重新游戏 Wabby Wabbo', True, color)
	screen.blit(tip, ((WIDTH-tip.get_width())/2, 590))
	screen.blit(tip1, ((WIDTH-tip1.get_width())/2, 630))
	screen.blit(tip2, ((WIDTH-tip2.get_width())/2, 670))
	# pygame.display.update() # 此时没必要update，否则可能出现无绘制物体的瞬间画面

def CreateMap(screen, bird, time, Total_Time):
	'正式开始后的界面。鸟的动作要根据具体情况设定。'

	screen.fill((255, 255, 255))
	screen.blit(background, background_pos) # 430*760
	screen.blit(ground, (ground_x, 600)) # 地面高168

	now = my_font.render(f'当前得分：{Total_Time/1000:.2f}秒', True, (0, 0, 0))
	screen.blit(now, ((WIDTH-now.get_width())-20, (HEIGHT-now.get_height())-20))

def DieMap(screen, bird, now_score, top_score, Die_Time, Die_Type):
	'该函数不对Die_Time, Die_Type进行修改，两个变量保存在main中，由main修改'
	screen.fill((255, 255, 255))
	screen.blit(background, background_pos) # 430*760
	screen.blit(ground, (ground_x, 600)) # 地面高168
	screen.blit(game_over, (61, 290)) # 308*68  x:(430-308)/2 y:(760-180)/2

	now = my_font.render(f'你的得分为：{now_score:.2f}秒！', True, (0, 0, 0))
	top = my_font.render(f'你的最高分为：{top_score:.2f}秒！', True, (0, 0, 0))
	screen.blit(now, ((WIDTH-now.get_width())/2, 430))
	screen.blit(top, ((WIDTH-top.get_width())/2, 460))

	# global Die_Time, Die_Type
	if Die_Time<1500:
		surf = Explode[Die_Type]
		screen.blit(surf, (bird.x-surf.get_width()/3, bird.y-surf.get_height()/2))




