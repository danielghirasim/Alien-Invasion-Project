import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """We create a subclass of Sprite called bullet
    Which defines our bullets"""

    def __init__(self, my_settings, my_ship, screen):
        super().__init__()
        self.settings = my_settings
        self.screen = screen

        self.rect = pygame.Rect(0, 0, my_settings.bullet_width, my_settings.bullet_height)
        self.rect.centerx = my_ship.rect.centerx
        self.rect.top = my_ship.rect.top

        self.speed_factor = my_settings.bullet_speed_factor
        self.y = float(self.rect.y)  # we get the bullets Y position

    def update(self):
        """Updates each bullets Y position"""
        self.y -= self.speed_factor  # We speed factor from Y Position
        self.rect.y = self.y

    def draw_bullets(self):
        """Draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
