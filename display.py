import pygame
from gameparameters import *
import random


#draw background
def draw_background(mine):
    dirt = pygame.image.load("../assets/sprites/dirt.PNG")
    top_soil = pygame.image.load("../assets/sprites/top_soil.png")
    top_soil.set_colorkey((0, 0, 0))
