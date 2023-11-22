import random

import pygame
from gameparameters import *

class Dynamite(pygame.sprite.Sprite):
    def __init__(self, scr):
        super().__init__()
        self.image1 = pygame.image.load("../assets/sprites/dirt1.PNG").convert()
        self.image1.set_colorkey((0,0,0))
        self.rect = self.image1.get_rect()
        self.image2 = pygame.image.load("../assets/sprites/Capture.PNG").convert()
        self.image2.set_colorkey((0, 0, 0))
        self.rect = self.image2.get_rect()

        # Choose random loaction.
        self.x = random.randint(0, screen_width-tile_size/2)
        self.y = random.randint(0, screen_height-tile_size*2)

        self.rect.center = (self.x, self.y)


