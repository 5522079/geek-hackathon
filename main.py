import pygame
import player

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    self.running = True

  def run(self):
    player1 = player.Player(100, 100)

    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      self.screen.fill((0, 0, 0))
      player1.gravity()
      player1.draw(self.screen)
      pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
  game = Game()
  game.run()