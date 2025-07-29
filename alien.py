import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game,alien_type='碧琪'):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.alien_type = alien_type

        #加载外星人图像并设置其rect属性
        if alien_type == '碧琪':
            self.image = pygame.image.load('image/碧琪.png')
        if alien_type == '紫悦':
            self.image = pygame.image.load('image/紫悦.png')
        if alien_type == '珍奇':
            self.image = pygame.image.load('image/珍奇.png')
        if alien_type == '柔柔':
            self.image = pygame.image.load('image/柔柔.png')
        if alien_type == '云宝':
            self.image = pygame.image.load('image/云宝.png')
        if alien_type == '苹果嘉儿':
            self.image = pygame.image.load('image/苹果嘉儿.png')

        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的水平位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)