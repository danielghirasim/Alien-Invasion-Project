import pygame.font


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, my_settings, screen, stats):
        """Init scorekeeping attributes"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = my_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a render image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the right top part of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top - 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image,self.screen_rect)