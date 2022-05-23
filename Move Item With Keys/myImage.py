import pygame


class MyImage:
    # my image Constructor
    def __init__(self, path, screenSize, speed):
        self.picture = pygame.image.load(path)
        self.rect = self.picture.get_rect()
        self.width = screenSize[0]
        self.height = screenSize[1]
        self.speed = speed

    # Moving in the direction of velocity
    def moveImage(self):
        self.rect = self.rect.move(self.speed)
        # If it hits the boundary, it reverses velocity
        if self.rect.left < 0 or self.rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

    # Move the image a certain amount along the amount
    def moveImageAmount(self, amount):
        self.rect = self.rect.move(amount)

    # Move the center of the image to position
    def moveImageToPosition(self, position):
        self.rect.x = position[0] - self.rect.w / 2
        self.rect.y = position[1] - self.rect.h / 2

    # Binds the image to the screen window passed in
    def blitImage(self, screen):
        screen.blit(self.picture, self.rect)