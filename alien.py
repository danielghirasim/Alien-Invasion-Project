import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, my_settings):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings

        # Load the alien and get its rect
        self.image = pygame.image.load('images/enemy1.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien neart the top left of the corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        self.x += (self.my_settings.alien_speed_factor * self.my_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
