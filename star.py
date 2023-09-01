import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star"""
    def __init__(self, game):
        """Spawn a single star on the screen"""
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load('star.bmp')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        
        # Set star at top left with some breathing room
        self.rect.x = self.image.get_width()
        self.rect.y = self.image.get_height()

    def create_star(self):
        """Draws the star"""
        