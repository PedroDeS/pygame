import pygame
from constants import *
from player import *

#Initialize pygame, set screen size, set clock and delta variables
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#Create infinite loop for game to stay open, end code loop when window is closed 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

#Screen fill color and screen refresh
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

# limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
