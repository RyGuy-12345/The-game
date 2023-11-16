import time

import pygame
import sys
from gameparameters import *
from display import *
from diamonds import *

#initialize pygame
pygame.init()

mine = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("the children yern for the mines")

#set clock
clock = pygame.time.Clock()

running = True
background = mine.copy()
draw_background(background)

num_diamonds = 5
diamond_list = []
for _ in range(0, num_diamonds):
    diamond_list.append(Diamonds(mine))

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    mine.blit(background, (0, 0))

    for diamond in diamond_list:
        diamond.draw_diamonds(mine)
        #pop when collide with character
    pygame.display.flip()


    pygame.display.flip()
