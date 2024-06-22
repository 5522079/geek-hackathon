import pygame
from random import randint, random
from settings import SCROLL_SPEED
from item import Item

# どかんのサイズ調整
(width, height) = (88, 542)

gap_x = 350  # 左のどかんと右のどかんの幅
gap_y = 150  # 上のどかんと下のどかんの幅

# どかんが流れる速度
scroll_speed = SCROLL_SPEED

class Obstacle:
    def __init__(self, x, y):
        # どかん1
        self.top_x = x
        self.top_y = y
        self.top = pygame.image.load("sprites/sand.png").convert_alpha()
        self.top = pygame.transform.scale(self.top, (width, height))
        self.top_rect = self.top.get_rect(topleft=(self.top_x, self.top_y))

        # 土管1のアイテム
        self.item1 = Item(self.top_x + 15, self.top_y + self.top.get_height() + 50, True)
        self.item1.random_hide()

        self.bottom_x = x
        self.bottom_y = self.top_y + self.top.get_height() + gap_y
        self.bottom = pygame.image.load("sprites/cactus.png").convert_alpha()
        self.bottom = pygame.transform.scale(self.bottom, (width, height))
        self.bottom_rect = self.bottom.get_rect(topleft=(self.bottom_x, self.bottom_y))

        # どかん2
        self.top_x2 = x + gap_x
        self.top_y2 = y - 50
        self.top2 = pygame.image.load("sprites/sand.png").convert_alpha()
        self.top2 = pygame.transform.scale(self.top2, (width, height))
        self.top2_rect = self.top2.get_rect(topleft=(self.top_x2, self.top_y2))

        # 土管2のアイテム
        self.item2 = Item(self.top_x2 + 15, self.top_y2 + self.top2.get_height() + 50, True)
        self.item2.random_hide()
        
        self.bottom_x2 = x + gap_x
        self.bottom_y2 = self.top_y2 + self.top2.get_height() + gap_y
        self.bottom2 = pygame.image.load("sprites/cactus.png").convert_alpha()
        self.bottom2 = pygame.transform.scale(self.bottom2, (width, height))
        self.bottom2_rect = self.bottom2.get_rect(topleft=(self.bottom_x2, self.bottom_y2))

        # たまにうえのどかんを消す
        self.hide_top = randint(1, 10) <= 3
        self.hide_top2 = randint(1, 10) <= 3

    def draw(self, screen):
        if not self.hide_top:
            screen.blit(self.top, self.top_rect.topleft)
        screen.blit(self.bottom, self.bottom_rect.topleft)
        self.item1.draw(screen)

        if not self.hide_top2:
            screen.blit(self.top2, self.top2_rect.topleft)
        screen.blit(self.bottom2, self.bottom2_rect.topleft)
        self.item2.draw(screen)

    def update(self):
        self.top_rect.move_ip(scroll_speed, 0)
        self.bottom_rect.move_ip(scroll_speed, 0)
        self.top_x = self.top_rect.x
        self.bottom_x = self.bottom_rect.x
        self.item1.update()

        self.top2_rect.move_ip(scroll_speed, 0)
        self.bottom2_rect.move_ip(scroll_speed, 0)
        self.top_x2 = self.top2_rect.x
        self.bottom_x2 = self.bottom2_rect.x
        self.item2.update()

        if self.top_rect.right < 0:
            self.hide_top = randint(1, 10) <= 3

            self.top_rect.left = 600

            # 上が聞いているときは、高くする
            if self.hide_top:
                self.top_rect.top = randint(-400, -200)
            else:
                self.top_rect.top = randint(-300, -150)
            self.bottom_rect.left = self.top_rect.left
            self.bottom_rect.top = self.top_rect.top + self.top.get_height() + gap_y

            self.item1.set_rect_left_top(self.top_rect.left + 15, self.top_rect.top + self.top.get_height() + 50)
            self.item1.reset()
            self.item1.random_hide()

        if self.top2_rect.right < 0:
            self.hide_top2 = randint(1, 10) <= 3

            self.top2_rect.left = 600

            # 上が聞いているときは、高くする
            if self.hide_top2:
                self.top2_rect.top = randint(-350, -200)
            else:
                self.top2_rect.top = randint(-200, 0)

            self.bottom2_rect.left = self.top2_rect.left
            self.bottom2_rect.top = self.top2_rect.top + self.top2.get_height() + gap_y

            self.item2.set_rect_left_top(self.top2_rect.left + 15, self.top2_rect.top + self.top.get_height() + 50)
            self.item2.reset()
            self.item2.random_hide()


