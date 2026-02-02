import os

# screen constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# player constants
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

# Skeleton constants
SKELETON_TURN_SPEED = 300
SKELETON_SPEED = 200
SKELETON_SPAWN_RATE = 0.8

# FILE SOURCES
BASE_PATH = os.path.dirname(__file__)
PLAYER_SPRITES = os.path.join(BASE_PATH, '..', 'sprites', 'mage')
SKELETON_SPRITES = os.path.join(BASE_PATH, '..', 'sprites', 'skeleton')
