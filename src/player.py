import pygame
import os
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_SPRITES, PLAYER_SHOOT_COOLDOWN, SHOT_RADIUS, SKELETON_SHOT_DMG, PLAYER_HEALTH, HIT_RADIUS
from shot import PlayerShot, SkeletonShot

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
        self.cooldown = 0
        self.health = PLAYER_HEALTH
        self.is_alive = True

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.original_image, -self.rotation)
        screen.blit(rotated, self.rect)

    def rotate(self, dt, other):
        pass

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

    def got_shot(self, shot):
        if self.position.distance_to(shot.position) <= HIT_RADIUS and isinstance(shot, SkeletonShot):
            return 1
        else:
            return 0

    def update(self, dt, player, skeletons, shots):
        keys = pygame.key.get_pressed()
        is_moving = 0
        self.cooldown -= dt
        if keys[pygame.K_q] or keys[pygame.K_LEFT]: # movements handling
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

        for shot in shots:
            if self.got_shot(shot): # got shot handling
                self.health -= SKELETON_SHOT_DMG
                print(f"player health = {self.health}")
                shot.kill()

        if self.health <= 0:
            self.kill()
            self.is_alive = False

        target = self.get_closest_skeleton(skeletons) # shooting handling
        if target and not is_moving:
            if self.position.distance_to(target.position) < 110:
                if self.cooldown > 0:
                    pass
                else:
                    self.cooldown = PLAYER_SHOOT_COOLDOWN
                    self.shoot(target)

        self.rect.center = self.position