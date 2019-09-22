class Settings:
    def __init__(self):
        #!screen instance variable
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (142, 243, 79)

        #!ship speed
        self.ship_speed = 3.5
        self.ship_limit = 3

        #!bullet instance variable
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 16
        self.bullet_color = (0, 255, 0)
        self.bullet_allowed = 3

        # Alien setting
        self.alien_speed = 3.0
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 4
        self.bullet_speed = 6.5
        self.alien_speed = 3.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
