import pygame
from random import randint, random
from settings import SCROLL_SPEED, PIPE_GAP_X, PIPE_GAP_Y

# 土管用アイテムも混じっているので気を付けてください
class Item:
  def __init__(self,  x: int = 600, y: int = 300, pipe_item: bool = False,):
    if not pipe_item:
      self.x = 600 + (PIPE_GAP_X // 2)
      self.y = randint(300, 600)
    else:
      self.x = x
      self.y = y
    self.b_hide = False
    self.rare = not pipe_item #パイプ用のアイテムではない場合はレア

    if not pipe_item:
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
    if self.rect.right < -0 and self.rare:
      self.rect.x = 600 + randint(100, 600)
      self.rect.y = randint(100, 600)
      self.x = self.rect.x
      self.y = self.rect.y
      self.b_hide = False

  def get_point(self):
    return 1 if not self.rare else 5

  def hide(self):
    self.b_hide = True

  def is_hide(self):
    return self.b_hide

  # ドカンとめり込んで出現するのを防ぐ
  def collide_rect(self, pipe: pygame.Rect):
    return self.rect.colliderect(pipe)

  def random_hide(self):
    if randint(1,10) < 7:
      self.b_hide = True

  def reset(self):
    self.b_hide = False

  def set_rect_left_top(self, x, y):
    self.rect.left = x
    self.rect.top = y
    self.x = x
    self.y = y

  def draw(self, screen):
    if not self.b_hide:
      screen.blit(self.img, self.rect)