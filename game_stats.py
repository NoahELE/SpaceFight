class GameStats():
    def __init__(self, sf_settings):
        self.sf_settings = sf_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.sf_settings.ship_limit