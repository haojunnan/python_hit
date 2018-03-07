#coding:gb2312
import pygame
import sys
from item import Item
from buttle import Buttle
def k_down(event,al_setting,screen,ship,buttles,stats,scoreboard):
	"""��ⰴ�¼�λ����Ӧ��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
	elif event.key == pygame.K_SPACE:
		if len(buttles) == 0:
			buttle = Buttle(al_setting,screen,ship)
			buttles.add(buttle)
	elif event.key == pygame.K_p:
		stats.game_active = True
		stats.reset_stats()
		al_setting.reset_massages()
		scoreboard.prep_score()
		scoreboard.prep_ships()
		scoreboard.prep_level()
def k_up(event,ship):
	"""����ɿ���λ����Ӧ��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	elif event.key == pygame.K_LEFT:
		ship.move_left = False
def check_event(al_setting,screen,ship,buttles,stats,scoreboard):
	"""�����������Ӧ�¼�"""
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			k_down(event,al_setting,screen,ship,buttles,stats,scoreboard)
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		elif event.type == pygame.KEYUP:
			k_up(event,ship)
		elif event.type == pygame.QUIT:
			sys.exit()
def update_buttle(al_setting,buttles,items,stats,scoreboard):
	"""�����ӵ�λ�ã�����ӵ���ײ��Ļ��Ե"""
	if al_setting.ship_limit > 0:
		buttles.update()
		for buttle in buttles.copy():
			if buttle.rect.bottom <= 0:
				buttles.remove(buttle)
				al_setting.ship_limit -= 1
				scoreboard.prep_ships()
			check_buttle_item_collisions(al_setting,buttles,items,stats,
				scoreboard)
	else:
		stats.game_active = False
def check_buttle_item_collisions(al_setting,buttles,items,stats,scoreboard):
	"""�ӵ���ײ�¼����Ƴ��ӵ�������"""
	collisions = pygame.sprite.groupcollide(buttles,items,True,True)
	if collisions:
		al_setting.level_up()
		stats.level += 1
		stats.score += al_setting.scores
		scoreboard.prep_score()
		scoreboard.prep_level()
def check_edge(al_setting,screen,items):
	"""��������Ƿ�������Ե����������"""
	screen_rect = screen.get_rect()
	for item in items:
		check_right = item.rect.right >= screen_rect.right
		check_left = item.rect.left < screen_rect.left
		if check_right or check_left:
			al_setting.direction *= -1
def items_update(al_setting,screen,items):
	"""��������"""
	check_edge(al_setting,screen,items)
	items.update()
	if len(items) == 0:
		item = Item(al_setting,screen)
		items.add(item)
def screen_update(al_setting,screen,ship,items,buttles,scoreboard):
	"""������Ļ����"""
	screen.fill(al_setting.bg_color)
	for buttle in buttles.sprites():
		buttle.draw_buttle()
	ship.blitme()
	for item in items.sprites():
		item.draw_item()
	scoreboard.show_score()
	pygame.display.flip()
	
