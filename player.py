import pygame

SCALE = 1.5

class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y

    # 画像の読み込み
    self.midimg = pygame.image.load('sprites/yellowbird-midflap.png')
    self.midimg = pygame.transform.rotozoom(self.midimg, 0, SCALE)
    self.downimg = pygame.image.load('sprites/yellowbird-downflap.png')
    self.downimg = pygame.transform.rotozoom(self.downimg, 0, SCALE)
    self.upimg = pygame.image.load('sprites/yellowbird-upflap.png')
    self.upimg = pygame.transform.rotozoom(self.upimg, 0, SCALE)

  def draw(self, screen):
    screen.blit(self.midimg, (self.x, self.y))

  def gravity(self):
    self.y += 8