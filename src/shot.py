import pygame
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED
from circleshape import CircleShape


class PlayerShot(CircleShape):
    def __init__(self, x, y, radius, enemy_pos):
        super().__init__(x, y, radius)
        direction = pygame.Vector2(enemy_pos) - self.position
        if direction.length() == 0:
            direction = pygame.Vector2(0, -1)
        if direction.length() > 0:
            direction = direction.normalize()
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, LINE_WIDTH)
        ## --- Shoot debug ---
        pygame.draw.line(
            screen,
            "yellow",
            self.position,
            self.position + self.velocity.normalize() * 40
        )
        ## --- Shoot debug ---

    def update(self, dt, player, skeleton):
        self.position += self.velocity * dt

class SkeletonShot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, LINE_WIDTH)

    def update(self, dt, other):
        self.position += self.velocity * dt

