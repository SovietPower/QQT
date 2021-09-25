# -*- coding: utf-8 -*-

'''
main
默认类的update函数为更新信息、输出到屏幕函数。
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame, random, threading
from random import randint
from collections.abc import Iterable

import cfg, Level
from modules import *
# from modules import Map # 此行可用Map.x修改Map的全局变量

WIDTH, HEIGHT = cfg.WIDTH, cfg.HEIGHT
SCREEN_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT = cfg.SCREEN_SIZE, cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT

# ! Init
pygame.init()
pygame.display.set_caption("QQT")

PATH = os.path.dirname(os.path.abspath(__file__))

screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
Level.Level.screen = screen

# ! 字体加载


# ! 图片加载
Cursor_image = pygame.image.load(os.path.join(PATH, 'pics\\cursor.png')).convert_alpha()
Cursor_hand_image = pygame.image.load(os.path.join(PATH, 'pics\\cursor_hand.png')).convert_alpha().convert_alpha()
Cursor_hand_push_image = pygame.image.load(os.path.join(PATH, 'pics\\cursor_hand_push.png')).convert_alpha()

# ! 将cfg中预加载的图片进行convert
def Convert_Image_Dict(*dicts):
	for d in dicts:
		for v in d.values():
			if isinstance(v, Iterable):
				for x in v:
					x = x.convert_alpha()
			else: v = v.convert_alpha()
Convert_Image_Dict(cfg.bomb_image, cfg.bomb_shadow_image, cfg.bomb_effect_image)
Convert_Image_Dict(cfg.item_image, cfg.element_image)

# ! 音乐加载


# ! 一些全局的属性
clock = pygame.time.Clock()


def Get_Pos(rect=pygame.Rect(0, 0, 60, 60)):
	'''根据rect大小，返回地图中的随机合法位置'''
	return (random.randint(0, WIDTH-rect.width), random.randint(0, HEIGHT-rect.height))

def Init(map):
	'''声明并初始化全局变量、其它模块的类变量。
	此处为初始化/清空，Level处暂时不做'''
	Bomb.bomb_queue = []
	Bomb.effect_group = pygame.sprite.Group()

	'''初始化其它库的类属性'''
	Bomb.Init(map) # Bomb的类方法初始化
	Item.map_surface = map.surface
	Element.map = map
	Player.map = map

	'''初始化完Element后，才可创建地图元素'''
	map.update_map_element()


def Die(screen, bird):
	pass


def main():
# music
	# pygame.mixer.music.load(cfg.background_music)
	# pygame.mixer.music.set_volume(1)
	# pygame.mixer.music.play(-1)

# Init
	# pygame.time.set_timer(DEBUG, 1500, False)

# Else
	cursor_image = Cursor_image
	pygame.mouse.set_visible(False)

	message = Text_on_Screen(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-20, 'Press 1 to Start.', font='yaheiconsolashybrid', color=(255,255,255), value=-1, fix=Set_Center)
	message2 = Text_on_Screen(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+20, '按1开始游戏', font='yaheiconsolashybrid', color=(255,255,255), value=-1, fix=Set_Center)

	while True:
		time = clock.tick(FRAMERATE)
		screen.fill((0,0,0))

		message.update(screen)
		message2.update(screen)

		for ev in pygame.event.get():
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_1:

					map = Map(map_mode='sea', map_id=11)
					Init(map)
					player_num = map.player_num
					player_pos = map.player_pos

					print('map:', map.map_name)
					print('player_pos:', player_pos)

					players = [] # 玩家表
					player_type = ['hy', 'jelly'] # 选择的英雄类型
					for i in range(0, player_num):
						type_ = player_type[i] if i<len(player_type) else 'hy' # 注意type是关键字
						players.append(Player(hero=Hero(type_), grid_pos=player_pos[i]))

					Level.Start(map, players)
					# Level.Start(Player(Hero('jelly'))) # ! debug用
					continue
			elif ev.type == pygame.QUIT:
				for e in threading.enumerate():
					if type(e)==threading.Timer:
						e.cancel()
				sys.exit()

		# if begin_next_scene:
		# 	begin_next_scene = 0
		# 	scenes_num+=1
		# 	if scenes_num<len(scenes):
		# 		Init()
		# 		scenes[scenes_num].Init()
		# 	else:
		# 		scenes_num = -1
		# keys_pressed = pygame.key.get_pressed()
		# scenes[scenes_num].Run(screen, player, keys_pressed, player2=player2)

		'cursor'
		cursor_pos =  pygame.mouse.get_pos()
		if(not pygame.mouse.get_pressed()[0]):
			cursor_image = Cursor_hand_image
		else:
			cursor_image = Cursor_hand_push_image
		screen.blit(cursor_image, cursor_pos) # 如果要将图片放在鼠标正中心，还要减去宽度/高度除以2。


		pygame.display.flip()











if __name__ == '__main__':
	main()


