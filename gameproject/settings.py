class Settings:
    #存储项目中所有的设置信息
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船限制
        self.ship_speed = 1.5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        # 最大子弹数量
        self.bullet_allowed = 3

        # 外星人移动设置
        self.alien_speed = 0.2
        self.fleet_drop_speed = 90

        # 表明机器人的移动方向。1为右移 -1为左移
        self.fleet_direction = 1

        


    