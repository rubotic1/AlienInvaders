import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Clase quye representa un alien indivudual"""

	def __init__(self, ai_game):
		"""Inicializa el alien y coloca en posicion"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Cargamos imagen y definimos el rect
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Posicion horizontal del alien
		self.x = float(self.rect.x)

	def update(self):
		"""Movemos el alien a la derecha."""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""Devuelve TRUE si toca el borde de pantalla"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True