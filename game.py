'''Authors: Jhon Paul Espiritu, Sukhreen Sandhu, Moisedk
   Date: 5/24/ 2024
'''

# Imports
from config import *
import pygame
from pygame.locals import *
import time
import random

# Initializes offsets for the ball.
BALL_X_OFFSET, BALL_Y_OFFSET = (WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)

# Initializes an individual Block class for inserting the files themselves.
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
    '''Intializes the ball to be used in-game.'''
    def ball_init(self) -> None:
        self.ball = pygame.draw.circle(self.surface, WHITE, self.ball_offset, BALL_RADIUS)

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

    '''Randomizes the ball's X and Y movement.'''
    def randomize_ball_movement(self, x_movement) -> None:
        self.ball_random = (x_movement, random.randrange(-10, 10, 9))


    '''Initializes the class and its variables.'''
    def __init__(self) -> None:
        pygame.init()
        # Variable for checking if pygame is running
        # Iniitalizes to True so the game continues when run is called.
        self.running = True

        # Sets the window title
        pygame.display.set_caption("Breakout")
        # Sets the window display.
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        # Makes the background white.
        self.surface.fill(BLACK)

        # Initializes the ball's offset, and the movement it should take.
        self.ball_offset = (BALL_X_OFFSET, BALL_Y_OFFSET)
        self.randomize_ball_movement(random.randrange(-10, 10, 9))
        self.ball_init()

        # Initializes the blocks
        # self.paddle = Paddle(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 30, 100, 10, BLACK, PADDLE_SPEED)
        self.blocks = self.create_blocks()

    '''When this function is called, it checks to make sure the pygame's running
       boolean is True. Then it continues to run the variable.'''
    def run(self):

        # Checks to make sure the game should run.
        while self.running:
            # Ensures that canvas has been reset to black before other elements are initialized.
            self.surface.fill(BLACK)

            for event in pygame.event.get():
                # Checks to see if the process should quit.
                if event.type == pygame.QUIT:
                    self.running = False
                # Keydown elements.
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print("the up key has been pressed down")
                    if event.key == K_DOWN:
                        print("the down key has been pressed down")
            # Functions for moving the blocks.
            for block in self.blocks:
                block.draw(self.surface)

            # Functions for moving ball itself.
            self.ball.move_ip(self.ball_random)
            if self.ball.right == WINDOW_WIDTH:
                self.randomize_ball_movement(-self.ball_random[0])
            if self.ball.top == WINDOW_HEIGHT:
                self.randomize_ball_movement()
            if self.ball.left == 0:
                self.randomize_ball_movement(-self.ball_random[0])
            if self.ball.bottom == 0:
                self.randomize_ball_movement()
                
            self.ball_offset = (self.ball.centerx, self.ball.centery)
            self.ball = pygame.draw.circle(self.surface, WHITE, self.ball_offset, BALL_RADIUS)
            pygame.display.flip()
            # Controls ticks.
            time.sleep(SLEEP_TIME)
        
        # Stops the game process.
        pygame.quit()

# Runs the game process if this is the main file.
if __name__ == "__main__":
    game = Game()
    game.run()
