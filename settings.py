class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (235,251,255)

        #飞船属性
        self.ship_speed = 15.1
        self.ship_limit = 3

        #子弹的属性
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3000

        #外星人设置
        self.alien_speed = 2.5
        self.fleet_drop_speed = 5
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1


        