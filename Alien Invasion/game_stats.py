class GameStats:
    """Guardamos las estadísticas del juego."""

    def __init__(self, ai_game):
        """Inicializamos las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Inicializamos estadístcas que cambiarán luego"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.bullet_style=1
        self.bullet_counter = 0

    def check_bullet_change(self):
        """Cambia bullet_style segun tramo de counter"""
        print (self.bullet_counter)
        if self.bullet_counter < 100:
            self.bullet_style = 1
        elif self.bullet_counter  >= 100 and self.bullet_counter < 200:
            self.bullet_style = 2
        elif self.bullet_counter  >= 200 and self.bullet_counter < 300:
            self.bullet_style = 3
        elif self.bullet_counter  >= 300 and self.bullet_counter< 400:
            self.bullet_style = 4

    def reset_bullets(self):
        self.bullet_style = 1
        self.bullet_counter = 0
