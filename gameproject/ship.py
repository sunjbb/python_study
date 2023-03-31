import pygame
from pygame.sprite import Sprite
from settings import Settings

class Ship(Sprite):
    # 管理飞船类
    def __init__(self,ai_game):
        super().__init__()
        # 初始化飞船 并定义初始位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载图像 获取外形
        self.image = pygame.image.load('gameproject/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 默认每艘新飞船位于底部中央   在Pygame中，原点(0, 0)位于容器屏幕左上角，
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
        self.x = float(self.rect.x)


    def blitme(self):
        # 指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    # screen_rect是指屏幕
    # rect 飞船图像
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    