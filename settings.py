class Settings():

    def __init__(self):
        """Different Settings Troughout the game"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.screen_title = "Alien Invasion"

        # Ship settings
        self.ship_speed_factor = 2
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = (255, 255, 255)
        self.bullet_speed_factor = 5
        self.miss_limit = 1 # Default 5
        self.miss_count = 0

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction of 1 is represents right -1 represents left
        self.fleet_direction = 1
