import pygame
from sys import argv
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import logger_setup
from colors import *
from player import Player

def main():
    if argv[1] == "debug":
        logger_setup()

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()