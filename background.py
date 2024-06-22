import pygame
from settings import WIDTH, HEIGHT

class Ground:
    """地面のクラス"""
    def __init__(self):
        self.image = pygame.image.load('sprites/base.png').convert()  # 地面の画像を読み込む
        self.rect = self.image.get_rect(bottomleft=(0, HEIGHT))  # 画像の位置を設定

    def draw(self, screen):
        """地面を描画する"""
        screen.blit(self.image, self.rect.topleft)  # 画像を描画

class Background:
    """背景を管理するクラス"""
    def __init__(self):
        self.day_image = pygame.image.load('sprites/background-day.png').convert()  # 昼の背景画像を読み込む
        self.night_image = pygame.image.load('sprites/background-night.png').convert()  # 夜の背景画像を読み込む
        self.current_image = self.day_image  # 最初は昼の背景を表示
        self.ground = Ground()  # 地面を作成
        self.change_interval = 30000  # 30秒ごとに背景を切り替え
        self.last_change_time = pygame.time.get_ticks()  # 最後に背景を切り替えた時間を記録

    def update(self):
        """背景の更新"""
        # 一定時間ごとに背景を切り替える
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time > self.change_interval:
            self.current_image = self.night_image if self.current_image == self.day_image else self.day_image
            self.last_change_time = current_time

    def draw(self, screen):
        """背景を描画する"""
        screen.blit(self.current_image, (0, 0))  # 現在の背景画像を描画
        self.ground.draw(screen)  # 地面を描画
