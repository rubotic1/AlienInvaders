import pygame
import random
from pygame.sprite import Sprite

class Star(Sprite):
	"""Clase que crea estrellas"""

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.color = self.rand_color()
		self.pos = self.rand_pos()
		self.ai_game = ai_game

		# Crea el rect de la estrella a (0, 0) y luego lo colocamos en posicion.
		tam_star= random.randint(0,2)
		self.rect = pygame.Rect(0, 0,tam_star,tam_star)
		self.rect.center = self.pos
		# Guardamos la posicion y como float.
		self.y = float(self.rect.y)

	def update(self):
		"""Movemos la estrella."""
		
		if self.rect.bottom >= self.screen_rect.bottom:
			self.y = 0
		else:
			self.y += (self.ai_game.settings.field_speed)
		self.rect.y = self.y

	def rand_color(self):
		r = random.randint(0,50) + 205
		g = random.randint(0,50) + 205
		b = random.randint(0,50) + 205
		return (r,g,b)

	def rand_pos(self):
		x = random.randint(0,self.screen_rect.width)
		y = random.randint(0,self.screen_rect.height)

		return [x,y]
	
	def draw_star(self):
		"""Dibujamos estrella en pantalla."""
		self.screen.fill(self.color, self.rect)
