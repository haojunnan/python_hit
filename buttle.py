#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Buttle(Sprite):
	def __init__(self,al_setting,screen,ship):
		"""��ʼ���ӵ�λ��ͼ��"""
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
		"""�����ӵ�λ��"""
		self.y -= self.speed
		self.rect.y = self.y
	def draw_buttle(self):
		"""����Ļ�ϻ����ӵ�"""
		pygame.draw.rect(self.screen,self.color,self.rect)
