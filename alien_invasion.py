#author : pangbo
#date : 2018/10/18
#import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
#from alien import Alien
def run_game():
	# init game and build screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# build PALY button
	play_button = Button(ai_settings,screen,"PLAY")
	# bulid instance for counting
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	# build a ship
	ship = Ship(ai_settings,screen)
	# build a group of bullet
	bullets = Group()
	# build a alien
	aliens = Group()

	gf.create_fleet(ai_settings,screen,ship,aliens)
	#alien = Alien(ai_settings,screen)

	# set background color 
	bg_color = ai_settings.bg_color

	# start game main loop
	while True:

		# listen keyboard and mouse event
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
			#print(len(bullets))

		#repaint screen for each loop
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		


run_game()