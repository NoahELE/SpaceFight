class Settings():
    # save the settings for the game

    def __init__(self):
        #screen
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (200, 200, 200)

        #ship
        self.ship_speed = 0.5

        #bullet
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        #alien
        self.alien_speed = 0.5
        self.alien_direction = 1
        self.fleet_drop_speed = 5