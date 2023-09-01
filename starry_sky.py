import sys
import pygame

class StarrySky:
    """Draw a grid of stars across the screen randomly spaced (using sprites)"""
    def __init__(self):
        """Initialize app resources and attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

    def run_app(self):
        while True:
            self._check_events()
            self._update_screen()
            
            pygame.display.flip()

    def _check_events(self):
        """Checks for keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _update_screen(self):
        """Updates screen"""
        self.screen.fill((0,0,30))

if __name__ == '__main__':
    ss = StarrySky()
    ss.run_app()