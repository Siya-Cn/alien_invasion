import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载图片
        self.image = pygame.image.load('image/ship.jpg')
        self.rect = self.image.get_rect()

        #将飞船放在屏幕中
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #移动标志位
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_right and self.rect.right < self. screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed
        if self.moving_top and self.rect.top > 0 :
            self.y -= self.settings.ship_speed
        if self.moving_bottom and self.rect.bottom < self. screen_rect.bottom :
            self.y += self.settings.ship_speed

        #根据self.x来更新对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        #将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)