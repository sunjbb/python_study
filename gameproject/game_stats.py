# 统计游戏中的信息
class GameStats:

    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # 标明游戏是否运行
        self.game_active = False
        self.high_score = 0

       

    # 初始化统计数据   
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
         # 得分
        self.score = 0
        self.level = 1