import pygame as pg
import Assets, Player, Item
from EnemyProjectile import EnemyProjectile

class Farmer(Item.Item):
    ''' The farmer who's sick of flying AstroChickens on his property! Though an 'enemy' in the literal sense, Farmer is classified as an Item, as he himself cannot harm the player. That is not to say he is COMPLETELY safe... Hitbox is on his head. Subclass of Item.Item.'''
    
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.farmer
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft = (x, y))
        self.hitbox = pg.Rect(x + 20, y + 20, 35, 28)

        self.is_egged = False
        self.timer = 0

        self.egged_index = 6
        self.shooting_left_index = 0
        self.shooting_right_index = 5
        self.anchor_y = y
        self.shooting_speed = 6 if Assets.hardMode else 10

    def shoot(self):
        bullet = EnemyProjectile(self.rect.midtop[0], self.rect.midtop[1])
        Assets.sprite_list.add(bullet)
        pg.mixer.Channel(2).set_volume(0.5)
        pg.mixer.Channel(2).play(pg.mixer.Sound(Assets.gunshotAudioPath))

    def update(self, dt):
        
    
        # Only moves right to left. Will despawn once offscreen
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed
        
        if self.timer == self.shooting_speed:
            if not self.is_egged: self.shoot()
            self.timer = 0
            self.shooting_left_index = 0
            self.shooting_right_index = 5

        # Animation
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.timer += 1 % self.shooting_speed
            self.current_time = 0
            if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and self.x >= Assets.sprite_list.sprites()[0].pos.x and not self.is_egged:
                if self.timer >= self.shooting_speed - 2 and self.shooting_left_index != 2:
                    self.shooting_left_index += 1
                self.image = self.images[self.shooting_left_index]
                self.rect = self.image.get_rect(bottomright = (self.x + 30, self.anchor_y))

            elif isinstance(Assets.sprite_list.sprites()[0], Player.Player) and self.x < Assets.sprite_list.sprites()[0].pos.x and not self.is_egged:
                if self.timer >= self.shooting_speed - 3 and self.shooting_right_index != 3:
                    self.shooting_right_index -= 1
                self.image = self.images[self.shooting_right_index]
                self.rect = self.image.get_rect(bottomleft = (self.x, self.anchor_y))



        if self.current_time >= self.animation_time / 2 and self.is_egged:
            self.current_time = 0
            self.image = self.images[self.egged_index]
            self.rect = self.image.get_rect(bottomleft = (self.x, self.anchor_y))

            if self.egged_index < 9: self.egged_index += 1
            
        self.hitbox.bottomleft = (self.rect.x + 20, self.rect.y + 20)
        
       

        if self.x < -100:
            self.kill()
    
    
    