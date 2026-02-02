import pygame
import os
from circleshape import CircleShape
from constants import PLAYER_RADIUS


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

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.original_image, -self.rotation)
        rect = rotated.get_rect(center=self.position)
        screen.blit(rotated, rect)
