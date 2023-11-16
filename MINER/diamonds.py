import random

import pygame
from gameparameters import *

class Diamonds(pygame.sprite.Sprite):
    def __init__(self, scr):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/diamond.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        # Choose random loaction.
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)

        self.rect.center = (self.x, self.y)

    def draw_diamonds(self, scr):

        # Copy to screen.
        scr.blit(self.image, (self.x, self.y))


    #def place(self):
    #    for _ in range(7):
    #        x = random.randint(0, screen_width)
    #        mine.blit(self.image, (x, screen_height - tile_size * 2 + 5))




