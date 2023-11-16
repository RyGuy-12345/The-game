import pygame
from gameparameters import *
import random


#draw background
def draw_background(mine):
    dirt1 = pygame.image.load("../assets/sprites/dirt1.png").convert()
    top_soil = pygame.image.load("../assets/sprites/top_soil.png").convert()
    top_soil.set_colorkey((245, 245, 245))
    dirt1.set_colorkey((0, 0, 0))

    #sky
    color = (98, 189, 217)

    # Changing surface color
    mine.fill(color)

    #Unmined dirt
    for x in range(0,screen_width,tile_size):
        for y in range(tile_size*2,screen_height, tile_size):
            mine.blit(dirt1, (x,y))
    #grassy dirt
    for x in range(0, screen_width,tile_size):
        mine.blit(top_soil, (x,screen_height-(8*tile_size)))

    #font
    font = pygame.font.Font("../assets/fonts/Montague.ttf", 115)
    text = font.render("Miner",True,(245, 215, 66))
    mine.blit(text, (screen_width/2 - text.get_width()/2, screen_height / 9 - text.get_height()/1.5))


