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

# from cfg import *
import cfg, Level
from modules import *
# from modules import Map # 用Map.x修改Map的全局变量

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
def Convert_image_dict(*dicts):
	for d in dicts:
		for v in d.values():
			if isinstance(v, Iterable):
				for x in v:
					x = x.convert_alpha()
			else: v = v.convert_alpha()
Convert_image_dict(cfg.bomb_image, cfg.bomb_effect_image, cfg.item_image, cfg.element_image)

# ! 音乐加载


# ! 一些全局的属性
clock = pygame.time.Clock()


def Get_Pos(rect=pygame.Rect(0, 0, 60, 60)):
	'根据rect大小，返回地图中的随机合法位置'
	return (random.randint(0, WIDTH-rect.width), random.randint(0, HEIGHT-rect.height))

def Init():
	'声明并初始化全局变量、其它模块的类变量'
	Bomb.bomb_queue = []
	Bomb.effect_group = pygame.sprite.Group()
	pass

def Die(screen, bird):
	pass


def main():
# music
	# pygame.mixer.music.load(cfg.background_music)
	# pygame.mixer.music.set_volume(1)
	# pygame.mixer.music.play(-1)

# 计时器

# Init
	Init()

	# begin_next_scene = 1
	# scenes = []
	# scenes.append(Level(cfg.background_image))
	# scenes_num = -1

	player = Player(Hero('hy'), Get_Pos())
	player2 = Player(Hero('jelly'), Get_Pos())
	print(player.speed, player2.speed)

	pygame.time.set_timer(DEBUG, 1500, False)

# Else
	cursor_image = Cursor_image
	pygame.mouse.set_visible(False)

	while True:
		time = clock.tick(FRAMERATE)
		screen.fill((0,0,0))

		for ev in pygame.event.get():
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_1:
					Init()
					Level.Start(Player(Hero('hy')), Player(Hero('jelly')))
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


