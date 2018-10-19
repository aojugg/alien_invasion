# setting
class Settings():
	"""save class of settings in alien invasion """

	def __init__(self):
		"""init game setting """
		# screen setting
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		# ship
		#self.ship_speed_factor = 1.5
		self.ship_limit = 3
		# bullet
		#self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
		# alien
		#self.alien_speed_factor = 10
		self.fleet_drop_speed = 90
		self.speedup_scale = 1.1

		self.score_scale = 1.5
		# fleet_direction_1 : move right 
		# fleet_direction_2 : move left
		#self.fleet_direction = 1

		self.initialize_dynamic_settings()
	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 2.5
		self.bullet_speed_factor = 5
		self.alien_speed_factor = 2
		self.fleet_direction = 1
		self.alien_points = 50
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

		#print(self.alien_points)




