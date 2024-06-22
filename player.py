import pygame
from obstacle import Obstacle
from background import Ground
from item import Item

SCALE = 0.04
MOVE_SPEED = 7
GRAVITY = 0.5

class PlayerBird:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.velocity = 0
    self.angle = 0
    self.flayImageCount = 0
    self.flameCount = 0

    # 画像の読み込み
    self.cat1 = pygame.image.load('sprites/pink_cat_1.png').convert_alpha()
    self.cat1 = pygame.transform.rotozoom(self.cat1, 0, SCALE)
    self.cat2 = pygame.image.load('sprites/pink_cat_2.png').convert_alpha()
    self.cat2 = pygame.transform.rotozoom(self.cat2, 0, SCALE)

    self.rect = self.cat1.get_rect(topleft=(self.x, self.y))


  def jump(self):
    self.velocity = -10

  def update(self):
    self.velocity = min(self.velocity + GRAVITY, 10)
    self.rect.y += self.velocity

    if self.velocity < 0:
      self.angle = min(self.angle + 10, 45)
    else:
      self.angle = max(self.angle - 4, -70)

    if self.y < 0:
      self.y = 0
      self.velocity = 0
    if self.y > 800:
      self.y = 800
      self.velocity = 0

    self.x = self.rect.x
    self.y = self.rect.y

  def collides_with_pip(self, pipe: Obstacle):
    return ((not pipe.hide_top and self.rect.colliderect(pipe.top_rect))
              or self.rect.colliderect(pipe.bottom_rect) 
            or (not pipe.hide_top2 and self.rect.colliderect(pipe.top2_rect))
              or self.rect.colliderect(pipe.bottom2_rect))
  
  def collides_with_ground(self, ground: Ground):
    return self.rect.colliderect(ground.rect)
  
  def collides_with_item(self, item: Item):
    return self.rect.colliderect(item.rect)

  def draw(self, screen):
    if self.flameCount < 0:
      self.flameCount = 5
      self.flayImageCount -= 1
      if self.flayImageCount < 0:
        self.flayImageCount = 2
    else:
      self.flameCount -= 1

    draw_cat_img = self.cat1
    if self.flayImageCount == 1:
      draw_cat_img = self.cat2

    # デバッグ用の当たり判定描画
    # pygame.draw.rect(screen, (255, 0, 0), self.rect)

    draw_bird = pygame.transform.rotate(draw_cat_img, self.angle)

    screen.blit(draw_bird, (self.x, self.y))