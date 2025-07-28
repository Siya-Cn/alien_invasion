import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('My Little Pony')

        #加载背景图片
        self.bg_image = pygame.image.load('image/forest.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        #加载背景音乐
        pygame.mixer.music.load('sound/my little pony.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        #加载外星人被击中音效
        self.alien_hit_sound = pygame.mixer.Sound('sound/碧琪.mp3')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)

        #游戏启动后处于活动状态
        self.game_active = False
        self.play_button = Button(self,'Game Start')

        self._create_fleet()


        #设置背景颜色
        #self.bg_color = (249,241,249)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x ,current_y = alien_width,alien_height

        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)

                #x，y增加
                current_x += 4 * alien_width
            #添加完一行外星人后，重置x，并递增y
            current_x = alien_width
            current_y += 2*alien_height

    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

              
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
     
                 
    def _check_keydown_event(self,event):
        #print(f"Pressed key: {event.key}")
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
        if event.key == pygame.K_p:
            if self.game_active:
                self.game_active = False
            else:
                self.game_active = True

        

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
        self.screen.blit(self.bg_image,(0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        if not self.game_active :
            self.play_button.draw_button()

    def _update_bullets(self):
        self.bullets.update()

        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 
        #print(self.bullets)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        
        if collisions:
            #播放外星人被击中音效
            self.alien_hit_sound.play()
            
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1  # 改变外星人移动方向

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("The magic of friendship!")
            self._ship_hit()

        self._check_aliens_bottom

    def _check_aliens_bottom(self):   
        #检查外星人是否到达屏幕底部
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _ship_hit(self):
        if self.stats.ships_left > 0 :
            #将ship_left减1
            self.stats.ships_left -= 1

            #清空外星人和子弹
            self.bullets.empty()
            self.aliens.empty()

            #创建新的舰队
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active = False
    
    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            
            #屏幕可见
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__' :
    #创建游戏实例
    ai = AlienInvasion()
    ai.run_game()

                    