import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
import os

base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "..", "sprites", "test_sprite.png")

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.image.load(image_path)

    def draw(self):
        pass