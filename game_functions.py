import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet

"""A module that has different functions for the game"""


def check_event(my_ship, screen, my_settings, bullets, stats, play_button, aliens, sb):
    """Checks for Keyboard,Mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown_events(event, my_ship, screen, my_settings, bullets, stats, aliens)
        check_keyup_events(event, my_ship)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, bullets, aliens, my_settings, my_ship, screen, sb)


def check_play_button(stats, play_button, mouse_x, mouse_y, bullets, aliens, my_settings, my_ship, screen,sb):
    """Start a new game when the player click Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:  # 'Not stats.game_active' = you can only click it when the game is not active
        # Hide mouse cursor
        pygame.mouse.set_visible(False)  # Makes mouse invisible when game active

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Reset game settings
        my_settings.initialize_dynamic_settings()

        # Empty the list of aliens and bullets
        bullets.empty()
        aliens.empty()

        # Create a new fleet and center the ship
        create_fleet(my_settings, my_ship, screen, aliens)
        my_ship.center_ship()


def start_game(stats, bullets, aliens, my_settings, my_ship, screen):
    """Start a new game when the player presses 'p' """
    if not stats.game_active:  # 'Not stats.game_active' = you can only click it when the game is not active
        # Hide mouse cursor
        pygame.mouse.set_visible(False)  # Makes mouse invisible when game active

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset game settings
        my_settings.initialize_dynamic_settings()

        # Empty the list of aliens and bullets
        bullets.empty()
        aliens.empty()

        # Create a new fleet and center the ship
        create_fleet(my_settings, my_ship, screen, aliens)
        my_ship.center_ship()


def display_update(screen, my_ship, my_settings, bullets, aliens, my_background, play_button, stats, sb):
    """Updates the screen with ship , bullets , etc"""
    screen.fill(my_settings.bg_color)
    screen.blit(my_background, (0, 0))
    my_ship.blitme()
    my_ship.update()
    bullets.update()
    aliens.draw(screen)

    # This draws my bullets on the screen because I fked something up I had to put it here
    for each in bullets.sprites():
        each.draw_bullets()

    # Draw the score information.
    sb.show_score()

    # Draw the play button if game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def create_fleet(my_settings, my_ship, screen, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of alien in a row
    alien = Alien(screen, my_settings)
    number_aliens_x = get_number_aliens_x(my_settings, alien.rect.width)
    number_rows = int(get_number_rows(my_settings, my_ship.rect.height, alien.rect.height))

    # Create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen, my_settings, aliens, alien_number, row_number)


def update_aliens(my_settings, aliens, my_ship, stats, screen, bullets, sb):
    """Check if the fleet is at an edge and the update position
    of all aliens in the fleet"""
    check_fleet_edges(my_settings, aliens)
    aliens.update()
    check_aliens_hit_bottom(my_settings, stats, screen, my_ship, aliens, bullets, sb)
    # Look for Ship - Alien collision
    if pygame.sprite.spritecollideany(my_ship, aliens):
        ship_hit(my_settings, stats, screen, my_ship, aliens, bullets, sb)
        print("Ship Hit!!")


def check_aliens_hit_bottom(my_settings, stats, screen, my_ship, aliens, bullets , sb):
    """Check if any aliens hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        """Treat it the same way as if ship is hit"""
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(my_settings, stats, screen, my_ship, aliens, bullets, sb)
            break


def check_bullet_misses(my_settings, stats, screen, my_ship, aliens, bullets,sb):
    """We check if the bullets top rect is lower that screen_top rect
    if it is then we increment miss count with 1 if it reaches 3 we register
    it as a ship_hit and reset."""
    screen_rect = screen.get_rect()
    for bullet in bullets:
        if bullet.rect.top < screen_rect.top:
            my_settings.miss_count += 1
            if my_settings.miss_count > my_settings.miss_limit:
                ship_hit(my_settings, stats, screen, my_ship, aliens, bullets, sb)


def ship_hit(my_settings, stats, screen, my_ship, aliens, bullets, sb):
    """Respond to ship being hit by alien
    + I added bullet miss limit """
    if stats.ships_left > 0 and stats.miss_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1
        stats.miss_left -= 1
        stats.ships_left -= 1
        my_settings.miss_count = 0

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Preps ships image after ship was hit
        sb.prep_ships()


        # Create a new fleet and center the ship
        create_fleet(my_settings, my_ship, screen, aliens)
        my_ship.center_ship()

        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_direction(my_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += my_settings.fleet_drop_speed
    my_settings.fleet_direction *= -1


def check_fleet_edges(my_settings, aliens):
    """Respond appropriately if any alien have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direction(my_settings, aliens)
            break


def create_alien(screen, my_settings, aliens, alien_number, row_number):
    """Create an alien an place it in a row"""
    alien = Alien(screen, my_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(my_settings, alien_width):
    available_space_x = my_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(my_settings, ship_height, alien_height):
    """Determine number of rows of aliens that fit on a screen"""
    available_space_y = (my_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = available_space_y / (2 * alien_height)
    return number_rows


def check_keydown_events(event, my_ship, screen, my_settings, bullets, stats, aliens):
    """Checks for KEY_DOWN events"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            start_game(stats, bullets, aliens, my_settings, my_ship, screen)
    if event.type == pygame.KEYDOWN and stats.game_active:
        if event.key == pygame.K_RIGHT:
            my_ship.moving_right = True
        if event.key == pygame.K_LEFT:
            my_ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            shoot_bullet(bullets, my_settings, my_ship, screen)


def check_keyup_events(event, my_ship):
    """Checks for KEY UP events"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            my_ship.moving_right = False
        if event.key == pygame.K_LEFT:
            my_ship.moving_left = False


def remove_old_bullets(bullet, bullets, my_ship):
    """Removes the old bullets"""
    if bullet.rect.y < my_ship.screen_rectangles.top:
        bullet.remove(bullets)


def shoot_bullet(bullets, my_settings, my_ship, screen):
    """Shoots maximum 3 bullets at one time"""
    if len(bullets) < 3:
        new_bullet = Bullet(my_settings, my_ship, screen)
        bullets.add(new_bullet)


def update_bullets(aliens, bullets, my_settings, my_ship, screen, stats, sb):
    """Update position of bullets and get rid of old bullets."""
    for bullet in bullets.sprites():
        bullet.draw_bullets()
        remove_old_bullets(bullet, bullets, my_ship)

    check_bullet_alien_collision(bullets, aliens, my_settings, my_ship, screen, stats, sb)


def check_bullet_alien_collision(bullets, aliens, my_settings, my_ship, screen, stats, sb):
    # Check for any bullet if it has hit an alien
    # If so , get rid of the bullet and alien
    # And make a new fleet of aliens

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += my_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(sb, stats)
        display_level(sb)
        sb.prep_ships()

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet
        bullets.empty()
        # Increases game speed
        my_settings.increase_speed()
        # Increments level by 1
        increment_level(stats)
        # Creates new fleet
        create_fleet(my_settings, my_ship, screen, aliens)

def check_high_score(sb,stats):
    """Check to see if there is any new highscore"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def display_level(sb):
    """Displays level"""
    sb.prep_level()

def increment_level(stats):
    stats.level += 1