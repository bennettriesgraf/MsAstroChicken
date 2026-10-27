
import Assets, AnimatedSprite

class Enemy(AnimatedSprite.AnimatedSprite):
    ''' This class is used to define entities that will kill the player. Variables: image (uses player image as place-holder), rect, hitbox, x, y, is_egged (though only two enemy types can be egged). Subclass of AnimatedSprite.AnimatedSprite.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        # Placeholder value, will get changed when subclass is initialized
        self.image = Assets.player1[0]

        self.rect = self.image.get_rect(topleft = (x,y))
        self.hitbox = self.rect
        self.x, self.y = x, y

        self.is_egged = False


    def update(self, dt):
        '''Does nothing on its own. Every subclass of this has its own unique properties. Run every frame.'''
        pass



    
