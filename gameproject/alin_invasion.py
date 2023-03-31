import sys
import pygame

from time import sleep
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)
        self.game_stats = GameStats(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,'Play')
        self.sb = ScoreBoard(self)


        pygame.display.set_caption("Alien Invasion")

        """设置背景颜色"""
        self.bg_color = (230,230,230)
    
    """主运行程序"""
    def run_game(self):

        while True:    
            """监听鼠标键盘事件"""
            self._check_events()
            if self.game_stats.game_active:
                """判断是否移动飞船"""
                self.ship.update()
                """渲染子弹"""
                self._update_bullets()
                # 移动外星人
                self._update_aliens()

            # """修改屏幕信息，如内容和背景"""
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)



            # 随着动作进行背景变化
            # elif event.type:
            #     self.bg_color = (randint(0,255),randint(0,255),randint(0,255))

    # 检查是否点击游戏开始按钮
    def _check_play_button(self,mouse_pos):
        # self.game_stats.game_active == False 太low
        if not self.game_stats.game_active and self.play_button.rect.collidepoint(mouse_pos):
            # 重置设置信息
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息。
            self.game_stats.reset_stats()
            self.game_stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏鼠标
            pygame.mouse.set_visible(False)



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
        if not self.game_stats.game_active:
            self.play_button.draw_button()
        self.sb.show_score()
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

        self._check_bullet_alien_collisions()

    # 消灭外星人
    def _check_bullet_alien_collisions(self):
                # 检查两个集合中是否有重复 有就消除
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
        if collisions:
            for aliens in collisions.values():
                self.game_stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()


        # 判断是否消灭完毕
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.game_stats.level += 1
            self.sb.prep_level()
            # self.settings.fleet_drop_speed += 4


        
    """创建外星群"""
    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        # 计算极限空间
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # // 整除 只求商 不要余数 
        number_alines_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height-(3*alien_height)-ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows):
            for alien_number in range(number_alines_x):
                self._create_alien(alien_number,row_number)

    # 创建外星人
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 *alien_width *alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2*alien_height  * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            # print('你挂了')
            self._ship_hit()
        self._check_aliens_bottom()
    
    # 阵亡情况
    def _ship_hit(self):
        # 命减一
        if self.game_stats.ship_left > 0:
            self.game_stats.ship_left -= 1
            self.sb.prep_ships()
            # 清空屏幕
            self.aliens.empty()
            self.bullets.empty()
            # 重置资源
            self._create_fleet()
            self.ship.center_ship()
            # 延迟等待
            sleep(0.7)
        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)

    # 检查外星舰队是否抵达底部
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    # 修改舰队方向
    def _change_fleet_direction(self):
        # 将整群外星人下移，改变移动方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  

    # 检查舰队边缘
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break   
                



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()



