import pygame
from sys import argv
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import logger_setup
from colors import *
from player import Player
from skeleton import Skeleton
from skeleton_hord import SkeletonHord
from shot import PlayerShot, SkeletonShot

def main():
    if argv[1] == "debug":
        logger_setup()

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    skel_count = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    skeletons = pygame.sprite.Group()
    skel_hord = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Skeleton.containers = (skeletons, drawable, updatable)
    SkeletonHord.containers = (skel_hord)
    PlayerShot.containers = (updatable, drawable, shots)
    SkeletonShot.containers = (updatable, drawable, shots)

    # Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    skeleton_hord = SkeletonHord()

    # Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        for drawables in drawable:
            drawables.draw(screen)
        updatable.update(dt, player, skeletons)
        while skel_count < 3:
            skel_hord.update(dt, player)
            skel_count += 1
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()