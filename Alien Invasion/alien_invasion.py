import sys
import pygame


from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from starfield import Starfield
from sound_fx import Sound_fx

class AlienInvasion:
	"""Clase general que controla en juego y sus objetos"""

	def __init__(self):
		""" Inicializamos el juego y creamos los recursos"""

		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(self.settings.screen_size())
		#para FULLSCREEN
		#self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
		pygame.display.set_caption("Alien Invasion")

		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.sound_fx = Sound_fx()

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.starfield = Starfield(self)

		# Color de fondo
		self.bg_color = self.settings.bg_color

		# Boton "Play"
		self.play_button = Button(self, "Play")

		#Inicializamos musica
		self.sound_fx.play_init_music()

		self._create_fleet()



	def run_game(self):
		"""Comienza el bucle loop principal"""
		while True:
			
			self._check_events()
			if self.stats.game_active:
				self.starfield.update()
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			self._update_screen()	


	def _check_events(self):
		# Espera eventos del teclado y del mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)	
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()	
				self._check_play_button(mouse_pos)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		#elif event.key == pygame.K_q:
		#	sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _check_play_button(self, mouse_pos): 
		"""Comprueba si hay colision mouse vs button"""
		if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
			# Reseteamos stats
			self.stats.reset_stats()
			# Eliminamos balas y aliens
			self.aliens.empty()
			self.bullets.empty()

			# Creamos flota nueva y centramos nave
			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()

			self.settings.initialize_dynamic_settings()
			# Ponemos la música de batalla
			self.sound_fx.play_game_music()


	def _update_screen(self):
		# Redibuja la pantalla
		self.screen.fill(self.bg_color)
		self.starfield.draw_stars()
		self.ship.blitme()
		# Dibujamos los misiles en el grupo
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)
		self.sb.show_score()

		if not self.stats.game_active:
			self.play_button.draw_button()

		pygame.display.flip()

	def _fire_bullet(self):
		"""Crea bala y la añade al grupo"""
		if len(self.bullets) < self.settings.bullets_allowed:
			self.stats.check_bullet_change()
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			self.stats.bullet_counter+=1

	def _update_bullets(self):
		"""Actualiza posicion y quita a los desaparecidos"""
		# Actualiza posicion.
		self.bullets.update()

		# Sacar del grupo los misiles desaparecidos
		# por el borde superior
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self.check_bullet_alien_collisions()	

	def check_bullet_alien_collisions(self):
		"""Quita las balas y aliens que colisionen"""

		# Comprobamos si las balas tocan el alien
		# Si tocan, destruimos ambos.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if collisions:
			self.stats.score += self.settings.alien_points
			self.sb.prep_score()
			self.sb.check_high_score()
			self.sound_fx.play_alien()

		if not self.aliens:
			# Destruye las balas y crea flota nueva.
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

			# Incrementa nivle.
			self.stats.level += 1
			self.sb.prep_level()

	def _create_fleet(self):
		# creamos la flota alien y calculamos cuantos
		# aliens caben en una fila
		alien = Alien(self)

		alien_width, alien_height = alien.rect.size

		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Numero filas
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
			(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Creamos filas.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		"""Crea un alien y lo pone en su columna"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien_height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _update_aliens(self):
		self._check_fleet_edges()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self.aliens.update()
		self._check_aliens_bottom()

	def _check_fleet_edges(self):
		"""Responde si tocamos borde"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Baja velocidad y cambia dirección"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _ship_hit(self):
		"""Responde cuando golpeamos a un alien"""

		if self.stats.ships_left > 0:

			# Una vida menos
			self.stats.ships_left -= 1
			self.sb.prep_ships()

			# Eliminamos balas y aliens
			self.aliens.empty()
			self.bullets.empty()

			# Creamos flota nueva y centramos nave
			self._create_fleet()
			self.ship.center_ship()

			#Reseteamos velocidad y balas
			self.stats.reset_bullets()
			self.settings.initialize_dynamic_settings()

			# Pause.
			sleep(0.5)
		else:
			pygame.mouse.set_visible(True)
			self.sound_fx.play_init_music()
			self.stats.game_active = False



	def _check_aliens_bottom(self):
		"""Comprueba si el alien ha tocado el suelo"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
			# Hacemos lo mismo que si choca con la nave
				self._ship_hit()
				break


if __name__== '__main__':
	#Creamos instancia y comenzamos
	ai = AlienInvasion()
	ai.run_game()
