# Respond to Collision is finished
# create a driver file
# init pygame
import random
import sys
from myImage import *

import pygame

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
background = (100, 100, 150)

ballSpeed = [-1, -1]
ball2Speed = [1, 1]
ball = MyImage("intro_ball.gif", size, ballSpeed)
ball2 = MyImage("intro_ball.gif", size, ball2Speed)
ball.setLocation(size)

speedList = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #     Add keyboard event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ball.rect.left - 60 >= 0:
                ball.moveImageAmount((-60, 0))
            if event.key == pygame.K_RIGHT and ball.rect.right + 60 <= size[0]:
                ball.moveImageAmount((60, 0))
            if event.key == pygame.K_UP and ball.rect.top - 60 >= 0:
                ball.moveImageAmount((0, -60))
            if event.key == pygame.K_DOWN and ball.rect.bottom + 60 <= size[1]:
                ball.moveImageAmount((0, 60))

        # Handle the mouse drag ball event
        # If the left mouse button is pressed
        if pygame.mouse.get_pressed()[0] == 1:
            mouse_position = pygame.mouse.get_pos()
            # Determine whether the mouse click position is in the ball image
            if (ball.rect.collidepoint(mouse_position)):
                isIn = True
        else:
            isIn = False

        if isIn:
            moveAmount = list(pygame.mouse.get_rel())
            ball.moveImageToPosition(mouse_position)
    # Determine if two balls collide
    if ball.rect.colliderect(ball2.rect):
        ball.speed = speedList[random.randint(0, 7)]
        ball2.speed = speedList[random.randint(0, 7)]
    clock = pygame.time.Clock()
    screen.fill(background)
    ball.blitImage(screen)
    ball2.blitImage(screen)
    ball.moveImage()
    ball2.moveImage()
    pygame.display.flip()
    clock.tick(300)
