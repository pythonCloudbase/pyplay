import pygame
import random

import math

from pygame import mixer
import android

mixer.init()

r = 'ready'
b = 2
space = 0
x = 50
y = 515
start = 10
width = 40
height = 5

Asteroid1 = []
Asteroid_x = []
Asteroid_y = []
Asteroid_x_change = []
Asteroid_y_change = []

for i in range(30):
    Asteroid1.append(pygame.image.load('alien.png'))
    Asteroid_x.append(random.randint(0,800))
    Asteroid_y.append(random.randint(50, 150))
    Asteroid_x_change.append(3.8)
    Asteroid_y_change.append(6)

pygame.init()

#icon = pygame.image.load('ufo.png')
#pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800,600))

background = pygame.display.set_mode((800, 600))
background = pygame.image.load('space.jpg')
pygame.display.set_caption("Space shooter")

BLUE = (100,100,255)
RED = (255,0,0)
LIME = (180,255,100)

#player = pygame.image.load('player.png')
player_x = 370
player_y = 480

#Bullet = pygame.image.load('Bullet.png')
Bullet_x = 370
Bullet_y = 480
Bullet_x_change = 9
Bullet_y_change = 60
Bullet_state = r

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)
text_x = 200
text_y = 10

def score(X,Y):
    scores = font.render('Score : {}'.format(score_value), True, BLUE)
    screen.blit(scores, (X,Y))

def fire(x,y):
    global Bullet_state
    Bullet_state = fire
    screen.blit(Bullet, (x+18, y+10))

def play(X,Y):
    