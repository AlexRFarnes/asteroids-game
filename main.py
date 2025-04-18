import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt  = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # group with all updatable objects
        updatable.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()
                

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # drawable is a group containing all objects that should be drawn on screen
        for object in drawable:
            object.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000 # tick -> millisencods / 1000 -> seconds (returns the delta time)
        
    pygame.quit()

if __name__=="__main__":
    main()