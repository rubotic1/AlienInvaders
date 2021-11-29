import pygame
from pygame.sprite import Sprite
from stars import Star

class Starfield(Sprite):
	"""Clase que crear el fondo estelar"""

	def __init__(self, ai_game):
		super().__init__()
		"""Calculamos el campo estrellas."""
		self.settings = ai_game.settings
		self.create_stars(ai_game)

	def update(self):
		for star in self.stars:
			star.update()

	def create_stars(self, ai_game):
		self.stars = pygame.sprite.Group()
		self.st_number = self.settings.stars_number

		for star_number in range(self.st_number):
			star = Star(ai_game)
			self.stars.add(star)

	def draw_stars(self):
		"""Dibujamos estrellas en pantalla."""
		for star in self.stars.sprites():
			star.draw_star()