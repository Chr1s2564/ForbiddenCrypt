import os
import pygame
from circleshape import CircleShape
from constants import SKELETON_SPRITES, SKELETON_TURN_SPEED, SKELETON_SPEED, SKELETON_SHOOT_COOLDOWN, SHOT_RADIUS
from shot import SkeletonShot

# image path
image_path = os.path.join(SKELETON_SPRITES, 'test_skeleton.png')

class Skeleton(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=0)
        self.rotation = 0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=self.position)
        self.cooldown = 0

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.original_image, -self.rotation)
        screen.blit(rotated, self.rect)

    def rotate(self, dt):
        self.rotation += (dt * SKELETON_TURN_SPEED)

    def move_towards(self, other, dt):
        direction = pygame.Vector2(other.position) - self.position
        if direction.length() > 0:
            direction = direction.normalize()
        self.position += direction * SKELETON_SPEED * dt

    def move_away(self, other, dt):
        direction = pygame.Vector2(other.position) + self.position
        if direction.length() > 0:
            direction = direction.normalize()
        self.position += direction * SKELETON_SPEED * dt

    def shoot(self, other):
        skel_shot = SkeletonShot(self.position.x, self.position.y, SHOT_RADIUS, other.position)

    def update(self, dt, player, skeleton): # AI keeps player at shooting range but not to close
        is_moving = 0
        self.cooldown -= dt
        if self.position.distance_to(player.position) < 80:
            self.move_away(player, dt)
            is_moving = 1
        if self.position.distance_to(player.position) > 150:
            self.move_towards(player, dt)
            is_moving = 1

        if self.position.distance_to(player.position) < 150 and not is_moving:
            if self.cooldown > 0:
                pass
            else:
                self.cooldown = SKELETON_SHOOT_COOLDOWN
                self.shoot(player)

        self.rect.center = self.position
