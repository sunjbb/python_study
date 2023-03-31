import pygame.font

from pygame.sprite import Group
from ship import Ship


# 计分板
class ScoreBoard:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.game_stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    # 当前得分
    def prep_score(self):
        # 将得分渲染为图像
        randed_score = round(self.stats.score,-1)
        score_str = "{:,}".format(randed_score)
        # score_str = str(self.stats.score)
        self.score_image =  self.font.render(score_str, True, self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    # 最高分渲染
    def prep_high_score(self):
        high_score = round(self.stats.high_score,-1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,self.settings.bg_color)
        self.high_score_rect =self.high_score_image.get_rect()
        self.high_score_rect.centerx =self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    # 检查最高分
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    # 展示等级（关卡数）
    def prep_level(self):
        # 将等级转换为渲染的图像
        level_str = str(round(self.stats.level))
        self.level_image = self.font.render(level_str, True, self.text_color,self.settings.bg_color)

        # 将等级放到得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.top + 30
    
    def prep_ships(self):
        self.ships = Group()
        for ship_num in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    



