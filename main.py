import pygame
from sys import argv
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import logger_setup


pygame.init()

def main():
    if argv[1] == "debug":
        logger_setup()
    if argv[1] != "debug":
        pass
    print(f"Runing pygame version: {pygame.version}")



if __name__ == "__main__":
    main()