import sys
import pygame
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

        """设置背景颜色"""
        self.bg_color = (230,230,230)
    
    """主运行程序"""
    def run_game(self):

        while True:    
            """监听鼠标键盘事件"""
            self._check_events()
            """判断是否移动飞船"""
            self.ship.update()
            """渲染子弹"""
            self._update_bullets()
            """修改屏幕信息，如内容和背景"""
            self._update_screen()

    """监听鼠标键盘事件"""
    def _check_events(self):
        """pygame.QUIT 单击关闭按钮"""
        for event in pygame.event.get():
             
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


            # 随着动作进行背景变化
            # elif event.type:
            #     self.bg_color = (randint(0,255),randint(0,255),randint(0,255))

    """KeyDown 事件"""
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            # self.ship.rect.x += 1
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            """必须是英文q"""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            """可以开火但是子弹有限制"""
            self._fire_bullet()
    
    """keyup事件"""
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    """渲染游戏背景"""
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        """顺序不能错，如果先放飞船，再设置颜色，就覆盖上了"""
        self.ship.blitme()
        """渲染子弹"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """渲染外星人"""
        self.aliens.draw(self.screen)

        pygame.display.flip()

    """发射子弹"""
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """清理子弹"""
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            # print(bullet.rect.bottom)
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    """创建外星人"""
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        # 计算极限空间
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # // 整除 只求商 不要余数 
        number_alines_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_alines_x):
            alien = Alien(self)
            alien.x = alien_width + 2 *alien_width *alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)



        




            

    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()




