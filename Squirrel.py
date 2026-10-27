import Assets, Enemy


class Squirrel(Enemy.Enemy):
    '''Flying squirrel enemy. Pops up at the players last known y-coordinate. A Subclass of Enemy.Enemy.'''
    def __init__(self, x, y):
        super().__init__(x, y)


        self.images = Assets.squirrel
        self.index = 0
        self.image = self.images[self.index]
        self.hitbox = self.rect

        # A little faster than other sprites
        self.speed = self.speed - 1


    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed
        self.hitbox = self.rect

        #Animation
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        
        if self.x < -200:
            self.kill()
