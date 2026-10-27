import pygame as pg
import random
import Farmer, Dog, AnimatedSprite, Assets

class Projectile(AnimatedSprite.AnimatedSprite):
    ''' The eggs you throw as Ms. AstroChicken. Follows parabolic movement with gravity/air resistance factor (self.gravity and self.air_drag). Can only hit Farmers and Dogs. A Subclass of AnimatedSprite.AnimatedSprites'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.egg
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.x, self.y = x, y
        self.hitbox = pg.Rect(x, y, 15, 15)

        self.gravity = 2.5
        self.y_velocity = 5
        self.timer = 0
        self.grounded = False
        self.i = 0
        self.air_drag = 0.0
        
        pg.mixer.Channel(0).set_volume(.5)
        pg.mixer.Channel(0).play(pg.mixer.Sound(Assets.launchaudioPath))


    def collisionDetection(self):
        for enemy in Assets.sprite_list:
            if pg.Rect.colliderect(self.hitbox, enemy.hitbox) and ((type(enemy) is Farmer.Farmer) or (type(enemy) is Dog.Dog)) and not enemy.is_egged:
                enemy.is_egged = True

                if type(enemy) == Dog.Dog: Assets.score += random.randint(2, 4)
                elif type(enemy) == Farmer.Farmer: Assets.score += random.randint(5, 7)

                pg.mixer.Channel(0).pause()
                pg.mixer.Channel(3).set_volume(.5)
                pg.mixer.Channel(3).play(pg.mixer.Sound(Assets.hitEnemyAudioPath))

                Assets.ready_to_launch = True
                self.kill()


    def update(self, dt):
        if self.y >= Assets.screen.get_height() - 90 and not self.grounded:
            Assets.ready_to_launch = True
            self.grounded = True
            pg.mixer.Channel(0).pause()
            pg.mixer.Channel(3).set_volume(.5)
            pg.mixer.Channel(3).play(pg.mixer.Sound(Assets.hitGroundAudioPath))

        if not self.grounded:
            self.rect.move_ip(7 - self.air_drag, .06 * self.y_velocity * self.gravity**2)
            self.collisionDetection()
            self.y_velocity += 1.5
        else:
            self.rect.move_ip(self.speed, 0)

        if self.air_drag < 7:
            self.air_drag += 0.2

        self.x = self.rect.centerx
        self.y = self.rect.centery

        # Animation
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if not self.grounded:
                self.index = (self.index + 1) % 7
            else:
                self.index = (8 + self.i)
                if self.i < 4:
                    self.i += 1
            self.image = self.images[self.index]

        self.hitbox.topleft = (self.rect.x, self.rect.y)

        if self.x < -50:
            self.kill()