import pygame as pg
import Assets


class AnimatedSprite(pg.sprite.Sprite):
    '''Only has three inherent, non-Sprite variables: animation_time, current_time, and speed. Subclass of pygame.sprite.Sprite'''
    def __init__(self, x, y):
        super().__init__()
        # Sets the animation times intended frames for EACH animated sprite
        self.animation_time = Assets.animation_time #default = 0.10

        self.current_time = 0

        # Speed value of EVERY enemy unit
        self.speed = -7 if Assets.hardMode else -4

        

    def update(self, dt):
        '''Does nothing on its own. Every subclass of this has its own unique properties. Run every frame.'''
        pass