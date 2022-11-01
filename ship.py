import pygame

class Ship:
    '''A class to manage the ship'''

    def __init__(self, ai_game):
        '''initialize the ship and sets its starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/coolspaceship.png')
        self.image = pygame.transform.scale(self.image, (100, 125))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ship's position based on the movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)