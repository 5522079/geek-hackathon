import pygame

def render_text_with_outline(font, text, text_color, outline_color):
    base_surface = font.render(text, True, text_color)
    width, height = base_surface.get_size()
    
    # アウトラインの太さ
    outline_width = 2
    
    # 新しいサーフェスを作成（元のテキストより大きくする）
    outline_surface = pygame.Surface((width + 2 * outline_width, height + 2 * outline_width), pygame.SRCALPHA)
    
    # アウトラインを描画
    for x in range(-outline_width, outline_width + 1):
        for y in range(-outline_width, outline_width + 1):
            if x != 0 or y != 0:  # 中心以外の位置に黒いテキストを描画
                outline_surface.blit(font.render(text, True, outline_color), (x + outline_width, y + outline_width))
    
    # 中心に元のテキストを描画
    outline_surface.blit(base_surface, (outline_width, outline_width))
    
    return outline_surface

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
      text = 'Press Space Key'
      text_surface = render_text_with_outline(font, text, (255, 255, 255), (0, 0, 0))
      screen.blit(text_surface, (150, 300))

    if self.b_game_over:
      # ゲームオーバーの表示
      font = pygame.font.Font(None, 50)
      text = 'Game Over'
      text_surface = render_text_with_outline(font, text, (250, 69, 0), (0, 0, 0))
      screen.blit(text_surface, (180, 300))


      # スコアの表示
      font = pygame.font.Font(None, 50)
      text = 'Score: ' + str(self.score)
      text_surface = render_text_with_outline(font, text, (255, 255, 255), (0, 0, 0))
      screen.blit(text_surface, (200, 400))

      # リトライの表示
      font = pygame.font.Font(None, 50)
      text = 'Press Space Key'
      text_surface = render_text_with_outline(font, text, (255, 255, 255), (0, 0, 0))
      screen.blit(text_surface, (150, 500))



    # スコアの表示
    font = pygame.font.Font(None, 50)
    text = 'Score: ' + str(self.score)
    text_surface = render_text_with_outline(font, text, (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface, (10, 30))
      

  def is_game_over(self) -> bool:
    return self.b_game_over
  
  def is_started(self) -> bool: 
    return self.b_started

  def add_score(self, score):
    self.score += score
  
  def game_over(self):
    self.b_game_over = True