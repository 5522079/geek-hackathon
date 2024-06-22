import pygame

SCALE = 1.5
MOVE_SPEED = 7

class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.jumpFlameCount = 0
    self.flayingStopCount = 0

    # 画像の読み込み
    self.midimg = pygame.image.load('sprites/yellowbird-midflap.png')
    self.midimg = pygame.transform.rotozoom(self.midimg, 0, SCALE)
    self.downimg = pygame.image.load('sprites/yellowbird-downflap.png')
    self.downimg = pygame.transform.rotozoom(self.downimg, 0, SCALE)
    self.upimg = pygame.image.load('sprites/yellowbird-upflap.png')
    self.upimg = pygame.transform.rotozoom(self.upimg, 0, SCALE)

  def draw(self, screen):
    screen.blit(self.midimg, (self.x, self.y))

  def jump(self):
    if self.jumpFlameCount <= 4:
      self.jumpFlameCount = 20

  def gravity(self):
    # 下まで行き過ぎないように
    if self.y > 800:
      self.y = 800

    # ジャンプと重力
    if self.jumpFlameCount > 0:
      # ジャンプ中
      self.y -= MOVE_SPEED 
      self.jumpFlameCount -= 1

      # ジャンプ終了後に少し止まる
      if self.jumpFlameCount == 0:
        self.flayingStopCount = 4


    elif self.flayingStopCount > 0:
      # ジャンプ終了後の停止中
      self.flayingStopCount -= 1
      
      # 重力
    else:
      self.y += MOVE_SPEED