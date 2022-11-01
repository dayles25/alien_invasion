import pygame
from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
    '''represents a single alien in the fleet'''
    def __init__(self, ai_game):
        '''initialize the alien and set its starting position'''
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/12b93f80-c7c0-11ea-9335-0ad96c694158.png')
        self.image = pygame.transform.scale(self.image, (91, 53))
        self.rect = self.image.get_rect()
        self.settings = Settings()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        '''return True if alien hits edge of screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        '''move the alien to the right or left'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

