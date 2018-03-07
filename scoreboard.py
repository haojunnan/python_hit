#coding:gb2312
import pygame
import pygame.font
class Scoreboard():
	"""显示得分信息"""
	def __init__(self,al_setting,screen,stats):
		"""初始化得分信息"""
		self.al_setting = al_setting
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats
		self.text_color = (10,10,10)
		self.font = pygame.font.SysFont(None,48)
		self.prep_score()
		self.prep_ships()
		self.prep_level()
	def prep_score(self):
		"""把得分转化成图像显示"""
		rounded_score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,
			self.text_color,self.al_setting.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right
		self.score_rect.top = 10
	def prep_ships(self):
		"""显示飞船剩余数"""
		self.ships_image = self.font.render(str(self.al_setting.ship_limit),
			True,self.text_color,self.al_setting.bg_color)
		self.ships_rect = self.ships_image.get_rect()
		self.ships_rect.x = 0
		self.ships_rect.y = 10
	def prep_level(self):
		"""显示当前击中目标个数"""
		self.level_image = self.font.render(str(self.stats.level),
			True,self.text_color,self.al_setting.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right
		self.level_rect.top = self.score_rect.bottom
	def show_score(self):
		"""显示得分"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.ships_image,self.ships_rect)
		self.screen.blit(self.level_image,self.level_rect)
