import pygame
from constants import *

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # flip() the display to put your work on screen
        pygame.display.flip()
        

if __name__=="__main__":
    main()