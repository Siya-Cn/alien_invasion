import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('My Little Polly')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #设置背景颜色
        #self.bg_color = (249,241,249)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_event(self,event):
        print(f"Pressed key: {event.key}")
        if event.key == pygame.K_RIGHT:
            #向右移动
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            #向左移动
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            #向上移动
            self.ship.moving_top = True
        if event.key == pygame.K_DOWN:
            #向下移动
            self.ship.moving_bottom = True
        if event.key == pygame.K_q :
            sys.exit()
        if event.key == pygame.K_SPACE :
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

                  

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

    def _update_bullets(self):
        self.bullets.update()

        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 
        print(self.bullets)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            
            self._update_screen()

            
            
            #屏幕可见
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__' :
    #创建游戏实例
    ai = AlienInvasion()
    ai.run_game()

                    