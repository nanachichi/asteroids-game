import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)
        pygame.Surface.fill(window, "black")

        for drawable in drawables:
            drawable.draw(window)

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
