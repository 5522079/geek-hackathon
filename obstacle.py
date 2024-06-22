import pygame
from random import randint

class Obstacle:
  def __init__(self, x, y):
    # どかんが流れる速度
    self.scroll_speed = -10
    # 上のどかんと下のどかんの間
    gap = 200

    self.top_x = x
    self.top_y = y
    self.top = pygame.image.load("sprites/pipe-green.png").convert_alpha()
    self.top = pygame.transform.rotate(self.top, 180)
    self.top_rect = self.top.get_rect(topleft=(self.top_x, self.top_y))

    self.bottom_x = x
    self.bottom_y = self.top_y + self.top.get_height() + gap
    self.bottom = pygame.image.load("sprites/pipe-green.png").convert_alpha()
    self.bottom_rect = self.bottom.get_rect(topleft=(self.bottom_x, self.bottom_y))

  def draw(self, screen):
    screen.blit(self.top, self.top_rect.topleft)
    screen.blit(self.bottom, self.bottom_rect.topleft)

  def update(self):
    self.top_rect.move_ip(self.scroll_speed, 0)
    self.bottom_rect.move_ip(self.scroll_speed, 0)
    self.top_x = self.top_rect.x
    self.bottom_x = self.bottom_rect.x

    if self.top_rect.right < 0 and self.bottom_rect.right < 0:
        self.top_rect.left = 600
        self.top_rect.top = randint(-100, 0)

        self.bottom_rect.left = 600