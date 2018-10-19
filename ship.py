import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self,ai_settings,screen):
		"""init ship and set start position"""
		super(Ship,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# load ship image and get shape square
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# place each new ship at the bottom of the middle screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# attribute of ship(center) save small digit
		self.center = float(self.rect.centerx)

		# moving flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""adjust ship position based on moving flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center
	def center_ship(self):
		""" place middle """
		self.center = self.screen_rect.centerx



	def blitme(self):
		"""paint ship at pointed position"""
		self.screen.blit(self.image,self.rect)