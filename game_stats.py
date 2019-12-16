class Stats():
    """Tracks statistics for alien invasion"""

    def __init__(self, my_settings):
        """Init statistics"""
        self.settings = my_settings
        self.reset_stats()

        # Start alien invasion in inactive state
        self.game_active = False

    def reset_stats(self):
        """Init statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.miss_left = self.settings.miss_limit
        self.score = 0
