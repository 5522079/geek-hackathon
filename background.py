import pygame
from file_loader import resource_path
from settings import SCROLL_SPEED

# 定数
WIDTH = 600
HEIGHT = 800

class Ground:
    """地面のクラス"""
    def __init__(self):
        self.image = pygame.image.load(resource_path('sprites/base.png')).convert()  # 地面の画像を読み込む
        self.image = pygame.transform.scale(self.image, (WIDTH, 100))  # 地面の画像をウィンドウ幅にスケーリング
        self.rect = self.image.get_rect(bottomleft=(0, HEIGHT))  # 画像の位置を設定
        self.rect2 = self.image.get_rect(bottomleft=(WIDTH, HEIGHT))  # 画像の位置を設定 (2枚目)

    def update(self):
        """地面の更新"""
        self.rect.move_ip(SCROLL_SPEED, 0)
        self.rect2.move_ip(SCROLL_SPEED, 0)

        # 1枚目の地面が完全に画面外に出たら、2枚目の地面の右側に配置
        if self.rect.right <= 0:
            self.rect.left = self.rect2.right

        # 2枚目の地面が完全に画面外に出たら、1枚目の地面の右側に配置
        if self.rect2.right <= 0:
            self.rect2.left = self.rect.right

    def draw(self, screen):
        """地面を描画する"""
        screen.blit(self.image, self.rect.topleft)  # 画像を描画
        screen.blit(self.image, self.rect2.topleft)

class Background:
    """背景を管理するクラス"""
    def __init__(self):
        self.day_image = pygame.image.load(resource_path('sprites/background_day.png')).convert()  # 昼の背景画像を読み込む
        self.day_image = pygame.transform.scale(self.day_image, (WIDTH, HEIGHT))  # 昼の背景画像をウィンドウサイズにスケーリング
        self.night_image = pygame.image.load(resource_path('sprites/background_night.png')).convert()  # 夜の背景画像を読み込む
        self.night_image = pygame.transform.scale(self.night_image, (WIDTH, HEIGHT))  # 夜の背景画像をウィンドウサイズにスケーリング
        self.current_image = self.day_image  # 最初は昼の背景を表示
        self.change_interval = 6000  # 30秒ごとに背景を切り替え
        self.last_change_time = pygame.time.get_ticks()  # 最後に背景を切り替えた時間を記録

    def update(self):
        """背景の更新"""
        # 一定時間ごとに背景を切り替える
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time > self.change_interval:
            self.current_image = self.night_image if self.current_image == self.day_image else self.day_image
            self.last_change_time = current_time
    
    def reset(self):
        """背景を昼にリセット"""
        self.current_image = self.day_image
        self.last_change_time = pygame.time.get_ticks()

    def draw(self, screen):
        """背景を描画する"""
        screen.blit(self.current_image, (0, 0))  # 現在の背景画像を描画
