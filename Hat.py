import Assets, Item


class Hat(Item.Item):
    '''Entity that falls off the player for the plane death animation. Purely aesthetic. Subclass of Item.Item'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.hat
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft = (x, y))
        self.grounded = False

    def update(self, dt):
        if not self.grounded:
            self.rect.move_ip(0, abs(self.speed) + 2)
            self.y += abs(self.speed) + 2
        else:
            self.rect.move_ip(self.speed, 0)


        if self.y >= Assets.SCREEN_HEIGHT - 90:
            self.grounded = True

        #Animation
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if not self.grounded:
                self.index = (self.index + 1) % 4
                self.image = self.images[self.index]
            elif self.index + 4 < 9:
                self.image = self.images[self.index + 4]
                self.index += 1


            
        if self.x < -50:
            self.kill()
