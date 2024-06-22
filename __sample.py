import random
import pygame
import math

# ゲームの設定
GAME_WIDTH = 800
GAME_HEIGHT = 600
FPS = 60

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (135, 206, 235)
GROUND_COLOR = (222, 184, 135)

class GameObject:
    """すべてのゲームオブジェクトの基底クラス"""
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        """オブジェクトを描画する（サブクラスでオーバーライドする）"""
        pass

class Bird(GameObject):
    """プレイヤーが操作する鳥のクラス"""
    def __init__(self, x, y):
        super().__init__(x, y, 30, 30)
        self.velocity = 0
        self.gravity = 0.5
        self.angle = 0
        self.flap_speed = -10
        self.max_velocity = 10

    def jump(self):
        """鳥をジャンプさせる"""
        self.velocity = self.flap_speed
        self.angle = 45

    def update(self):
        """鳥の位置を更新する"""
        self.velocity = min(self.velocity + self.gravity, self.max_velocity)
        self.rect.y += self.velocity

        # 角度の更新
        if self.velocity < 0:
            self.angle = min(self.angle + 3, 45)
        else:
            self.angle = max(self.angle - 3, -45)

        # 画面外に出ないように制限
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom >= GAME_HEIGHT - Ground.HEIGHT:
            self.rect.bottom = GAME_HEIGHT - Ground.HEIGHT
            self.velocity = 0

    def draw(self, screen):
        """鳥を描画する"""
        bird_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.ellipse(bird_surface, RED, (0, 0, 30, 30))
        pygame.draw.ellipse(bird_surface, (255, 200, 0), (20, 10, 10, 10))  # 目
        rotated_bird = pygame.transform.rotate(bird_surface, self.angle)
        screen.blit(rotated_bird, self.rect.topleft)

class Pipe(GameObject):
    """パイプ障害物のクラス"""
    WIDTH = 80
    GAP = 200

    def __init__(self, x):
        self.top_height = random.randint(50, GAME_HEIGHT - self.GAP - Ground.HEIGHT - 50)
        super().__init__(x, 0, self.WIDTH, self.top_height)
        self.bottom_rect = pygame.Rect(x, self.top_height + self.GAP, self.WIDTH, GAME_HEIGHT - self.top_height - self.GAP - Ground.HEIGHT)
        self.passed = False

    def update(self):
        """パイプを左に移動させる"""
        self.rect.x -= 2
        self.bottom_rect.x -= 2

    def draw(self, screen):
        """上下のパイプを描画する"""
        pygame.draw.rect(screen, GREEN, self.rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)
        # パイプの装飾
        pygame.draw.rect(screen, (0, 100, 0), (self.rect.x, self.rect.bottom - 30, self.WIDTH, 30))
        pygame.draw.rect(screen, (0, 100, 0), (self.bottom_rect.x, self.bottom_rect.top, self.WIDTH, 30))

    def is_off_screen(self):
        """パイプが画面外に出たかどうかを判定"""
        return self.rect.right < 0

class Cloud(GameObject):
    """背景の雲を表すクラス"""
    def __init__(self):
        width = random.randint(50, 150)
        height = random.randint(30, 80)
        x = GAME_WIDTH
        y = random.randint(0, GAME_HEIGHT // 2)
        super().__init__(x, y, width, height)
        self.speed = random.uniform(0.5, 1.5)

    def update(self):
        """雲を左に移動させる"""
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = GAME_WIDTH
            self.rect.y = random.randint(0, GAME_HEIGHT // 2)

    def draw(self, screen):
        """雲を描画する"""
        pygame.draw.ellipse(screen, WHITE, self.rect)

class Ground(GameObject):
    """地面のクラス"""
    HEIGHT = 100

    def __init__(self):
        super().__init__(0, GAME_HEIGHT - self.HEIGHT, GAME_WIDTH, self.HEIGHT)

    def draw(self, screen):
        """地面を描画する"""
        pygame.draw.rect(screen, GROUND_COLOR, self.rect)
        pygame.draw.line(screen, (0, 0, 0), (0, self.rect.top), (GAME_WIDTH, self.rect.top), 2)

class ScoreBoard:
    """スコアボードのクラス"""
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self, score):
        """スコアを更新する"""
        self.score = score
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self, screen):
        """スコアを描画する"""
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 50))

class Game:
    """ゲーム全体を管理するクラス"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Advanced Flappy Bird Style Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.bird = Bird(50, GAME_HEIGHT // 2)
        self.pipes = []
        self.clouds = [Cloud() for _ in range(5)]
        self.ground = Ground()
        self.score_board = ScoreBoard()
        self.game_over = False

    def handle_events(self):
        """イベント処理を行う"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.bird.jump()
                elif event.key == pygame.K_r and self.game_over:
                    self.__init__()  # ゲームをリセット
        return True

    def update(self):
        """ゲーム状態を更新する"""
        if not self.game_over:
            self.bird.update()

            # 雲の更新
            for cloud in self.clouds:
                cloud.update()

            # 新しいパイプの生成
            if len(self.pipes) == 0 or self.pipes[-1].rect.right < GAME_WIDTH - 200:
                self.pipes.append(Pipe(GAME_WIDTH))

            # パイプの更新と衝突判定
            for pipe in self.pipes:
                pipe.update()
                if pipe.rect.left < self.bird.rect.right < pipe.rect.right and not pipe.passed:
                    self.score_board.update(self.score_board.score + 1)
                    pipe.passed = True
                if (pipe.rect.colliderect(self.bird.rect) or 
                    pipe.bottom_rect.colliderect(self.bird.rect)):
                    self.game_over = True

            # 地面との衝突判定
            if self.bird.rect.colliderect(self.ground.rect):
                self.game_over = True

            # 画面外のパイプを削除
            self.pipes = [p for p in self.pipes if not p.is_off_screen()]

    def draw(self):
        """画面を描画する"""
        self.screen.fill(SKY_BLUE)

        # 雲を描画
        for cloud in self.clouds:
            cloud.draw(self.screen)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.ground.draw(self.screen)
        self.bird.draw(self.screen)
        self.score_board.draw(self.screen)

        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to restart", True, WHITE)
            self.screen.blit(game_over_text, (GAME_WIDTH // 2 - 160, GAME_HEIGHT // 2))

        pygame.display.flip()

    def run(self):
        """ゲームのメインループ"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()