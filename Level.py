# -*- coding: utf-8 -*-

'运行整个模式'

__author__={
	'name': 'SovietPower'
}

import itertools
import os, sys, pygame, random, threading
from typing import KeysView
from random import randint
from itertools import cycle
from threading import Timer
pygame.init()

import cfg
from modules import *

PATH = os.path.dirname(os.path.abspath(__file__))

# ! 字体加载

# ! 图片加载
background_image = pygame.image.load(os.path.join(PATH, 'pics\\background_water11.png'))

Cursor_image = pygame.image.load(os.path.join(PATH, 'pics\\cursor.png'))
Cursor_hand_image = pygame.image.load(os.path.join(PATH, 'pics\\cursor_hand.png'))
Cursor_hand_push_image = pygame.image.load(os.path.join(PATH, 'pics\\cursor_hand_push.png'))

# ! 音乐加载
background_music_list = []
for x in cfg.Background_music:
	m = pygame.mixer.Sound(x)
	m.set_volume(0.5)
	background_music_list.append(m)

# ! 某些常量
clock = pygame.time.Clock()

# ! 某些变量

def Start(*players):
	game = Level(players) # 此时players为tuple
	game.Begin()

class Level(object):
	screen = None

	def __init__(self, players):
		'''因为要定义screen才能convert，在init时convert好了（不知道可不可）'''
		global background_image, Cursor_image, Cursor_hand_image, Cursor_hand_push_image
		background_image = background_image.convert_alpha()
		Cursor_image = Cursor_image.convert_alpha()
		Cursor_hand_image = Cursor_hand_image.convert_alpha()
		Cursor_hand_push_image = Cursor_hand_push_image.convert_alpha()

		self.map = Map()

		Bomb.Init(self.map) # Bomb的类方法初始化
		Item.map_surface = self.map.surface
		Element.map = self.map

		self.map.update_map_element()

		random.shuffle(background_music_list)
		self.music_cycle = cycle(background_music_list)
		self.music = next(self.music_cycle)

		self.bomb_group = pygame.sprite.Group()
		self.player_group = pygame.sprite.Group()
		'''在此添加人物到map.player中'''
		for p in players:
			self.player_group.add(p)
			self.map.player[p.grid_pos[0]][p.grid_pos[1]].append(p)


		self.result = None

	def Begin(self):
		# Ready go
		cfg.Ready_go_music.play()

		self.Update_screen()
		self.screen.blit(cfg.ready_image, ((cfg.SCREEN_WIDTH-cfg.ready_image.get_width())/2, (cfg.SCREEN_HEIGHT-cfg.ready_image.get_height())/2))
		pygame.display.flip()
		pygame.time.wait(1200)

		self.Update_screen()
		self.screen.blit(cfg.go_image, ((cfg.SCREEN_WIDTH-cfg.go_image.get_width())/2, (cfg.SCREEN_HEIGHT-cfg.go_image.get_height())/2))
		pygame.display.flip()
		pygame.time.wait(800)

		# Start
		self.Play_music()

		# Slow((2, 2))
		# Banana((2, 4))

		while not self.result: # 尚未获得结果
			time = clock.tick(FRAMERATE)
			self.screen.fill((0,0,0))

			self.Run_events()
			self.Update_screen()
			pygame.display.flip() # 别忘了。。

		# End
		self.music.stop()
		# 取消炸弹、爆炸效果计时器
		for e in threading.enumerate():
			if type(e)==threading.Timer:
				e.cancel()

	def Place_bomb(self, player):
		x, y = Get_grid(player.pos)
		if not self.map.bomb[x][y]:
			if player.bomb_rest:
				player.bomb_rest-=1
				bomb = Bomb(player.bomb_type, player, (x, y))
				self.map.bomb[x][y]=bomb
				self.bomb_group.add(bomb)

				cfg.Place_bomb_music.play()

	def Player_move(self, player, keys_pressed, up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT, space=pygame.K_SPACE):
		moving = 0
		if player.canControlMove: # 能控制移动动作（包括被禁锢、速度为0时）
			if(keys_pressed[up]):
				moving = 1
				player.Move_up()
			if(keys_pressed[down]):
				moving = 1
				player.Move_down()
			if(keys_pressed[left]):
				moving = 1
				player.Move_left()
			if(keys_pressed[right]):
				moving = 1
				player.Move_right()
		if not moving:
			player.Set_stop()
		# if(keys_pressed[space]): # 此处为长按可放一直泡
		# 	self.Place_bomb(player)

	def Run_events(self):
		for ev in pygame.event.get():
			if ev.type == pygame.KEYDOWN:
				if ev.key == pygame.K_SPACE: # 在此可判断x的键位（是否等于某玩家的炸弹按键）
					for x in self.player_group:
						self.Place_bomb(x)
				elif ev.key == pygame.K_r:
					self.result = 1
					return
			elif ev.type == pygame.QUIT:
				for e in threading.enumerate():
					if type(e)==threading.Timer:
						e.cancel()
				sys.exit()
			elif ev.type == DEBUG:
				for p in self.player_group:
					# print(p.name, p.slow, p.slow_queue)
					pass

		keys_pressed = pygame.key.get_pressed()
		for x in self.player_group:
			self.Player_move(x, keys_pressed)

	def Update_screen(self):
		self.screen.blit(background_image, (0,0))
		'''炸弹、炸弹特效'''
		self.bomb_group.update(self.screen)
		Bomb.Update_effect(self.screen)

		'''map'''
		self.map.update(self.screen)

		'''player'''
		self.player_group.update(self.screen, self.map)

		'''cursor'''
		cursor_pos =  pygame.mouse.get_pos()
		if(not pygame.mouse.get_pressed()[0]):
			cursor_image = Cursor_hand_image
		else:
			cursor_image = Cursor_hand_push_image
			cfg.Click_music.play()
		self.screen.blit(cursor_image, cursor_pos) # 如果要将图片放在鼠标正中心，还要减去宽度/高度除以2。


	def Play_music(self):
		print('Play!')
		self.music.play()
		# Timer(self.music.get_length()-3, self.End_music).start()
	def End_music(self):
		print('End!')
		self.music.fadeout(3000)
		Timer(3, self.Change_music).start()
	def Change_music(self):
		print('Change!')
		self.music = next(self.music_cycle)
		self.Play_music()





