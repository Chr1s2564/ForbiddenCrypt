import pygame
from constants import LINE_WIDTH, PLAYER_SHOOT_SPEED, SKELETON_SHOOT_SPEED
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
        self.source = "player"

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, LINE_WIDTH)
        ## --- Shoot debug ---
        '''pygame.draw.line(
            screen,
            "yellow",
            self.position,
            self.position + self.velocity.normalize() * 40
        )'''
        ## --- Shoot debug ---

    def collides_with(self, skeleton):
        if self.position.distance_to(skeleton.position) == 0:
            return 1
        else:
            return 0

    def update(self, dt, player, skeletons, shots):
        self.position += self.velocity * dt
        for skeleton in skeletons:
            if self.collides_with(skeleton) == 1:
                print("true")
                self.kill()

class SkeletonShot(CircleShape):
    def __init__(self, x, y, radius, player_pos):
        super().__init__(x, y, radius)
        direction = pygame.Vector2(player_pos) - self.position
        if direction.length() == 0:
            direction = pygame.Vector2(0, -1)
        if direction.length() > 0:
            direction = direction.normalize()
        self.velocity = direction * SKELETON_SHOOT_SPEED
        self.source = "skeleton"

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, LINE_WIDTH)

    def collides_with(self, player):
        if self.position.distance_to(player.position) == 0:
            return 1
        else:
            return 0

    def update(self, dt, player, skeletons, shots):
        self.position += self.velocity * dt
        if self.collides_with(player):
            self.kill()

