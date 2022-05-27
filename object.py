import pygame

class Pad:
    def __init__(self, WIDTH, HEIGHT):
        self.padWidth = 100
        self.padHeight = 10
        self.DEFAULT_SIZE = 100
        self.SCREEN_WIDTH = WIDTH
        self.startX = int((WIDTH//2) - (self.DEFAULT_SIZE//2))
        self.startY = HEIGHT - 40
        self.pad = pygame.Rect(self.startX, self.startY, self.padWidth, self.padHeight)
        self.speed = 10
        

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 200, 0), self.pad)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.pad.x > 5:
            self.pad.x = self.pad.x - self.speed
        if keys_pressed[pygame.K_RIGHT] and self.pad.x < self.SCREEN_WIDTH - self.pad.width - 5:
            self.pad.x = self.pad.x + self.speed
    def reset(self):
        self.pad.x = self.startX
        self.pad.y = self.startY
        self.pad.width = self.DEFAULT_SIZE
        self.pad.height = self.padHeight
        
class Ball:
    def __init__(self, WIDTH, HEIGHT):
        self.startX = int(WIDTH/2)
        self.startY = HEIGHT - 50
        self.size = 10
        self.speed = 5
        self.DEFAULT_SPEED = 5
        self.ball = pygame.Rect(self.startX, self.startY , self.size, self.size)
        self.x_dir = 1
        self.y_dir = -1
        self.isMoving = True
    def draw(self, surface):
        pygame.draw.ellipse(surface, (255, 255, 255), self.ball) 
    def move(self):
        if self.isMoving:
            self.ball.x = self.ball.x + (self.speed * self.x_dir)
            self.ball.y = self.ball.y + (self.speed * self.y_dir)
    def reset(self):
        self.x_dir = 1
        self.y_dir = -1
        self.isMoving = True
        self.speed = self.DEFAULT_SPEED
        self.ball.x = self.startX 
        self.ball.y = self.startY


class Brick():
    def __init__(self, x, y):
        brick_width = 40
        brick_height = 20
        self.color = (255, 0, 255)
        self.brick = pygame.Rect(100 + (x * brick_width), 100 + (y* brick_height), brick_width, brick_height)
    def draw(self, surface):
        pygame.draw.rect(surface,(self.color),self.brick)