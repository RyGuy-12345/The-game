import time
import pygame
import sys
from gameparameters import *
from display import *
from diamonds import *
from player import *
from dynamite import Dynamite

#initialize pygame
pygame.init()

mine = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("the mines")

#set clock
clock = pygame.time.Clock()
running = True
background = mine.copy()
draw_background(background)

#set up timer (all help on clock was assisted by alex Dachos)
start_time = pygame.time.get_ticks()

#draw diamond
num_diamonds = 5
diamond_list = []
for _ in range(0, num_diamonds):
    diamond_list.append(Diamonds(mine))

#make dynamite
num_dynamite = 3
dynamite_list = []
for _ in range(0, num_dynamite):
    dynamite_list.append(Dynamite(mine))

#sounds
music = pygame.mixer.Sound("../assets/sounds/miners song.wav")
boom = pygame.mixer.Sound("../assets/sounds/boom.wav")
sound = pygame.mixer.Sound("../assets/sounds/inspectorshort.wav")
#inicializining the two players
player1 = Player1(screen_width/15, screen_height/20)
p1_score = 0
player2 = Player2(screen_width/1.05, screen_height/20)
p2_score = 0

click = False
while click == False:
    pygame.mixer.Sound.play(music)
    #main menu
    mine.blit(background, (0, 0))
    font = pygame.font.Font("../assets/fonts/Montague.ttf", 55)
    font1 = pygame.font.Font("../assets/fonts/Montague.ttf", 20)
    play = font.render("Click anywhere to PLAY GAME", True, (0, 0, 0))
    mine.blit(play, (screen_width/2 - play.get_width()/2, screen_height/6))
    instructions = font1.render("Try and collect as many Diamonds as you can in 30 seconds!", True, (0, 0, 0))
    mine.blit(instructions, (screen_width / 2 - instructions.get_width() / 2, screen_height / 2.25))
    instructions3 = font1.render("Beware of the hidden Dynamite!!", True, (0, 0, 0))
    mine.blit(instructions3, (screen_width / 2 - instructions3.get_width() / 2, screen_height / 2))
    instructions1 = font1.render("Player 1(red) use arrows to move and press 'm' to mine and 'n' to diffuse bombs", True, (0, 0, 0))
    mine.blit(instructions1, (screen_width / 2 - instructions1.get_width() / 2, screen_height / 1.75))
    instructions2 =font1.render("player 2(blue) use 'a','s','d','w' to move and '1' to mine and '2' to diffuse bombs", True, (0, 0, 0))
    mine.blit(instructions2, (screen_width / 2 - instructions2.get_width() / 2, screen_height / 1.50))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    pygame.display.flip()


#main loop
while running or click:
    pygame.mixer.Sound.play(music)
    for event in pygame.event.get():
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
            if event.key == pygame.K_UP:
                player1.stop()
            if event.key == pygame.K_DOWN:
                player1.stop()
            if event.key == pygame.K_LEFT:
                player1.stop()
            if event.key == pygame.K_RIGHT:
                player1.stop()
            if event.key == pygame.K_w:
                player2.stop()
            if event.key == pygame.K_s:
                player2.stop()
            if event.key == pygame.K_a:
                player2.stop()
            if event.key == pygame.K_d:
                player2.stop()

#respon more diamonds when all gone
    if len(diamond_list) == 0:
        for _ in range(0, num_diamonds):
            diamond_list.append(Diamonds(mine))

#print mine
    mine.blit(background, (0, 0))
#update miner
    player1.update()
    player1.draw(mine)
    player2.update()
    player2.draw(mine)

#calculate time
    running_time = (pygame.time.get_ticks()-start_time) // 1000
# stop once time reaches 30 sec
    if running_time >= 30:
        click = False
        running = False
#draw timer
    timer = pygame.font.Font("../assets/fonts/Montague.ttf",25)
    clock = timer.render(f"{running_time}", True, (0, 0, 0))
    mine.blit(clock, (10,10))
#indexing the dimonds and dynamite
    idx1 = 0
    idx2 = 0
    idxe1 = 0
    idxe2 = 0
#print diamonds
    for diamond in diamond_list:
        diamond.draw_diamonds(mine)
        result1 = pygame.sprite.collide_rect(player1, diamond)
        result2 = pygame.sprite.collide_rect(player2, diamond)
        #if result1:
        while result1:
            player1.stop()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        diamond_list.pop(idx1)
                        p1_score += 1
                        pygame.mixer.Sound.play(sound)
                    break
            break
        #pop when collide with character
        if idx1 == len(diamond_list):
            idx1 = 0
        else:
            idx1 += 1
            while result2:
                player2.stop()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            diamond_list.pop(idx2)
                            p2_score += 1
                            pygame.mixer.Sound.play(sound)
                        break
                break
        if idx2 == len(diamond_list):
            idx2 = 0
        else:
            idx2 += 1
    #dynamite explotion
    for dynamite in dynamite_list:
        dynamite.draw_dynamite(mine)
        bang1 = pygame.sprite.collide_rect(player1, dynamite)
        bang2 = pygame.sprite.collide_rect(player2, dynamite)
        while bang1:
            dynamite.boom(mine)
            player1.stop()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        dynamite_list.pop(idxe1)
                        p1_score -= 1
                        pygame.mixer.Sound.play(boom)
                    break
            break
        if idxe1 == len(dynamite_list):
            idxe1 = 0
        else:
            idxe1 += 1
        while bang2:
            dynamite.boom(mine)
            player2.stop()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        dynamite_list.pop(idxe2)
                        p2_score -= 1
                        pygame.mixer.Sound.play(boom)
                    break
            break
        if idxe2 == len(diamond_list):
            idxe2 = 0
        else:
            idxe2 += 1
    pygame.display.flip()

    #create screen for game over
    while running == False:
       # print(running)
        mine.blit(background, (0, 0))
        font = pygame.font.Font("../assets/fonts/Montague.ttf", 50)
        font2 = pygame.font.Font("../assets/fonts/Montague.ttf", 25)
        message = font.render("GAME OVER", True, (0, 0, 0))
        mine.blit(message, (screen_width/2 - message.get_width()/2, screen_height/6))
        score1_text = font.render(f'PLAYER 1 SCORE: {p1_score}', True, (0, 0, 0))
        mine.blit(score1_text, (screen_width/2 - score1_text.get_width()/2, screen_height/4 +score1_text.get_height()))
        score2_text = font.render(f'PLAYER 2 SCORE: {p2_score}', True, (0, 0, 0))
        mine.blit(score2_text, (screen_width/2 - score2_text.get_width()/2, screen_height/3 +score2_text.get_height()))
        play_again = font2.render("click anywhere on screen to PLAY AGAIN", True, (0, 0, 0,))
        mine.blit(play_again, (screen_width/2 - play_again.get_width()/2, screen_height/1.5))
        button_2 = play_again
        quit_text = font2.render("Press space to QUIT", True, (0, 0, 0))
        mine.blit(quit_text, (screen_width/2 -quit_text.get_width()/2, screen_height/1.25))
        button_3 = quit_text
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                running = True
                start_time = pygame.time.get_ticks()
                running_time = (pygame.time.get_ticks()-start_time) // 1000
                diamond_list = []
                for _ in range(0, num_diamonds):
                    diamond_list.append(Diamonds(mine))
                player1.stop()
                player1 = Player1(screen_width / 15, screen_height / 20)
                p1_score = 0
                player2.stop()
                player2 = Player2(screen_width / 1.05, screen_height / 20)
                p2_score = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('stop')
                    pygame.quit()





pygame.quit()

#TODO Helping hand
#Alex Dachos helped me with the timer
#Justin Mumaw helped me with the apple power-up
    #I ended up scrapping this idea because it made the game lag too much, but he still helped with it
#I helped Alex with the main menu
#TODO extra points
#multiplayer
#keyboard king
#Tiler
#Sound Blaster
#Points-r-us
#Helping hand
#Textual
#tick tock
#fancy font
#The walls are hard
#muzak
#Main menu
#all muzak is original
# most sprites are hand-drawn
