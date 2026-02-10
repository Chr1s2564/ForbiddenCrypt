import os
import pygame
import random
import math
from circleshape import CircleShape
from constants import SKELETON_SPRITES, SKELETON_TURN_SPEED, SKELETON_SPEED, SKELETON_SHOOT_COOLDOWN, SHOT_RADIUS, SKELETON_HEALTH, PLAYER_SHOT_DMG, HIT_RADIUS
from shot import SkeletonShot, PlayerShot

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
        self.health = SKELETON_HEALTH
        self.state = "wander"
        self.wander_timer = 0
        self.wander_target = None

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.original_image, -self.rotation)
        screen.blit(rotated, self.rect)

    def rotate(self, dt):
        self.rotation += (dt * SKELETON_TURN_SPEED)

    def wander(self, dt):
        self.wander_timer -= dt
        if not self.wander_target or self.wander_timer <= 0:
            angle = random.uniform(0, math.pi * 2)
            distance = random.randint(50, 200)
            self.wander_target = pygame.Vector2(
                self.position.x + math.cos(angle) * distance,
                self.position.y + math.sin(angle) * distance
            )
            self.wander_timer = random.uniform(1.5, 3)
        direction = self.wander_target - self.position
        if direction.length() > 5:
            direction = direction.normalize()
            self.position += direction * SKELETON_SPEED * dt

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

    def got_shot(self, shot):
        if self.position.distance_to(shot.position) <= HIT_RADIUS and isinstance(shot, PlayerShot):
            return 1
        else:
            return 0

    def get_valid_skeletons(self, skeletons):
        valid_skeletons = [skel for skel in skeletons if hasattr(skel, "position")]
        if not valid_skeletons:
            return None
        if valid_skeletons:
            return valid_skeletons

    def update(self, dt, player, skeleton, shots):
        is_moving = 0
        self.cooldown -= dt
        distance = self.position.distance_to(player.position)

        if distance < 200:
            self.state = "combat"
        else:
            self.state = "wander"

        if self.state == "wander":
            self.wander(dt)
        elif self.state == "combat":
            if distance < 80: # AI keeps player at shooting range but not to close
                self.move_away(player, dt)
                is_moving = 1
            if distance > 150:
                self.move_towards(player, dt)
                is_moving = 1
            if distance < 150 and not is_moving and player.is_alive:  # shooting handling
                if self.cooldown > 0:
                    pass
                else:
                    self.cooldown = SKELETON_SHOOT_COOLDOWN
                    # self.shoot(player)

        for shot in shots:
            if isinstance(shot, PlayerShot) and self.got_shot(shot): # Got_shot handling
                self.health -= PLAYER_SHOT_DMG
                print(f"skel health = {self.health}")
                shot.kill()

        if self.health <= 0:
            self.kill()

        self.rect.center = self.position
