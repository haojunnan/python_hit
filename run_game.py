#coding:gb2312
import pygame
import function as gf
from pygame.sprite import Group
from ship import Ship 
from settings import Settings
from stats import Stats
from scoreboard import Scoreboard
def run_game():
	pygame.init()
	al_setting = Settings()
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	pygame.display.set_caption("hit the item")
	ship = Ship(al_setting,screen)
	stats = Stats(al_setting)
	scoreboard = Scoreboard(al_setting,screen,stats)
	items = Group()
	buttles = Group()
	while True:
		gf.check_event(al_setting,screen,ship,buttles,stats,scoreboard)
		if stats.game_active:
			ship.update()
			gf.update_buttle(al_setting,buttles,items,stats,scoreboard)
			gf.items_update(al_setting,screen,items)
		gf.screen_update(al_setting,screen,ship,items,buttles,scoreboard)
run_game()
