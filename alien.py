import pygame
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

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        '''move the alien to the right'''
        self.x += self.settings.alien_speed
        self.rect.x = self.x
