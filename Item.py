import Assets, AnimatedSprite

class Item(AnimatedSprite.AnimatedSprite):
    '''Parent class of entities that are not meant to harm the player. Variables: image (defaults to player image), rect, hitbox, x, y. Subclass of AnimatedSprite.AnimatedSprite.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        # Defaults to player image when no subclass is defined
        self.image = Assets.player1[0]

        # # Established necessary variables 
        # # (Rect hitbox, x and y coordinates, etc)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.hitbox = self.rect
        self.x, self.y = x, y




    def update(self, dt):
        '''Does nothing on its own. Every subclass of this has its own unique properties. Run every frame.'''
        pass



    
