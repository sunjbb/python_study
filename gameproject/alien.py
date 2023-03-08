import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,ai_game):
        # 初始化
        super().__init__()
        self.screen = ai_game.screen

        # 加载图像
        self.image = pygame.image.load('gameproject/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储精确的水平位置
        self.x = float(self.rect.x)
        

