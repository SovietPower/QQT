# -*- coding: utf-8 -*-

"""
用来添加部分图片、音乐路径。一般只加载路径，不加载图片。
"""

__author__={
	'name': 'SovietPower'
}


import os, pygame, random, json
pygame.init()


FRAMERATE = 60

PATH = os.path.dirname(os.path.abspath(__file__))

GRID_SCALE = 40 # 网格大小
GRID_X = 15 # 网格数
GRID_Y = 13
GRID_OFFSET_X = 40 # 网格起始位置
GRID_OFFSET_Y = 37

WIDTH, HEIGHT = GRID_X*GRID_SCALE, GRID_Y*GRID_SCALE # 实际活动区域。高度与地面的输出位置相同
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # 屏幕大小


# ! 事件定义


# ! 字体加载
# print(pygame.font.get_fonts())
my_font = pygame.font.SysFont('yaheiconsolashybrid',30) # 创建一个Font对象(系统自带)

# ! 音乐
background_music = (
	os.path.join(PATH, 'music\\M07.ogg'),
	os.path.join(PATH, 'music\\M08.ogg'),
	os.path.join(PATH, 'music\\M09.ogg'),
	os.path.join(PATH, 'music\\M10.ogg'),
	os.path.join(PATH, 'music\\M11.ogg'),
	os.path.join(PATH, 'music\\M15.ogg'),
	os.path.join(PATH, 'music\\M17.ogg')
)

Diamond_music = os.path.join(PATH, 'music\\diamond.wav')
Ice_music = os.path.join(PATH, 'music\\ice_frozen.ogg')
Icemelon_music = os.path.join(PATH, 'music\\ice_melonimpact.ogg')

Hit_music = (
	os.path.join(PATH, 'music\\explode_cherrybomb.ogg'),
	os.path.join(PATH, 'music\\explode_explosion.ogg'),
	os.path.join(PATH, 'music\\explode_potato_mine.ogg')
)


# ! 图片
ready_image = pygame.image.load(os.path.join(PATH, 'pics\\ready.png'))
go_image = pygame.image.load(os.path.join(PATH, 'pics\\go.png')) # iCCP

background_image = pygame.image.load(os.path.join(PATH, 'pics\\background_pvz2.png'))

plant_food_image = pygame.image.load(os.path.join(PATH, 'pics\\plant_food.png'))

Diamond_image = os.path.join(PATH, 'pvz_pics\\Diamond.png')
Ice_image = os.path.join(PATH, 'pvz_pics\\Ice_WinterMelon_projectile.png')

Explode_image = (
	os.path.join(PATH, 'pvz_pics\\ExplosionCloud.png'),
	os.path.join(PATH, 'pvz_pics\\ExplosionPow.png'),
	os.path.join(PATH, 'pvz_pics\\ExplosionPowie.png'),
	os.path.join(PATH, 'pvz_pics\\Explosion_PotatoMine_mashed.png'),
	os.path.join(PATH, 'pvz_pics\\ExplosionSpudow.png')
)

# ! 人物图片、信息
SPEED_basic = 3.5 # 所有角色最基础移速
SPEED_delta = 0.25 # 每个道具加的速度

'注意转tuple，且注意这个内容放在数组/dict里就不是注释了，因为这就是一个str'
hero_image = {
	'hy':{
		'move_up': tuple(os.path.join(PATH, 'pic_players\\hy_up'+str(x)+'.png') for x in range(1, 5)),
		'move_down': tuple(os.path.join(PATH, 'pic_players\\hy_down'+str(x)+'.png') for x in range(1, 5)),
		'move_left': tuple(os.path.join(PATH, 'pic_players\\hy_left'+str(x)+'.png') for x in range(1, 5))
	},
	'jelly':{
		'move_up': tuple(os.path.join(PATH, 'pic_players\\jelly_up'+str(x)+'.png') for x in range(1, 5)),
		'move_down': tuple(os.path.join(PATH, 'pic_players\\jelly_down'+str(x)+'.png') for x in range(1, 5)),
		'move_left': tuple(os.path.join(PATH, 'pic_players\\jelly_left'+str(x)+'.png') for x in range(1, 5)),
		# 'move_right': tuple(os.path.join(PATH, 'pic_players\\jelly_right'+str(x)+'.png') for x in range(1, 5))
		# 'stop': os.path.join(PATH, 'pic_players\\jelly_stop.png')
	}
}
def add_hero_image(name):
	hero_image[name] = {

	}

hero_data = {} # 数量 威力 速度（初始为3.5，每次加0.25，上限6？）
try:
	with open(os.path.join(PATH, 'data\\hero.json')) as f:
		hero_data = json.load(f)
except Exception as e:
	print('Hero data error:', e)

# ! 炸弹图片
bomb_image = { # 该图片预加载，因为会频繁生成且都是一样的。
	'grape': tuple(map(lambda x: pygame.image.load(x), (os.path.join(PATH, 'pics\\bomb_grape'+str(x)+'.png') for x in (1, 2, 3, 2))))
}
# flip(Surface, xbool, ybool) -> Surface
bomb_effect_image = { # 该图片预加载，因为会频繁生成且都是一样的。
	'left': tuple(map(lambda x: pygame.image.load(x), (os.path.join(PATH, 'pics\\bomb_effect_left'+str(x)+'.png') for x in range(0, 2)))),
	'right': tuple(map(lambda x: pygame.transform.flip(pygame.image.load(x), True, False), (os.path.join(PATH, 'pics\\bomb_effect_left'+str(x)+'.png') for x in range(0, 2)))),
	'up': tuple(map(lambda x: pygame.image.load(x), (os.path.join(PATH, 'pics\\bomb_effect_up'+str(x)+'.png') for x in range(0, 2)))),
	'down': tuple(map(lambda x: pygame.transform.flip(pygame.image.load(x), False, True), (os.path.join(PATH, 'pics\\bomb_effect_up'+str(x)+'.png') for x in range(0, 2)))),
	'center': (pygame.image.load(os.path.join(PATH, 'pics\\bomb_effect_center.png')), ) # 注意只含一个元素的tuple写法！
}






