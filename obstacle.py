import pygame
from random import randint, random

# どかんのサイズ調整
(width, height) = (88, 542)

gap_x = 350  # 左のどかんと右のどかんの幅
gap_y = 150  # 上のどかんと下のどかんの幅

# どかんが流れる速度
scroll_speed = -8

class Obstacle:
    def __init__(self, x, y):
        # どかん1
        self.top_x = x
        self.top_y = y
        self.top = pygame.image.load("sprites/pipe-green.png").convert_alpha()
        self.top = pygame.transform.rotate(self.top, 180)
        self.top = pygame.transform.scale(self.top, (width, height))
        self.top_rect = self.top.get_rect(topleft=(self.top_x, self.top_y))

        self.bottom_x = x
        self.bottom_y = self.top_y + self.top.get_height() + gap_y
        self.bottom = pygame.image.load("sprites/pipe-green.png").convert_alpha()
        self.bottom = pygame.transform.scale(self.bottom, (width, height))
        self.bottom_rect = self.bottom.get_rect(topleft=(self.bottom_x, self.bottom_y))

        # どかん2
        self.top_x2 = x + gap_x
        self.top_y2 = y - 50
        self.top2 = pygame.image.load("sprites/pipe-green.png").convert_alpha()
        self.top2 = pygame.transform.rotate(self.top2, 180)
        self.top2 = pygame.transform.scale(self.top2, (width, height))
        self.top2_rect = self.top2.get_rect(topleft=(self.top_x2, self.top_y2))
        
        self.bottom_x2 = x + gap_x
        self.bottom_y2 = self.top_y2 + self.top2.get_height() + gap_y
        self.bottom2 = pygame.image.load("sprites/pipe-green.png").convert_alpha()
        self.bottom2 = pygame.transform.scale(self.bottom2, (width, height))
        self.bottom2_rect = self.bottom2.get_rect(topleft=(self.bottom_x2, self.bottom_y2))

        # たまにうえのどかんを消す
        self.hide_top = randint(1, 10) <= 3
        self.hide_top2 = randint(1, 10) <= 3

    def draw(self, screen):
        if not self.hide_top:
            screen.blit(self.top, self.top_rect.topleft)
        screen.blit(self.bottom, self.bottom_rect.topleft)

        if not self.hide_top2:
            screen.blit(self.top2, self.top2_rect.topleft)
        screen.blit(self.bottom2, self.bottom2_rect.topleft)

    def update(self):
        self.top_rect.move_ip(scroll_speed, 0)
        self.bottom_rect.move_ip(scroll_speed, 0)
        self.top_x = self.top_rect.x
        self.bottom_x = self.bottom_rect.x

        self.top2_rect.move_ip(scroll_speed, 0)
        self.bottom2_rect.move_ip(scroll_speed, 0)
        self.top_x2 = self.top2_rect.x
        self.bottom_x2 = self.bottom2_rect.x

        if self.top_rect.right < 0:
            self.top_rect.left = 600
            self.top_rect.top = randint(-400, -150)
            self.bottom_rect.left = self.top_rect.left
            self.bottom_rect.top = self.top_rect.top + self.top.get_height() + gap_y

            self.hide_top = randint(1, 10) <= 3

        if self.top2_rect.right < 0:
            self.top2_rect.left = 600
            self.top2_rect.top = randint(-200, 0)
            self.bottom2_rect.left = self.top2_rect.left
            self.bottom2_rect.top = self.top2_rect.top + self.top2.get_height() + gap_y

            self.hide_top2 = randint(1, 10) <= 3


