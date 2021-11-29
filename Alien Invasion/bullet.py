import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Clase que maneja los misiles lanzados"""

	def __init__(self, ai_game):
		"""Crea el misil en la posicion actual de la nave."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		self.sound_fx = ai_game.sound_fx

		# Cargamos imagen y definimos el rect
		if (self.stats.bullet_style == 1):
			self.image = pygame.image.load('images/bullet1.png')
		elif (self.stats.bullet_style == 2):
			self.image = pygame.image.load('images/bullet2.png')
		elif (self.stats.bullet_style == 3):
			self.image = pygame.image.load('images/bullet3.png')
		elif (self.stats.bullet_style == 4):
			self.image = pygame.image.load('images/bullet4.png')
		self.rect = self.image.get_rect()
		self.rect.midtop = ai_game.ship.rect.midtop

		# Guardamos la posicion y como float.
		self.y = float(self.rect.y)
		self.sound_fx.play_shot()

	def update(self):
		"""Movemos el misil."""
		# Acutualizamos la posicion vertical y.
		self.y -= self.settings.bullet_speed
		# Actualizamos la posicion del rect.
		self.rect.y = self.y

	def draw_bullet(self):
		"""Dibujamos misil en pantalla."""
		#pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.image, self.rect)

