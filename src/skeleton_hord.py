import pygame
import random
from skeleton import Skeleton

class SkeletonHord(pygame.sprite.Sprite):
    spawn_points = [
        (80, 80),
        (600, 80),
        (1100, 90),
        (1100, 360),
        (1100, 640),
        (600, 640),
        (80, 640),
        (80, 360)
    ]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, spawn_point):
        skeleton = Skeleton(spawn_point[0], spawn_point[1])

    def update(self, dt, other):
        self.spawn_timer += dt
        spawn_point = random.choice(self.spawn_points)
        self.spawn(spawn_point)


