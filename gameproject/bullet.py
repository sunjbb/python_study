import pygame
from pygame.sprite import Sprite

# Sprite 精灵
class Bullet(Sprite):
    
    def __init__(self,ai_game):
        # 在飞船当前位置创建一个子弹对象
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # rect 矩形
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 存储子弹位置
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    




