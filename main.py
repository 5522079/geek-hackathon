import pygame
import player

# 定数
WITH = 600
HEIGHT = 800

class Game:
  # ゲームの初期化
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WITH, HEIGHT))
    self.running = True

  def run(self):
    player1 = player.Player(100, 100)
    fps = pygame.time.Clock()

    while self.running:
      #メイン処理
      self.screen.fill((0, 0, 0))

      player1.gravity()

      # イベント処理
      for event in pygame.event.get():
        # 終了イベント
        if event.type == pygame.QUIT:
          self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
          player1.jump()

      # 描画処理
      player1.draw(self.screen)

      # 画面更新
      pygame.display.update()
      fps.tick(45)

    # 終了処理
    pygame.quit()

if __name__ == '__main__':
  game = Game()
  game.run()