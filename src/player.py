import pygame
import os
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SPRITES, PLAYER_SHOOT_SPEED, SHOT_RADIUS
from shot import PlayerShot

#path to sprites // currently a test sprite
image_path = os.path.join(PLAYER_SPRITES, "test_sprite.png")

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

    def rotate(self, dt, other):
        pass
        '''if self.position.distance_to(other.position) < 110:
            direction = pygame.Vector2(other.position) - self.position
            if direction.length() > 0:
                direction = direction.normalize()
                self.rotation += (PLAYER_TURN_SPEED * dt) * direction'''

    def move_y(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        vector_speed = PLAYER_SPEED * unit_vector * dt
        self.position += vector_speed

    def move_x(self, dt):
        unit_vector = pygame.Vector2(1, 0)
        vector_speed = PLAYER_SPEED * unit_vector * dt
        self.position += vector_speed

    def get_closest_skeleton(self, skeletons):
        valid_skeletons = [skel for skel in skeletons if hasattr(skel, "position")]
        if not valid_skeletons:
            return None
        else:
            return min(valid_skeletons, key=lambda skel: self.position.distance_to(skel.position))

    def shoot(self, other):
        shot = PlayerShot(self.position.x, self.position.y, SHOT_RADIUS, other.position)

    def update(self, dt, player, skeletons):
        keys = pygame.key.get_pressed()
        is_moving = 0
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.move_x(-dt)
            is_moving = 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move_x(dt)
            is_moving = 1
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            self.move_y(-dt)
            is_moving = 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move_y(dt)
            is_moving = 1

        target = self.get_closest_skeleton(skeletons)

        if target and is_moving == 0:
            if self.position.distance_to(target.position) < 110:
                self.shoot(target)
        self.rect.center = self.position