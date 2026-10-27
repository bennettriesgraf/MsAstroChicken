import Assets, random, Item

class Hill(Item.Item):
    '''Hill object. This is a subclass of Item.Item.'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.images = Assets.hill
        self.index = random.randint(0, 1)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft = (x, y))
        
    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed
        
        if self.x < -250:
            self.kill()


class Grass(Item.Item):
    '''Grass object. This is a subclass of Item.Item.'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.images = Assets.grass
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft = (x, y))
        
        # This statement allows for the parralax scrolling effect.
        # Moves faster when closer to camera
        if y == Assets.SCREEN_HEIGHT - 50:
            self.speed = self.speed - 2
        else: self.speed = self.speed - 1

    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed
        
        if self.x < -100:
            self.kill()



class Rock(Item.Item):
    '''Rock object. This is a subclass of Item.Item.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.rock
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft = (x, y))
        
        # This statement allows for the parralax scrolling effect.
        # Moves faster when closer to camera
        if y == Assets.SCREEN_HEIGHT - 50:
            self.speed = self.speed - 2
        else: self.speed = self.speed - 1

    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed
        
        if self.x < -100:
            self.kill()