# -*- coding: utf-8 -*-

"""
用来添加部分图片、音乐路径。一般只加载路径，不加载图片。
预加载的图片，需在main中convert。
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
DEBUG = pygame.event.custom_type()

# ! 字体加载
# print(pygame.font.get_fonts())
my_font = pygame.font.SysFont('yaheiconsolashybrid',30) # 创建一个Font对象(系统自带)

# ! 音乐
Ready_go_music = pygame.mixer.Sound(os.path.join(PATH, 'music\\ReadyGo.wav'))
Background_music = ( # 在Level初始化时加载
	os.path.join(PATH, 'music\\desert.ogg'),
	os.path.join(PATH, 'music\\field.ogg'),
	os.path.join(PATH, 'music\\match.ogg'),
	os.path.join(PATH, 'music\\snow.ogg'),
	os.path.join(PATH, 'music\\town.ogg'),
	os.path.join(PATH, 'music\\water.ogg')
)

# ! 音效
Blast_music = pygame.mixer.Sound(os.path.join(PATH, 'sound\\blast.wav'))
Click_music = pygame.mixer.Sound(os.path.join(PATH, 'sound\\click.wav'))
Get_item_music = pygame.mixer.Sound(os.path.join(PATH, 'sound\\get_item.wav'))
Option_music = pygame.mixer.Sound(os.path.join(PATH, 'sound\\option.wav'))
Place_bomb_music = pygame.mixer.Sound(os.path.join(PATH, 'sound\\place_bomb.wav'))


# ! 图片
ready_image = pygame.image.load(os.path.join(PATH, 'pics\\ready.png'))
go_image = pygame.image.load(os.path.join(PATH, 'pics\\go.png')) # iCCP

background_image = pygame.image.load(os.path.join(PATH, 'pics\\background_pvz2.png'))

plant_food_image = pygame.image.load(os.path.join(PATH, 'pics\\plant_food.png'))


# ! 人物图片、信息
SPEED_basic = 3.5 # 所有角色最基础移速
SPEED_delta = 0.25 # 每个道具加的速度
SPEED_min = 1 # 可被降低到的最小速度

'注意转tuple，且注意这个内容放在数组/dict里就不是注释了，因为这就是一个str'
hero_image = {}
def Add_hero_image(*names):
	for name in names:
		hero_image[name] = {
			'move_up': tuple(os.path.join(PATH, 'pic_players\\'+name+'_up'+str(x)+'.png') for x in range(1, 5)),
			'move_down': tuple(os.path.join(PATH, 'pic_players\\'+name+'_down'+str(x)+'.png') for x in range(1, 5)),
			'move_left': tuple(os.path.join(PATH, 'pic_players\\'+name+'_left'+str(x)+'.png') for x in range(1, 5))
		}
Add_hero_image('hy', 'jelly')

hero_data = {} # 数量 威力 速度（初始为3.5，每次加0.25，上限6？）
try:
	with open(os.path.join(PATH, 'data\\hero.json')) as f:
		hero_data = json.load(f)
except Exception as e:
	print('Hero data error:', e)

# ! 炸弹图片
bomb_image = {} # 该图片预加载，因为会频繁生成且都是一样的。
def Add_bomb_image(name):
	bomb_image[name] = tuple(map(lambda x: pygame.image.load(x), (os.path.join(PATH, 'pics\\bomb_'+name+str(x)+'.png') for x in (1, 2, 3, 2))))
Add_bomb_image('grape')

# flip(Surface, xbool, ybool) -> Surface
bomb_effect_image = { # 该图片预加载，因为会频繁生成且都是一样的。
	'left': tuple(map(lambda x: pygame.image.load(x), (os.path.join(PATH, 'pics\\bomb_effect_left'+str(x)+'.png') for x in range(0, 2)))),
	'right': tuple(map(lambda x: pygame.transform.flip(pygame.image.load(x), True, False), (os.path.join(PATH, 'pics\\bomb_effect_left'+str(x)+'.png') for x in range(0, 2)))),
	'up': tuple(map(lambda x: pygame.image.load(x), (os.path.join(PATH, 'pics\\bomb_effect_up'+str(x)+'.png') for x in range(0, 2)))),
	'down': tuple(map(lambda x: pygame.transform.flip(pygame.image.load(x), False, True), (os.path.join(PATH, 'pics\\bomb_effect_up'+str(x)+'.png') for x in range(0, 2)))),
	'center': (pygame.image.load(os.path.join(PATH, 'pics\\bomb_effect_center.png')), ) # 注意只含一个元素的tuple写法！
}


# ! 道具图片
def Add_image(images, type, name_prefix, *names):
	type = type+name_prefix
	for name in names:
		images[name_prefix+name] = pygame.image.load(os.path.join(PATH, 'pics\\'+type+name+'.png'))

item_image = {} # 该图片预加载，因为会频繁生成且都是一样的。
Add_image(item_image, 'item_', '', 'slow1')


# ! 地图元素图片
element_image = {} # 该图片预加载
Add_image(element_image, 'element_', 'wall_', 'sea1', 'town1')
Add_image(element_image, 'element_', 'stone_', 'sea1')







