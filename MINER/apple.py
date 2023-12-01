import random

import pygame
from gameparameters import *

class Apple(pygame.sprite.Sprite):
    def __init__(self, scr):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/apple.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        # Choose random location.
        self.x = random.randint(0, screen_width-tile_size)
        self.y = random.randint(75, screen_height-tile_size)

        self.rect.center = (self.x, self.y)

    def draw_apple(self, scr):

        # Copy to screen.
        scr.blit(self.image, (self.x, self.y))