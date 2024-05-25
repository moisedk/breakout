# Imports
from config import *
import pygame
from pygame.locals import *
import time

class Block:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.alive = True
    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)
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
        
        # self.paddle = Paddle(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 30, 100, 10, BLACK, PADDLE_SPEED)
        self.blocks = self.create_blocks()
        
    def create_blocks(self):
        blocks = []
        rows = 5
        cols = 10
        block_width = WINDOW_WIDTH // cols
        block_height = 20
        
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE]
        for row in range(rows):
            for col in range(cols):
                x = col * block_width
                y = row * block_height
                color = colors[row % len(colors)]
                block = Block(x,y, block_width, block_height, color)
                blocks.append(block)
        return blocks
        
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
        # Draw blocks
            for block in self.blocks:
                block.draw(self.surface)

            pygame.display.flip()
            time.sleep(SLEEP_TIME)
        # Stops the game process.
        pygame.quit()
# Runs the game process if this is the main file.
if __name__ == "__main__":
    game = Game()
    game.run()