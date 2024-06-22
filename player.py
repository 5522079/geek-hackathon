import pygame
from obstacle import Obstacle
from background import Ground
from item import Item

SCALE = 1.5
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
    self.midimg = pygame.image.load('sprites/yellowbird-midflap.png').convert_alpha()
    self.midimg = pygame.transform.rotozoom(self.midimg, 0, SCALE)
    self.downimg = pygame.image.load('sprites/yellowbird-downflap.png').convert_alpha()
    self.downimg = pygame.transform.rotozoom(self.downimg, 0, SCALE)
    self.upimg = pygame.image.load('sprites/yellowbird-upflap.png').convert_alpha()
    self.upimg = pygame.transform.rotozoom(self.upimg, 0, SCALE)

    self.rect = self.midimg.get_rect(topleft=(self.x, self.y))


  def jump(self):
    self.velocity = -10

  def update(self):
    self.velocity = min(self.velocity + GRAVITY, 10)
    self.rect.y += self.velocity

    if self.velocity < 0:
      self.angle = min(self.angle + 10, 45)
    else:
      self.angle = max(self.angle - 4, -90)

    if self.y < 0:
      self.y = 0
      self.velocity = 0
    if self.y > 800:
      self.y = 800
      self.velocity = 0

    self.x = self.rect.x
    self.y = self.rect.y

  def collides_with_pip(self, pipe: Obstacle):
    return self.rect.colliderect(pipe.top_rect) or self.rect.colliderect(pipe.bottom_rect)
  
  def collides_with_ground(self, ground: Ground):
    return self.rect.colliderect(ground.rect)
  
  def collides_with_fish(self, item: Item):
    return self.rect.colliderect(item.rect)

  def draw(self, screen):
    if self.flameCount < 0:
      self.flameCount = 5
      self.flayImageCount -= 1
      if self.flayImageCount < 0:
        self.flayImageCount = 3
    else:
      self.flameCount -= 1

    draw_bird_img = self.midimg
    if self.flayImageCount == 0:
      draw_bird_img = self.downimg
    elif self.flayImageCount == 2:
      draw_bird_img = self.upimg

    if self.angle < -45:
      draw_bird_img = self.midimg

    # デバッグ用の当たり判定描画
    # pygame.draw.rect(screen, (255, 0, 0), self.rect)

    draw_bird = pygame.transform.rotate(draw_bird_img, self.angle)

    screen.blit(draw_bird, (self.x, self.y))