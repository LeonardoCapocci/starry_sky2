import pygame
from pygame.sprite import Sprite

from random import randint

class Star(Sprite):
    """A class to represent a single star"""
    def __init__(self, game, x_position, y_position):
        """Spawn a single star on the screen"""
        super().__init__()
        self.screen = game.screen
        size = randint(20, 100)

        self.image = pygame.image.load('star.bmp')
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect()
        
        self.rect.x = x_position
        self.rect.y = y_position