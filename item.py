#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Item(Sprite):
	"""��������������"""
	def __init__(self,al_setting,screen):
		"""��ָ��λ�ô����ӵ�����"""
		super(Item,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.al_setting = al_setting
		self.rect = pygame.Rect(0,0,al_setting.item_width,
			al_setting.item_height)
		self.rect.x = 0
		self.rect.top = self.screen_rect.top
		self.x = float(self.rect.x)
		self.color = al_setting.item_color
	def update(self):
		"""����λ��"""
		self.x += self.al_setting.item_speed * self.al_setting.direction
		self.rect.x = self.x
	def draw_item(self):
		"""����ͼ��"""
		pygame.draw.rect(self.screen,self.color,self.rect)
