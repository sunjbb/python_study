import pygame

class Sky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500,400))
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                #  pygame.QUIT 单击关闭按钮
                if event.type == pygame.QUIT:
                    sys.exit()     
            self.screen.fill((0,255,255))
            pygame.display.flip()

if __name__ == '__main__':
    Sky().run_game()


