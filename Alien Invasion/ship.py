import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Clase que controla la nave."""

	def __init__(self, ai_game):

		"""Iniciliza la nave y la coloca en posicion inicial."""

		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings


		# Carga la imagen y su rect (rectangulo).
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		

		# Comienza en el centro.
		self.rect.midbottom = self.screen_rect.midbottom

		self.moving_right = False
		self.moving_left = False

		self.x = float(self.rect.x)


	def blitme(self):
		"""Dibuja la nave en su posición"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Actualiza los movimientos de la nave"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#Actulizamos el rect
		self.rect.x = self.x

	def center_ship(self):
		"""Centra la nave en pantalla"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)