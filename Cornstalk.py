import pygame as pg
import Assets, Item, Player

class Cornstalk(Item.Item):
    '''Cornstalk object. Collecting these will gain the player eggs. May spawn in groups, though that is handled with spawnEnemies() in main.py. More likely to spawn when the player is low on eggs. Subclass of Item.Item.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.cornstalk
        self.index = 0
        self.image = Assets.cornstalk[self.index]
        self.hitbox = pg.Rect(x, y, 10, 20)
        self.picked = False

    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        
        if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and pg.Rect.colliderect(self.hitbox, Assets.sprite_list.sprites()[0].corn_hitbox) and not Assets.sprite_list.sprites()[0].dead and not self.picked:
            self.image = self.images[-1]
            Assets.eggs_stored += 1
            self.picked = True
            pg.mixer.Channel(4).play(pg.mixer.Sound(Assets.cornCollectAudioPath))

            # This sprite is rendered at topLeft, so the picked over sprite is smaller and thus
            # needs to move down to compensate. This can be fixed through fenagling with the 
            # specific image rect, but it works great as is.
            self.rect.move_ip(0, 18)

        self.hitbox.bottomleft = (self.rect.x + 10, self.rect.y + 20)

        if self.x < -50:
            self.kill()
