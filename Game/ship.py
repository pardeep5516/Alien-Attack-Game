import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    #!class to manage ship

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get it rect
        self.image = pygame.image.load('images/player.gif')
        self.rect = self.image.get_rect()

        #!strart each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        #!Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):  # !update ship movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
