class GameStats():
	# trace and count game information
	def __init__(self,ai_settings):
		# init 
		self.high_score = 0
		self.level = 1
		self.ai_settings = ai_settings
		self.reset_stats()

		self.game_active = False
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		
