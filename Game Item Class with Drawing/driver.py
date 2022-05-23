# Game Item class with Drawing is finished
# create a driver file
import sys
from mydraw import *

import pygame

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
background = (255, 255, 255)

ballSpeed = [1, 1]
squareSpeed = [1, 1]
square = MyDraw.draw(MyDraw.Kind.SQUARE, size, squareSpeed)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #     Add keyboard event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and square.Rect.left - 60 >= 0:
                square.moveDrawAmount((-60, 0))
            if event.key == pygame.K_RIGHT and square.Rect.right + 60 <= size[0]:
                square.moveDrawAmount((60, 0))
            if event.key == pygame.K_UP and square.Rect.top - 60 >= 0:
                square.moveDrawAmount((0, -60))
            if event.key == pygame.K_DOWN and square.Rect.bottom + 60 <= size[1]:
                square.moveDrawAmount((0, 60))

        # Handle the mouse drag ball event
        # If the left mouse button is pressed
        if pygame.mouse.get_pressed()[0] == 1:
            mouse_position = pygame.mouse.get_pos()
            # Determine whether the mouse click position is in the ball image
            if (square.Rect.collidepoint(mouse_position)):
                isIn = True
        else:
            isIn = False

        if isIn:
            moveAmount = list(pygame.mouse.get_rel())
            square.moveDrawToPosition(mouse_position)


    clock=pygame.time.Clock()
    screen.fill(background)
    screen.fill((100,150,150))
    square.blitDraw(screen)
    square.moveDraw()
    pygame.display.flip()
    clock.tick(300)
