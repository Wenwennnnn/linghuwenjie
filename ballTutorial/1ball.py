import sys, pygame
from item import *
# simple pygame tutorial is finished
pygame.init()

size = width, height = 1000, 600
faceSpeed = [1, 1]
ballSpeed = [1, 1]
ball2Speed = [2, 2]
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 120)
backgroundColor = (100, 100, 150)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", size, ballSpeed)
ball2 = Item("intro_ball.gif", size, ball2Speed)
face = Item("smileyTiny.png", size, faceSpeed)

testSurface = pygame.Surface((50,50))
testRect = pygame.Rect(0, 0, 50, 50)
test = pygame.draw.rect(testSurface, blue, testRect)

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  pygame.time.wait(2)
  ball.move()
  ball2.move()
  face.move()
  

  screen.fill(backgroundColor)
  ball.blit(screen)
  ball2.blit(screen)
  face.blit(screen)
  screen.blit(testSurface, testRect)
  pygame.display.flip()


