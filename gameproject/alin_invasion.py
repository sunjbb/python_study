import sys
import pygame
from random import randint
from setting import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

        # 设置背景颜色
        self.bg_color = (230,230,230)
    def _check_events(self):
    #    监听鼠标键盘事件
        for event in pygame.event.get():
             #  pygame.QUIT 单击关闭按钮
            if event.type == pygame.QUIT:
                sys.exit()                
            # 随着动作进行背景变化
            # elif event.type:
            #     self.bg_color = (randint(0,255),randint(0,255),randint(0,255))

    def _update_screen(self):
        # 为表面设置颜色
        self.screen.fill(self.setting.bg_color)
        # 顺序不能错，如果先放飞船，再设置颜色，就覆盖上了
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            # 监听鼠标键盘事件
            self._check_events()
            # 修改屏幕信息，如内容和背景
            self._update_screen()
            

    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




