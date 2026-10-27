import pygame as pg
import Assets, Enemy


class MV_Plane(Enemy.Enemy):
    '''The MediaVisions plane that flies over occasionally. Watch out for the propeller! A Subclass of Enemy.Enemy.'''
    def __init__(self, x, y):
        super().__init__(x, y)


        self.images = Assets.mv_plane
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft = (x, y))
        self.anchor_y = y
        self.hitbox = pg.Rect(x - 10, y + 35, 20, 25)



    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed

        #Animation
        self.current_time += dt
        if self.current_time >= self.animation_time * 2:
            self.current_time = 0
            self.index = (self.index + 1) % (len(self.images) - 1)
            self.image = self.images[self.index]
            self.rect = self.image.get_rect(bottomleft = (self.x, self.anchor_y))

        self.hitbox.bottomleft = (self.rect.x - 10, self.rect.y + 35)
        
        if self.x < -400:
            self.kill()
