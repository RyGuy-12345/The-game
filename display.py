import pygame
from gameparameters import *
import random


#draw background
def draw_background(mine):
    dirt = pygame.image.load("../assets/sprites/dirt.PNG")
    top_soil = pygame.image.load("../assets/sprites/top_soil.png")
    top_soil.set_colorkey((0, 0, 0))
    dirt.set_colorkey((0, 0, 0))

    for x in range(0,screen_width,tile_size):
        for y in range(0,screen_height, tile_size):
            mine.blit(dirt, (x,y))