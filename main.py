import pygame
import player
from background import Background  # 追加

# 定数
WIDTH = 600
HEIGHT = 800

class Game:
    # ゲームの初期化
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.background = Background()  # 追加: 背景の初期化

    def run(self):
        playerBird = player.PlayerBird(100, 100)
        fps = pygame.time.Clock()

        while self.running:
            # メイン処理
            self.background.update()  # 追加: 背景の更新
            self.screen.fill((0, 0, 0))

            playerBird.update()

            # イベント処理
            for event in pygame.event.get():
                # 終了イベント
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    playerBird.jump()

            # 描画処理
            self.background.draw(self.screen)  # 追加: 背景の描画
            playerBird.draw(self.screen)

            # 画面更新
            pygame.display.update()
            fps.tick(45)

        # 終了処理
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
