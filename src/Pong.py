import pickle
import sys
import time
import pygame
import math
import random
import os

from Vf2d import *
from Rect import *
from Color import *
from Ball import *
from Paddle import *


SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000
PADDLE_WIDTH = SCREEN_WIDTH * 0.05
PADDLE_HEIGHT = SCREEN_HEIGHT * 0.2
BALL_WIDTH = SCREEN_WIDTH * 0.05
BALL_HEIGHT = SCREEN_WIDTH * 0.05

WORLD = Rect(0.0,0.0,SCREEN_WIDTH,SCREEN_HEIGHT,0.0,0.0,Color(0.0,0.0,0.0))
PLAYER_SPEED = 600.0

running: bool = True
elapsed_time: float = 0.0
last_time: float = 0.0

player1: Paddle = Paddle(0.0,0.0,PADDLE_WIDTH,PADDLE_HEIGHT,Color(1.0,0.0,0.0))
player2: Paddle = Paddle(0.0,0.0,PADDLE_WIDTH,PADDLE_HEIGHT,Color(0.0,0.0,1.0))
ball: Ball = Ball(0.0,0.0,40.0,Color(1.0,1.0,1.0))
screen = None

def get_input():
    global running
    global player1
    global player2
    
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player1.move(-PLAYER_SPEED)
    elif key[pygame.K_s]:
        player1.move(PLAYER_SPEED)
    else:
        player1.move(0.0)

    if key[pygame.K_UP]:
        player2.move(-PLAYER_SPEED)
    elif key[pygame.K_DOWN]:
        player2.move(PLAYER_SPEED)
    else:
        player2.move(0.0)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

def new_direction(max_out: float):
    a = random.random() * math.pi * 2.0
    if math.pi / 4.0 < a < math.pi / 2.0:
        a = math.pi / 4.0
    if math.pi / 2.0 < a < math.pi / 4.0 * 3.0:
        a = math.pi / 4.0 * 3.0
    if math.pi / 4.0 * 5.0 < a < math.pi / 2.0 * 3.0:
        a = math.pi / 4.0 * 5.0
    if math.pi / 2.0 * 3.0 < a < math.pi / 4.0 * 7.0:
        a = math.pi / 4.0 * 7.0
    v = Vf2d(math.cos(a), math.sin(a)) * max_out
    return v

def reset(r: int):
    global player1
    global player2
    global ball

    ball.p.x = (SCREEN_WIDTH - BALL_WIDTH) * 0.5
    ball.p.y = (SCREEN_HEIGHT - BALL_HEIGHT) * 0.5
    player1.p.x = 0
    player1.p.y = (SCREEN_HEIGHT - PADDLE_HEIGHT) * 0.5
    player2.p.x = SCREEN_WIDTH - PADDLE_WIDTH
    player2.p.y = (SCREEN_HEIGHT - PADDLE_HEIGHT) * 0.5
    ball.v = new_direction(300.0)

    if r==1:
        player2.points += 1
    elif r==2:
        player1.points += 1

def collision_field():
    global ball

    r = ball.goal(WORLD.d)
    if r > 0:
        reset(r)


def setup():
    global elapsed_time
    global last_time

    reset(0)
    elapsed_time = 0.0
    last_time = time.time()

def update():
    global running
    global player1
    global player2

    get_input()
    
    player1.update(elapsed_time)
    player2.update(elapsed_time)
    ball.update(elapsed_time)

    player1.collision_border(WORLD)
    player2.collision_border(WORLD)
    ball.collision_border(WORLD)
    player1.collision(ball)
    player2.collision(ball)
    collision_field()

    screen.fill(WORLD.c.get())
    pygame.draw.rect(screen,player1.c.get(),(player1.p.x,player1.p.y,player1.d.x,player1.d.y))
    pygame.draw.rect(screen,player2.c.get(),(player2.p.x,player2.p.y,player2.d.x,player2.d.y))
    pygame.draw.circle(screen,ball.c.get(),(ball.p.x + ball.d.x * 0.5,ball.p.y + ball.d.y * 0.5),ball.d.x * 0.5,0)

    string_render = pygame.font.Font(None, 200).render(str(player1.points) + " : " + str(player2.points), True, (255, 255, 255))
    rect = string_render.get_rect()
    rect.x = SCREEN_WIDTH * 0.5 - rect.w * 0.5
    rect.y = SCREEN_HEIGHT * 0.01
    screen.blit(string_render, rect)

def main():
    global running
    global screen
    global elapsed_time
    global last_time
    global player1
    global player2
    
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    title = "Pong by Codeleaded"
    
    setup()

    while running:
        elapsed_time = time.time() - last_time
        last_time = time.time()
        pygame.display.set_caption(title+"\t Fps: "+str(int(1.0 / elapsed_time * 10.0) / 10))

        update()

        pygame.display.flip()
        pygame.time.Clock().tick(120)
        time.sleep(0.005)

    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()