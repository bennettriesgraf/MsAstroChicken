import Assets, AnimatedSprite

class Bacock(AnimatedSprite.AnimatedSprite):
    '''Animated Bacock! Subclass of AnimatedSprite.AnimatedSprite.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.bacock
        self.index = 0

        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft = (x, y))
        self.hitbox = self.rect
        self.timer = 0.0
        



    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                self.timer += dt
                if self.timer >= 0.5:
                    self.kill()
            self.image = self.images[self.index]
            


