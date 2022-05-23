import pygame
from myImage import *

kinds = ""


class MyDraw(MyImage):

    # my draw Constructor
    def __init__(self, path, screenSize, speed):
        print()

    # Second constructor
    @classmethod
    def draw(cls, kind, screenSize, speed):
        cls.kind = kind
        cls.draws = None
        cls.Surface = pygame.Surface((50, 50))
        cls.Rect = pygame.Rect(0, 0, 50, 50)
        cls.width = screenSize[0]
        cls.height = screenSize[1]
        cls.speed = speed
        return cls(kind, screenSize, speed)

    # Binds the image to the screen window passed in
    def blitDraw(self, screen):
        if self.kind == "ball":
            self.draws = pygame.draw.circle(self.Surface, (100, 100, 100), (self.Rect.w,self.Rect.h), 750, 100)
        if self.kind == "square":
            self.draws = pygame.draw.rect(self.Surface, (100, 100, 100), self.Rect, 10)
        screen.blit(self.Surface, self.Rect)

    # Moving in the direction of velocity
    def moveDraw(self):
        self.Rect = self.Rect.move(self.speed)
        # If it hits the boundary, it reverses velocity
        if self.Rect.left < 0 or self.Rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.Rect.top < 0 or self.Rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

    # Move the image a certain amount along the amount
    def moveDrawAmount(self, amount):
        self.Rect = self.Rect.move(amount)

     # Move the center of the image to position
    def moveDrawToPosition(self, position):
        self.Rect.x = position[0] - self.Rect.w / 2
        self.Rect.y = position[1] - self.Rect.h / 2

    class Kind:
        BALL = "ball"
        SQUARE = "square"
