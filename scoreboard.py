import pygame.font


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, my_settings, screen, stats, my_background):
        """Init scorekeeping attributes"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = my_settings
        self.stats = stats
        self.background = my_background

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.level_font = pygame.font.SysFont(None, 28)

        # Prepare the initial score image
        self.prep_score()

        # prep_high_score
        self.prep_high_score()

        # Prep level
        self.prep_level()

    def prep_score(self):
        """Turn the score into a render image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.background)

        # Display the score at the right top part of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.settings.screen_width - 15
        self.score_rect.top = self.settings.screen_height - (self.settings.screen_height * 0.98)

    def prep_high_score(self):
        """Turn the highscore into a rendered image"""
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.background)

        # Display highscore in the middle/top part of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.centery = 25

    def prep_level(self):
        """Displays the level under the current score"""
        self.level = int(self.stats.level)
        level_str = "Level: " + str(self.level)
        self.level_image = self.level_font.render(level_str, True, self.text_color, self.background)

        # Display highscore in the middle/top part of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.right - 55
        self.level_rect.centery = self.screen_rect.top + 75

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
