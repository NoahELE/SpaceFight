import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, sf_settings, screen):
        super().__init__()
        self.screen = screen
        self.sf_settings = sf_settings
        self.image = pygame.image.load('images/alien.png')

