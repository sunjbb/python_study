class Settings:
    #存储项目中所有的设置信息
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船限制
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        # 最大子弹数量
        self.bullet_allowed = 3

        # 外星人移动设置
        self.fleet_drop_speed = 90

        # 加快游戏节奏
        self.speedup_scale = 1.1
        # 分数提高
        self.scope_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.2
         # 表明机器人的移动方向。1为右移 -1为左移
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.scope_scale) 


        


    