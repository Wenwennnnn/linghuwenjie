import pygame

class Item():
  # Constructor
  def __init__(self, filename, screenSize, speed): # self is like this
    # self is always the first argument in a method (function)
    self.picture = pygame.image.load(filename)
    self.rect = self.picture.get_rect()
    self.width = screenSize[0]
    self.height = screenSize[1]
    self.speed = speed

  def move(self):
    self.rect = self.rect.move(self.speed)
    if self.rect.left < 0 or self.rect.right > self.width:
      self.speed[0] = -self.speed[0]
    if self.rect.top < 0 or self.rect.bottom > self.height:
      self.speed[1] = -self.speed[1]

  def moveAmount(self, amount):
    self.rect = self.rect.move(amount)

  def moveToPosition(self, position):  
    self.rect.x = position[0] - self.rect.w/2
    self.rect.y = position[1] - self.rect.h/2

  def blit(self, screen):
    screen.blit(self.picture, self.rect)