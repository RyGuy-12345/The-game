import pygame
from gameparameters import *


class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagebackward = pygame.image.load('../assets/sprites/miner.PNG').convert()
        self.imageforward = pygame.image.load('../assets/sprites/miner.PNG').convert()
        self.imagebackward = pygame.transform.flip(self.imageforward, True, False)
        self.imageforward.set_colorkey((0, 0, 0))
        self.imagebackward.set_colorkey((0, 0, 0))
        self.image = self.imageforward
        self.rect = self.imageforward.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
       self.y_speed = -1*PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1*PLAYER_SPEED
        self.image = self.imageforward

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.imagebackward


    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        #need to stop player if it goes off screen
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > screen_width-tile_size:
            self.x = screen_width-tile_size
        if self.x < 0:
            self.x = 0
        if self.y > screen_height-tile_size:
            self.y = screen_height-tile_size
        if self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y





    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.rect.x = 64

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagebackward = pygame.image.load('../assets/sprites/miner2.png').convert()
        self.imageforward = pygame.image.load('../assets/sprites/miner2.png').convert()
        self.imagebackward = pygame.transform.flip(self.imageforward, True, False)
        self.imageforward.set_colorkey((0, 0, 0))
        self.imagebackward.set_colorkey((0, 0, 0))
        self.image = self.imageforward
        self.rect = self.imageforward.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
       self.y_speed = -1*PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1*PLAYER_SPEED
        self.image = self.imageforward

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.imagebackward


    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > screen_width-tile_size:
            self.x = screen_width-tile_size
        if self.x < 0:
            self.x = 0
        if self.y > screen_height-tile_size:
            self.y = screen_height-tile_size
        if self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y





    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.rect.x = 200


