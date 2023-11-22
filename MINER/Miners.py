import time
import pygame
import sys
from gameparameters import *
from display import *
from diamonds import *
from player import *

#make a main menu
#fix the movement bug
#make a closing menu
#make dirt change color once dug
#make sprites spawn on upper left and right corners of dirt
#stop diamonds from spawning in the sky
#make dinamite


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
player1 = Player1(screen_width/2, screen_height/2)
p1_score = 0
player2 = Player2(screen_width/2, screen_height/2)
p2_score = 0

#when the list is empty set running to false
while running and diamond_list:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.move_up()
            if event.key == pygame.K_DOWN:
                player1.move_down()
            if event.key == pygame.K_LEFT:
                player1.move_left()
            if event.key == pygame.K_RIGHT:
                player1.move_right()
            if event.key == pygame.K_w:
                player2.move_up()
            if event.key == pygame.K_s:
                player2.move_down()
            if event.key == pygame.K_a:
                player2.move_left()
            if event.key == pygame.K_d:
                player2.move_right()
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_UP or pygame.K_LEFT or pygame.K_DOWN or pygame.K_RIGHT:
                player1.stop()
            if event.type == pygame.K_a or pygame.K_d or pygame.K_s or pygame.K_w:
                player2.stop()
## this idea did not work
            #update to make only one player stop K_A OR K_S OR K_d

    if diamond_list == 0:
        pygame.quit()


#print mine
    mine.blit(background, (0, 0))
#update miner
    player1.update()
    player1.draw(mine)
    player2.update()
    player2.draw(mine)
    idx1 = 0
    idx2 = 0
#print diamonds
    for diamond in diamond_list:
        diamond.draw_diamonds(mine)
        result1 = pygame.sprite.collide_rect(player1, diamond)
        result2 = pygame.sprite.collide_rect(player2, diamond)
        if result1:
            diamond_list.pop(idx1)
            p1_score += 1
        #pop when collide with character
        if idx1 == len(diamond_list):
            idx1 = 0
        else:
            idx1 += 1

        if result2:
            diamond_list.pop(idx2)
            p2_score += 1
        if idx2 == len(diamond_list):
            idx2 = 0
        else:
            idx2 += 1

    pygame.display.flip()



#create screen for game over

mine.blit(background, (0, 0))
font = pygame.font.Font("../assets/fonts/Montague.ttf", 100)
message = font.render("GAME OVER", True, (0, 0, 0))
mine.blit(message, (screen_width/2 - message.get_width()/2, screen_height/6))
score1_text = font.render(f'PLAYER 1 SCORE: {p1_score}', True, (0, 0, 0))
mine.blit(score1_text, (screen_width/2 - score1_text.get_width()/2, screen_height/4 +score1_text.get_height()))
score2_text = font.render(f'PLAYER 2 SCORE: {p2_score}', True, (0, 0, 0))
mine.blit(score2_text, (screen_width/2 - score2_text.get_width()/2, screen_height/2 +score2_text.get_height()))
pygame.display.flip()
time.sleep(5)
pygame.quit()


