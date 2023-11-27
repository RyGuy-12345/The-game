import pygame
from gameparameters import *
import random



def main_menu():




def Restart_menu():
    mine.blit(background, (0, 0))
    font = pygame.font.Font("../assets/fonts/Montague.ttf", 50)
    message = font.render("GAME OVER", True, (0, 0, 0))
    mine.blit(message, (screen_width / 2 - message.get_width() / 2, screen_height / 6))
    score1_text = font.render(f'PLAYER 1 SCORE: {p1_score}', True, (0, 0, 0))
    mine.blit(score1_text,
              (screen_width / 2 - score1_text.get_width() / 2, screen_height / 4 + score1_text.get_height()))
    score2_text = font.render(f'PLAYER 2 SCORE: {p2_score}', True, (0, 0, 0))
    mine.blit(score2_text,
              (screen_width / 2 - score2_text.get_width() / 2, screen_height / 3 + score2_text.get_height()))
    play_again = font.render("PLAY AGAIN", True, (0, 0, 0,))
    mine.blit(play_again, (screen_width / 2 - play_again.get_width() / 2, screen_height / 1.5))
    button_2 = play_again
    quit_text = font.render("QUIT", True, (0, 0, 0))
    mine.blit(quit_text, (screen_width / 2 - quit_text.get_width() / 2, screen_height / 1.25))
    button_3 = quit_text
    pygame.display.flip()

    time.sleep(5)
    pygame.quit()