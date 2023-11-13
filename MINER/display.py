import pygame
from gameparameters import *
import random


#draw background
def draw_background(mine):
    dirt1 = pygame.image.load("../assets/sprites/dirt1.png").convert()
    top_soil = pygame.image.load("../assets/sprites/top_soil.png").convert()
    top_soil.set_colorkey((0, 0, 0))
    dirt1.set_colorkey((0, 0, 0))

    for x in range(0,screen_width,tile_size):
        for y in range(0,screen_height, tile_size):
            mine.blit(dirt1, (x,y))
    for x in range(0, screen_width,tile_size):
        mine.blit(top_soil, (x,tile_size-screen_height))
