import pygame.font
from pathlib import Path
import json

from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分图像
        self.prep_score()
        #准备最高分图像
        self.prep_high_score()

        self.prep_ships()

    def prep_ships(self):
        #显示剩下的飞船
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_high_score(self):
        high_score = round(self.stats.high_score,-1)
        high_score_str = f'{high_score}'
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        #将最高分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

        '''
        path = Path('self.high_score_rect.top.json')
        contents = json.dumps(self.high_score_rect.top)
        path.write_text(contents)
        '''

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        
        #在屏幕右上角显示
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()