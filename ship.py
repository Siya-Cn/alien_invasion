import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载图片
        self.image = pygame.image.load('image/ship.jpg')
        self.rect = self.image.get_rect()

        #将飞船放在屏幕中
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #移动标志位
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self. screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed


        #根据self.x来更新对象
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)