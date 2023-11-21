import time

import pygame
import sys
from gameparameters import *
from display import *
from diamonds import *
from player import Player

#initialize pygame
pygame.init()

mine = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("the children yern for the mines")

#set clock
clock = pygame.time.Clock()

running = True
background = mine.copy()
draw_background(background)

#draw diamond
num_diamonds = 5
diamond_list = []
for _ in range(0, num_diamonds):
    diamond_list.append(Diamonds(mine))

#miner
player = Player(screen_width/2, screen_height/2)



while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()

#print mine
    mine.blit(background, (0, 0))
#update miner
    player.update()
    player.draw(mine)
#print diamonds
    for diamond in diamond_list:
        diamond.draw_diamonds(mine)
        result = pygame.sprite.collide_rect(player, diamond)
        print(result)
        if result:
            diamond_list.pop()
        #pop when collide with character
    pygame.display.flip()

score = len(diamond_list)

#create screen for game over
mine.blit(background, (0, 0))
font = pygame.font.Font("../assets/fonts/Montague.ttf", 115)
message = font.render("GAME OVER", True, (0, 0, 0))
mine.blit(message, (screen_width/2 - message.get_width()/2, screen_height/2))
score_text = font.render(f'Score: {score}', True, (0, 0, 0))
mine.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 +score_text.get_height()))
time.sleep(2)
pygame.display.flip()


