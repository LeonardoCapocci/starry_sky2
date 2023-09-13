import sys
import pygame
from random import randint

from star import Star

class StarrySky:
    """Draw a grid of stars across the screen randomly spaced (using sprites)"""
    def __init__(self):
        """Initialize app resources and attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.all_stars = pygame.sprite.Group()
        self.screen.fill((0,0,30))
        self.create_starry_sky()
        self.all_stars.draw(self.screen)

    def run_app(self):

        while True:
            self._check_events()
            self.clock.tick(60)
            pygame.display.flip()

    def _check_events(self):
        """Checks for keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_star(self, x_position, y_position):
        """Creates a single star the star."""
        new_star = Star(self, x_position, y_position)
        self.all_stars.add(new_star)
        
    def create_starry_sky(self):
        """Create the grid of stars."""
        screen_width, screen_height = self.screen.get_size()
        current_x, current_y = 100, 100
        
        while current_y < screen_height - 100:
            while current_x < screen_width - 100:
                self._create_star(current_x, current_y)
                current_x += randint(80, 300)
            current_x = 100
            current_y += randint(80, 300)
        

if __name__ == '__main__':
    ss = StarrySky()
    ss.run_app()
