import pygame


from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    # Initialise the game and create a screen object

    pygame.init()
    sf_settings = Settings()
    screen = pygame.display.set_mode(
        (sf_settings.screen_width, sf_settings.screen_height))
    pygame.display.set_caption('Space Fight')

    #create a ship
    ship = Ship(sf_settings, screen)
    #create a Group for bullets
    bullets = Group()

    aliens = Group()

    gf.create_fleet(sf_settings, screen, ship, aliens)

    # Start the main loop of the game
    while True:
        gf.check_events(sf_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(sf_settings, screen, ship, aliens, bullets)
        gf.update_aliens(sf_settings, aliens)
        gf.update_screen(sf_settings, screen, ship, aliens, bullets)

run_game()