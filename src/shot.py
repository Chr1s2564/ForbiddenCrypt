import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class PlayerShot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, LINE_WIDTH)

    def update(self, dt, other):
        self.position += self.velocity * dt

class SkeletonShot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, LINE_WIDTH)

    def update(self, dt, other):
        self.position += self.velocity * dt

