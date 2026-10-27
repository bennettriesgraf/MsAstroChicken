import pygame as pg
import Assets, Enemy


class EnemyProjectile(Enemy.Enemy):
    '''The bullet the farmer shoots out of his gun. Subclass of Enemy.Enemy'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image = Assets.bullet[0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.hitbox = self.rect
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.velocity = pg.math.Vector2()

        self.velocity.from_polar((abs(self.speed) + 3, 270))



    def update(self, dt):
        self.rect.move_ip(self.velocity)
        self.pos += self.velocity
        self.hitbox = self.rect

        if self.pos.y < -20:
            self.kill()

