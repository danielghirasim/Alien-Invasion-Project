import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import Stats
from settings import Settings
from ship import Ship
from scoreboard import Scoreboard

# Start the main loop for our game
def run_game():
    pygame.init()
    my_background = pygame.image.load('images/background.bmp')
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption(my_settings.screen_title)
    # Make Play button
    play_button = Button(my_settings, screen, 'Play')
    my_ship = Ship(screen, my_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(my_settings, my_ship, screen, aliens)
    stats = Stats(my_settings)
    sb = Scoreboard(my_settings, screen, stats, my_background)

    while True:
        gf.check_event(my_ship, screen, my_settings, bullets, stats, play_button, aliens)
        if stats.game_active:
            gf.check_bullet_misses(my_settings, stats, screen, my_ship, aliens, bullets)
            gf.update_aliens(my_settings, aliens, my_ship, stats, screen, bullets)
            gf.update_bullets(aliens, bullets, my_settings, my_ship, screen, stats, sb)

        gf.display_update(screen, my_ship, my_settings, bullets, aliens, my_background, play_button, stats,sb)


run_game()
