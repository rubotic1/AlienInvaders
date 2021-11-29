class Settings:
	"""Una clase para guardar configuraciones."""

	def __init__(self):
		"""Inicializamos configuraciones"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0,0,0)

		#Controles de la nave
		self.ship_limit = 3

		#Campo estelar
		self.field_speed = 0.4
		self.field_color = (0,0,0)
		self.stars_number = 200

		# Controles de los misiles
		self.bullets_allowed = 3

		#Alien Settings
		self.fleet_drop_speed = 10
		# direccion de la flota. 1 es derecha y -1 es izquierda.
		self.fleet_direction = 1

		#Por cuanto incrementa velocidad
		self.speedup_scale = 1.5
		self.score_scale = 1.5
		self.initialize_dynamic_settings()


	def screen_size(self):
		a = []
		a.append(self.screen_width)
		a.append(self.screen_height)
		return a

	def initialize_dynamic_settings(self):
		"""Inicializa settings que cambian durante el juego."""
		self.ship_speed = 4
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		# direccion de la flota. 1 es derecha y -1 es izquierda.
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		"""incrementa velocidads"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)

