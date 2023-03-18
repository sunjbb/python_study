# 统计游戏中的信息
class GameStats:

    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # 标明游戏是否运行
        self.game_active = False

    # 初始化统计数据   
    def reset_stats(self):

        self.ship_left = self.settings.ship_limit