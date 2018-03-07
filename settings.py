#coding:gb2312
import pygame
class Settings():
	def __init__(self):
		"""初始化游戏数据"""
		self.screen_width = 780
		self.screen_height = 670
		self.bg_color = (66,67,68)
		self.ship_speed = 0.4
		self.item_color = (99,222,123)
		self.direction = 1
		self.buttle_width = 10
		self.buttle_height = 30
		self.buttle_color = (220,62,62)
		self.item_width = 60
		self.item_height = 8
		self.reset_massages()
	def level_up(self):
		"""游戏升级数据"""
		self.item_speed *= 1.2
		self.buttle_speed *= 1.2
		self.scores *= 1.2
	def reset_massages(self):
		"""游戏中可变数据"""
		self.item_speed = 0.5
		self.buttle_speed = 0.5
		self.scores = 10
		self.ship_limit = 3
