import pygame
from random import randint, random
from settings import SCROLL_SPEED, PIPE_GAP_X, PIPE_GAP_Y

class Item:
  def __init__(self, rare: bool = False):
    self.x = 600 + (PIPE_GAP_X // 2)
    self.y = randint(300, 600)
    self.b_hide = False
    self.rare = rare

    if self.rare:
      self.img = pygame.image.load('sprites/fish.png').convert()  
    else:
      self.img = pygame.image.load('sprites/fish.png').convert()  
    self.img = pygame.transform.scale(self.img, (50, 50))
    self.rect = self.img.get_rect(topleft=(self.x, self.y))

  def update(self):
    # アイテムを流す
    self.rect.move_ip(SCROLL_SPEED, 0)
    self.x = self.rect.x

    # アイテムリセット
    if self.rect.right < -0:
      self.rect.x = 600 + randint(100, 600)
      self.rect.y = randint(100, 600)
      self.x = self.rect.x
      self.y = self.rect.y
      self.b_hide = False

  def hide(self):
    self.b_hide = True

  def draw(self, screen):
    if not self.b_hide:
      screen.blit(self.img, self.rect)