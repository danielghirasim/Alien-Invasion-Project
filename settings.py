class Settings():

    def __init__(self):
        """Different Settings Troughout the game"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.screen_title = "Alien Invasion"

        # Ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 2555
        self.bullet_height = 25
        self.bullet_color = (255, 255, 255)
        self.miss_limit = 25 # Default 5
        self.miss_count = 0

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speed_up_scale = 1.1

        # Score scaling
        self.score_up_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change troughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 is represents right -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.alien_points = int(self.score_up_scale * self.alien_points)

    def reset_to_default(self):
        """Resets the settings to default after testing"""
        self.miss_limit = 5
        self.bullet_width = 5
        self.bullet_height = 25
        self.speed_up_scale = 1.1