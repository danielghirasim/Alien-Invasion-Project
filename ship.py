import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen, my_settings):
        super().__init__()
        """We create our main ship"""
        self.screen = screen
        self.settings = my_settings

        self.image = pygame.image.load('images/ship.bmp')

        # We get the rectangles of the image and screen
        self.rect = self.image.get_rect()
        self.screen_rectangles = self.screen.get_rect()

        # We set the ships position by settings the rectangles of the ship
        # To the bottom mid rectangles of the screen
        self.rect.centerx = self.screen_rectangles.centerx
        self.rect.bottom = self.screen_rectangles.bottom

        # Movement Flags

        self.moving_left = False
        self.moving_right = False

        # Transforming ship rect center to a decimal so we can add it together with speed factor
        self.ship_center = float(self.rect.centerx)
        # We get the speed factor from settings
        self.speed_factor = my_settings.ship_speed_factor

    def update(self):
        """We update the ships position when we press the keys"""
        if self.moving_left and self.rect.left > 0:
            self.ship_center -= self.speed_factor
        if self.moving_right and self.rect.right < self.screen_rectangles.right:
            self.ship_center += self.speed_factor

        # We get the rectangles from ship center so we can update it

        self.rect.centerx = self.ship_center

    def center_ship(self):
        """Center the ship on the screen"""
        self.ship_center = self.screen_rectangles.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
