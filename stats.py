#coding:gb2312
class Stats():
	"""��Ϸͳ����Ϣ"""
	def __init__(self,al_setting):
		"""��ʼ����Ϸͳ����Ϣ"""
		self.al_setting = al_setting
		self.game_active = False
		self.reset_stats()
	def reset_stats(self):
		"""��ʼ����Ϸ�п��ܱ仯��Ϣ"""
		self.score = 0
		self.ship_life = self.al_setting.ship_limit
		self.level = 1
