import pygame


class Ship():

    def __init__(self, sf_settings, screen):
        self.screen = screen
        self.sf_settings = sf_settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put ship in the middle of the bottom of the page
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #save float in the center value
        self.center = float(self.rect.centerx)

        #signs of moving
        self.moving_right = False
        self.moving_left = False

    def check_right(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return False
        else:
            return True

    def check_left(self):
        screen_rect = self.screen.get_rect()

        if self.rect.left <= 0:
            return False
        else:
            return True

    def update(self):
        ship_in_screen_right = self.check_right()
        ship_in_screen_left = self.check_left()

        if self.moving_right and ship_in_screen_right:
            self.center += self.sf_settings.ship_speed

        if self.moving_left and ship_in_screen_left:
            self.center -= self.sf_settings.ship_speed

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx