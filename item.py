import pygame

class Item:
  def __init__(self, x, y):
    self.x = x
    self.y = y

    self.img = pygame.image.load('sprites/fish.png').convert()  
    self.rect = self.midimg.get_rect(topleft=(self.x, self.y))

  def draw(self, screen):
    screen.blit(self.img, self.rect)