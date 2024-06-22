import pygame

class GameMaster:
  def __init__(self):
    self.score = 0
    self.b_started = False
    self.b_game_over = False

  def start(self):
    if self.b_game_over:
      self.retry()
      return
    self.b_started = True

  def retry(self):
    self.b_started = True
    self.b_game_over = False
    self.score = 0

  def draw(self, screen):

    if not self.b_started:
      font = pygame.font.Font(None, 50)
      text = font.render('Press Space Key', True, (255, 255, 255))
      screen.blit(text, (150, 300))

    if self.b_game_over:
      # ゲームオーバーの表示
      font = pygame.font.Font(None, 50)
      text = font.render('Game Over', True, (255, 255, 255))
      screen.blit(text, (180, 300))

      # スコアの表示
      font = pygame.font.Font(None, 50)
      text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
      screen.blit(text, (200, 400))

      # リトライの表示
      font = pygame.font.Font(None, 50)
      text = font.render('Press Space Key', True, (255, 255, 255))
      screen.blit(text, (150, 500))
      

  def is_game_over(self) -> bool:
    return self.b_game_over
  
  def is_started(self) -> bool: 
    return self.b_started

  def add_score(self, score):
    self.score += score
  
  def game_over(self):
    self.b_game_over = True