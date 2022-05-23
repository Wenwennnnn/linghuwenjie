# Move item with keys is finished
# create a driver file
# init pygame
import sys
from myImage import *

import pygame

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
background = (100, 100, 150)

ballSpeed = [1, 1]
ball = MyImage("intro_ball.gif", size, ballSpeed)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #     Add keyboard event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ball.rect.left-60 >= 0:
                ball.moveImageAmount((-60, 0))
            if event.key == pygame.K_RIGHT and ball.rect.right+60 <= size[0]:
                ball.moveImageAmount((60, 0))
            if event.key == pygame.K_UP and ball.rect.top-60 >= 0:
                ball.moveImageAmount((0, -60))
            if event.key == pygame.K_DOWN and ball.rect.bottom+60 <= size[1]:
                ball.moveImageAmount((0, 60))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and ball.rect.left-60 >= 0:
                ball.moveImageAmount((-60, 0))
            if event.key == pygame.K_d and ball.rect.right+60 <= size[0]:
                ball.moveImageAmount((60, 0))
            if event.key == pygame.K_w and ball.rect.top-60 >= 0:
                ball.moveImageAmount((0, -60))
            if event.key == pygame.K_s and ball.rect.bottom+60 <= size[1]:
                ball.moveImageAmount((0, 60))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k and ball.rect.left-60 >= 0:
                ball.moveImageAmount((-60, 0))
            if event.key == pygame.K_l and ball.rect.right+60 <= size[0]:
                ball.moveImageAmount((60, 0))
            if event.key == pygame.K_h and ball.rect.top-60 >= 0:
                ball.moveImageAmount((0, -60))
            if event.key == pygame.K_j and ball.rect.bottom+60 <= size[1]:
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
    clock = pygame.time.Clock()
    screen.fill(background)
    ball.blitImage(screen)
    ball.moveImage()
    pygame.display.flip()
    clock.tick(300)
