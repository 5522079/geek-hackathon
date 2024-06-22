import pygame
from player import PlayerBird
from obstacle import Obstacle
from background import Background, Ground
from game_master import GameMaster

# 定数
WITH = 600
HEIGHT = 800

class Game:
  # ゲームの初期化
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WITH, HEIGHT))
    self.running = True

  # ゲームのメイン処理
  # メインループ
  # リトライなし -> False
  def main_loop(self) -> bool:
    gameMaster = GameMaster()

    playerBird = PlayerBird(100, 250)
    pipe = Obstacle(600, -100)
    background = Background()
    ground = Ground()
    fps = pygame.time.Clock()

    retry = False

    while self.running:
      #メイン処理
      self.screen.fill((0, 0, 0))

      # スタート後の処理
      # スタート前で処理させないためにif文で囲む
      if gameMaster.is_started() and not gameMaster.is_game_over():
        playerBird.update()
        pipe.update()
        background.update()
        ground.update()
      

      # ゲームオーバー判定
      if playerBird.collides_with_pip(pipe) or playerBird.collides_with_ground(ground):
        gameMaster.game_over()

      # イベント処理
      for event in pygame.event.get():
        # 終了イベント
        if event.type == pygame.QUIT:
          self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            playerBird.jump()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not gameMaster.is_started():
              gameMaster.start()
            elif gameMaster.is_game_over():
              gameMaster.retry()
              self.running = False
              retry = True

      # 描画処理
      # 表示順番重要なので変えないように注意
      background.draw(self.screen)
      playerBird.draw(self.screen)
      pipe.draw(self.screen)
      ground.draw(self.screen)
      gameMaster.draw(self.screen)

      # 画面更新
      pygame.display.update()
      fps.tick(45)

    return retry
  
  # ゲームの実行
  def run(self):
    while True:
      retry = self.main_loop()
      if not retry:
        break
      self.running = True

    pygame.quit()

if __name__ == '__main__':
  game = Game()
  game.run()