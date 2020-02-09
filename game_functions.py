import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_events(sf_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kdown_events(event, sf_settings,screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_kup_events(event, ship)
        

def check_kdown_events(event, sf_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(sf_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def check_kup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullets(sf_settings, screen, ship, bullets):
    if len(bullets) < sf_settings.bullet_allowed:
        new_bullet = Bullet(sf_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(sf_settings, screen, ship, aliens, bullets):
    screen.fill(sf_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def update_bullets(sf_settings, screen, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullets_aliens_collisions(sf_settings, screen, ship, aliens, bullets)

def check_bullets_aliens_collisions(sf_settings,screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(sf_settings, screen, ship, aliens)

def get_number_aliens_x(sf_settings, alien_width):
    available_space_x = sf_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(sf_settings, ship_height, alien_height):
    available_space_y = (sf_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(sf_settings, screen, aliens, alien_number, row_number):
    alien = Alien(sf_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(sf_settings, screen, ship, aliens):
    alien = Alien(sf_settings, screen)
    number_aliens_x = get_number_aliens_x(sf_settings, alien.rect.width)
    number_rows = get_number_rows(sf_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(sf_settings, screen, aliens, alien_number, row_number)

def ship_hit(sf_settings, stats, screen, ship, aliens, bullets):
    stats.ships_left -= 1

    alien.empty()
    bullets.empty()

    create_fleet(sf_settings, screen, ship, aliens)
    ship.center_ship()

    #pause
    sleep(1)

def update_aliens(sf_settings,stats, screen, ship, aliens, bullets):
    check_fleet_edges(sf_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(sf_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(sf_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(sf_settings, aliens)
            break

def change_fleet_direction(sf_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += sf_settings.fleet_drop_speed
    sf_settings.alien_direction *= -1
