# -*- coding: utf-8 -*-

'''运行单局游戏'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame, random, threading
from random import randint
from itertools import cycle
from threading import Timer
pygame.init()

import cfg
from modules import *

PATH = os.path.dirname(os.path.abspath(__file__))

# ! 字体加载

# ! 图片加载
background_image = pygame.image.load(os.path.join(PATH, 'pics\\background_water.png'))

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

def Start(map, players):
	game = Level(map, players) # 此时players为tuple
	game.Begin()

class Player_Info(pygame.sprite.Sprite):
	'''定义玩家当前的信息。
	如玩家属性、名称。'''
	def __init__(self, x, y, player) -> None:
		pygame.sprite.Sprite.__init__(self)

		self.hero_name = player.hero_name
		self.player_name = player.player_name
		self.player = player
		self.name_text = Text_on_Screen(x, y, 'Name:'+self.player_name, size=20)

		self.bomb_num = [-1, -1, Text_on_Screen(x, y+25, 'Bomb Number:', size=20)]
		self.bomb_power = [-1, -1, Text_on_Screen(x, y+50, 'Bomb Power:', size=20)]
		self.speed = [-1, -1, Text_on_Screen(x, y+75, 'Speed:', size=20)]

		self.Update()

		self.text_group = pygame.sprite.Group(self.name_text, self.bomb_num[2], self.bomb_power[2], self.speed[2])

	def Check_Attr(self, *attr):
		'''检查玩家某些属性是否发生改变，并更新屏幕文字显示。'''
		player = self.player
		for x in attr:
			sx = 'self.'+x
			p0 = eval('player.'+x)
			p1 = eval('player.max_'+x)
			if eval(sx)[0:2]!=[p0, p1]:
				exec(sx+'[0]'+'= p0')
				exec(sx+'[1]'+'= p1')
				player_val = str(p0)+'/'+str(p1)
				exec(sx+'[2].value = player_val')

	def Update(self):
		'''
		更新信息
		可以选择在Player中定义其info，当其有属性改变时再调用该Update，以提高效率。
		但其实应该不用。此外改变属性的地方会比较多（可以在Player中用@property改变属性，但没必要）。
		'''
		self.Check_Attr('bomb_num', 'bomb_power', 'speed')

	def update(self, screen):
		self.Update()
		self.text_group.update(screen)


class Level(object):
	screen = None

	def __init__(self, map, players) -> None:
		'''背景、鼠标图片。因为要定义screen才能convert，在init时convert好了（不知道可不可）'''
		global background_image, Cursor_image, Cursor_hand_image, Cursor_hand_push_image
		background_image = background_image.convert_alpha()
		Cursor_image = Cursor_image.convert_alpha()
		Cursor_hand_image = Cursor_hand_image.convert_alpha()
		Cursor_hand_push_image = Cursor_hand_push_image.convert_alpha()

		self.map = map

		'''BGM'''
		random.shuffle(background_music_list)
		self.music_cycle = cycle(background_music_list)
		self.music = next(self.music_cycle)

		'''Group'''
		self.bomb_group = pygame.sprite.Group()
		self.player_group = pygame.sprite.Group()
		self.player_info_group = pygame.sprite.Group()

		'''在此添加人物到group, map.player, player_info_group中'''
		x, y = 630, 0
		for p in players:
			self.player_group.add(p)
			self.map.player[p.grid_pos[0]][p.grid_pos[1]].append(p)
			'''用于输出的辅助信息'''
			self.player_info_group.add(Player_Info(x, y, p))
			y += 120

		'''Flag of End'''
		self.result = None

	def Begin(self):
		# Ready go
		cfg.Ready_go_music.play()

		self.Update_screen()
		self.screen.blit(cfg.ready_image, ((cfg.SCREEN_WIDTH-cfg.ready_image.get_width())/2, (cfg.SCREEN_HEIGHT-cfg.ready_image.get_height())/2))
		pygame.display.flip()
		pygame.time.wait(1200) # 1200

		self.Update_screen()
		self.screen.blit(cfg.go_image, ((cfg.SCREEN_WIDTH-cfg.go_image.get_width())/2, (cfg.SCREEN_HEIGHT-cfg.go_image.get_height())/2))
		pygame.display.flip()
		pygame.time.wait(800) # 800

		# Start
		self.Play_music()

		# Slow((2, 2))
		# Banana((2, 4))

		while not self.result: # 尚未获得结果
			time = clock.tick(FRAMERATE)
			self.screen.fill((140,140,140))
			# (176,224,230)：淡蓝

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
		x, y = Get_Grid(player.pos)
		if not self.map.bomb[x][y]:
			if player.bomb_rest>0: # ! 注意尽量使用>0而不是!=0判断。
				player.bomb_rest-=1
				bomb = Bomb(player.bomb_type, player, (x, y))
				self.map.bomb[x][y]=bomb
				self.bomb_group.add(bomb)

				cfg.Place_Bomb_Sound.play()

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
				else:
					for x in self.player_group: # 按键操作
						x.Operate(ev.key, self.map.surface)
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
		self.screen.blit(background_image, (cfg.GRID_OFFSET_X-40,cfg.GRID_OFFSET_Y-37))
		'''炸弹、炸弹特效'''
		self.bomb_group.update(self.screen)
		Bomb.Update_effect(self.screen)

		'''map'''
		self.map.update(self.screen) # 输出地图元素，也可顺便输出地图元素信息

		'''player'''
		self.player_group.update(self.screen, self.map) # todo 应在map.update中更新，便于实现正确的层叠效果

		'''cursor'''
		cursor_pos =  pygame.mouse.get_pos()
		if(not pygame.mouse.get_pressed()[0]):
			cursor_image = Cursor_hand_image
		else:
			cursor_image = Cursor_hand_push_image
			cfg.Click_Sound.play()
		self.screen.blit(cursor_image, cursor_pos) # 如果要将图片放在鼠标正中心，还要减去宽度/高度除以2。

		'''辅助信息输出'''
		self.player_info_group.update(self.screen)


	def Play_music(self):
		print('Music Play!')
		self.music.play()
		Timer(self.music.get_length()-3, self.End_music).start() # 下一首BGM
	def End_music(self):
		print('Music End!')
		self.music.fadeout(3000)
		Timer(3, self.Change_music).start()
	def Change_music(self):
		print('Music Change!')
		self.music = next(self.music_cycle)
		self.Play_music()





