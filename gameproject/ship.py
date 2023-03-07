import pygame

class Ship:
    # 管理飞船类
    def __init__(self,ai_game):
        # 初始化飞船 并定义初始位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载图像 获取外形
        self.image = pygame.image.load('gameproject/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 默认每艘新飞船位于底部中央   在Pygame中，原点(0, 0)位于容器屏幕左上角，
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        # 指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
