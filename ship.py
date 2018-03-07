#coding:gb2312
import pygame
class Ship():
	"""�����ɴ�"""
	def __init__(self,al_setting,screen):
		"""��ʼ���ɴ�λ��ͼ��"""
		self.screen = screen
		self.al_setting = al_setting
		self.image = pygame.image.load("timg.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.move_right = False
		self.move_left = False
		self.x = float(self.rect.x)
	def update(self):
		"""���·ɴ�λ��"""
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.x += self.al_setting.ship_speed
		elif self.move_left and self.rect.x > 0:
			self.x -= self.al_setting.ship_speed
		self.rect.x = self.x
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	
