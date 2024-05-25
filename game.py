# Imports
from config import *
import pygame
from pygame.locals import *
import time

pygame.draw.rect()

# Class to run the pygame itself.
class Game:
    '''Initializes the class and its variables.'''
    def __init__(self) -> None:
        pygame.init()
        # Variable for checking if pygame is running
        # Iniitalizes to True so the game continues when run is called.
        self.running = True

        # Sets the window title
        pygame.display.set_caption("Breakout")
        # Sets the window display width and height.
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        # Makes the background white.
        self.surface.fill(WHITE)

    '''When this function is called, it checks to make sure the pygame's running
       boolean is True. Then it continues to run the variable.'''
    def run(self):
        # Checks to make sure the game should run.
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print("the up key has been pressed down")
            pygame.display.flip()
            time.sleep(SLEEP_TIME)
        
        # Stops the game process.
        pygame.quit()

# Runs the game process if this is the main file.
if __name__ == "__main__":
    game = Game()
    game.run()
