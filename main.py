import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.is_collided(shot):
                    asteroid.kill()
                    shot.kill()

        pygame.Surface.fill(window, "black")

        for drawable in drawables:
            drawable.draw(window)

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
