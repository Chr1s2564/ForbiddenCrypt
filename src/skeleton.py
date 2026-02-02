import os
import pygame
from circleshape import CircleShape
from constants import SKELETON_SPRITES, SKELETON_TURN_SPEED, SKELETON_SPEED

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

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.original_image, -self.rotation)
        screen.blit(rotated, self.rect)

    def rotate(self, dt):
        self.rotation += (dt * SKELETON_TURN_SPEED)

    def move_x(self, dt):
        unit_vector = pygame.Vector2(1, 0)
        vector_speed = SKELETON_SPEED * dt * unit_vector
        self.position += vector_speed

    def move_y(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        vector_speed = SKELETON_SPEED * dt * unit_vector
        self.position += vector_speed

    def update(self, dt):
        pass

    ## AI will be in certain range from player
