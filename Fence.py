import pygame as pg
import Assets, Item, Player

class Fence(Item.Item):
    '''A helpful item for the player to collect. Protects against Squirrels for 2 hits. Subclass of Item.Item.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.fence
        self.index = 0
        self.image = Assets.fence[self.index]
        self.picked = False



    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        
        if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and pg.Rect.colliderect(self.rect, Assets.sprite_list.sprites()[0].rect) and not Assets.sprite_list.sprites()[0].dead and not self.picked:
            self.image = self.images[-1]
            Assets.sprite_list.sprites()[0].fence_protection = 2
            self.picked = True
            pg.mixer.Channel(2).set_volume(.5)
            pg.mixer.Channel(2).play(pg.mixer.Sound(Assets.fenceShingAudioPath))


        if self.x < -100:
            self.kill()
