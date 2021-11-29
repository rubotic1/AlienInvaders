import pygame

class Sound_fx:
	"""Clase que controla el sonido."""
	def __init__(self):
		""" Inicializamos el sonido y cargamos los recursos"""
		self.init_music = 'sound/01_Title Screen.mp3'
		self.game_music = 'sound/12_Invader_Homeworld.mp3'

		self.shot = pygame.mixer.Sound('sound/shot.wav')
		self.alien = pygame.mixer.Sound('sound/mixkit-video-game-blood-pop-2361.wav')
		self.shot_cn = pygame.mixer.Channel(1)
		self.alien_cn = pygame.mixer.Channel(2)

		self.alien_cn.set_volume(0.5)

		pygame.mixer.init()

	def play_init_music(self):
		pygame.mixer.music.load(self.init_music)
		pygame.mixer.music.play(-1)

	def play_game_music(self):
		pygame.mixer.music.load(self.game_music)
		pygame.mixer.music.play(-1)

	def play_shot(self):
		self.shot_cn.play(self.shot)

	def play_alien(self):
		self.alien_cn.play(self.alien)


