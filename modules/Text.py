# -*- coding: utf-8 -*-

'''
定义显示的文字。

关于可用的字体：
似乎仅支持输出英文：
'arial'：系统字体。
'calibri', 'corbel', 'georgia', 'segoeui'：比较好看的英文字体，常规书法。
'inkfree'：英文草书。
'impact'：加粗。
'segoeprint'：好看的英文字体。

支持中文：
'yaheiconsolashybrid'
'''

__author__={
	'name': 'SovietPower'
}

import os, sys, pygame
pygame.init()

# from .Basic import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_FA = os.path.dirname(PATH)


# ! 导入父目录的cfg，及部分常用信息
sys.path.append(PATH_FA)
import cfg

# ! Start
# print(pygame.font.get_fonts())

def Set_Center(self):
	w, h = self.surface_text.get_width(), self.surface_text.get_height()
	self.print_pos = (self.x-w/2, self.y-h/2)

def Set_LeftTop(self):
	self.print_pos = (self.x, self.y)

def Set_RightTop(self):
	width = self.surface_text.get_width()
	self.print_pos = (self.x-width, self.y)


class Text_on_Screen(pygame.sprite.Sprite):
	'''显示单行文本内容。
	支持附加数值显示、更改文字、更改数值。'''
	# 需要用Sprite类，便于用Group统一输出。或许可以不用，但Sprite初始只有__g（所在组）一个属性，并不是很大。

	def __init__(self, x, y, text, color=(0,0,0), size=30, font='yaheiconsolashybrid', value=-1, fix=Set_LeftTop) -> None:
		'''
		text：文本内容。
		surface_text：用于输出的文本Surface对象。
		value：用于带数值的Text输出。当value=-1时，不带value输出。注意value也可为字符串，用于高级数字输出。
		fix：设置对齐(x, y)的方式，默认为左上角对齐。在更新文本后也要使用。

		使用_text, _value和修饰器，便于外部修改时更新surface_text。
		'''
		pygame.sprite.Sprite.__init__(self)

		self.x, self.y = x, y
		self.color = color
		self.font = pygame.font.SysFont(font, size)

		self.fix = fix
		self.print_pos = (x, y)

		self._text = text
		self._value = value
		self.Update_Text()

	@property
	def text(self): return self._text
	@text.setter
	def text(self, val):
		self._text = val
		self.Update_Text()

	@property
	def value(self): return self._value
	@value.setter
	def value(self, val):
		self._value = val
		self.Update_Text()

	def Update_Text(self):
		'''更新文本Surface对象。当text, value改变时都需调用（因为绘制次数远大于修改次数）。'''
		s = self._text + (str(self._value) if self._value!=-1 else '')
		self.surface_text = self.font.render(s, True, self.color)

		self.fix(self)

	def update(self, screen):
		screen.blit(self.surface_text, self.print_pos)





