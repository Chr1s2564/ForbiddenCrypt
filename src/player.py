import pygame
import os
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


#path to sprites // currently a test sprite
base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "..", "sprites", "test_sprite.png")

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.original_image, -self.rotation)
        screen.blit(rotated, self.rect)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move_y(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        vector_speed = PLAYER_SPEED * unit_vector * dt
        self.position += vector_speed

    def move_x(self, dt):
        unit_vector = pygame.Vector2(1, 0)
        vector_speed = PLAYER_SPEED * unit_vector * dt
        self.position += vector_speed

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.move_x(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move_x(dt)
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            self.move_y(-dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move_y(dt)

        self.rect.center = self.position