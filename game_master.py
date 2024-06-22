import pygame

class GameMaster:
  def __init__(self):
    self.score = 0
    self.b_started = False
    self.b_game_over = False

  def start(self):
    self.b_started = True

  def draw(self, screen):

    if not self.b_started:
      font = pygame.font.Font(None, 50)
      text = font.render('Press Space Key', True, (255, 255, 255))
      screen.blit(text, (150, 300))

  def is_game_over(self) -> bool:
    return self.b_game_over
  
  def is_started(self) -> bool: 
    return self.b_started

  def add_score(self, score):
    self.score += score
  
  def game_over(self):
    self.game_over = True