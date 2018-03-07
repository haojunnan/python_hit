#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Buttle(Sprite):
	def __init__(self,al_setting,screen,ship):
		"""初始化子弹位置图像"""
		super(Buttle,self).__init__()
		self.screen = screen
		self.al_setting = al_setting
		self.rect = pygame.Rect(0,0,self.al_setting.buttle_width,
			self.al_setting.buttle_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		self.color = al_setting.buttle_color
		self.speed = al_setting.buttle_speed
	def update(self):
		"""更新子弹位置"""
		self.y -= self.speed
		self.rect.y = self.y
	def draw_buttle(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
