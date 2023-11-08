import pygame
import sys
from gameparameters import *

#initialize pygame
pygame.init()

mine = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("the children yern for the mines")

#set clock
clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
