import pygame

class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.img = pygame.image.load('sprites/yellowbird-midflap.png')

  def draw(self, screen):
    screen.blit(self.img, (self.x, self.y))

  def gravity(self):
    self.y += 1