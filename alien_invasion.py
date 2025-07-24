import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('My Little Polly')
        self.ship = Ship(self)

        #设置背景颜色
        #self.bg_color = (249,241,249)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #向右移动
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    #向左移动
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                  

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
            #屏幕可见
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__' :
    #创建游戏实例
    ai = AlienInvasion()
    ai.run_game()

                    