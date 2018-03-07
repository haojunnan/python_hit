#coding:gb2312
class Stats():
	"""游戏统计信息"""
	def __init__(self,al_setting):
		"""初始化游戏统计信息"""
		self.al_setting = al_setting
		self.game_active = False
		self.reset_stats()
	def reset_stats(self):
		"""初始化游戏中可能变化信息"""
		self.score = 0
		self.ship_life = self.al_setting.ship_limit
		self.level = 1
