import pygame

class Ship:
    '''A class to manage the ship'''

    def __init__(self, ai_game):
        '''initialize the ship and sets its starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/coolspaceship.png')
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ship's position based on the movement flag'''
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)