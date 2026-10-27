import pygame as pg
import Assets, Item, EnemyProjectile, Player, Enemy

class Owl(Enemy.Enemy):
    '''Cedric the Owl makes a rare cameo from Kings Quest, though he may not feel too welcome here... Run into him to gain points, but watch out! The kerfuffle may land you in a bad spot afterward. A subclass of Enemy, though doesn't harm the player.'''
    
    def __init__(self, x, y):
        super().__init__(x, y)


        self.images = Assets.owl
        self.index = 0
        self.image = self.images[self.index]
        self.rect= self.image.get_rect(center = (x, y))
        self.hitbox = self.image.get_rect(center = (x, y))

        self.speed = self.speed - 1
        self.exploded = False
        

    def collisionDetection(self):
        for entity in Assets.sprite_list:
            if pg.Rect.colliderect(self.hitbox, entity.hitbox) and type(entity) == EnemyProjectile.EnemyProjectile:
                self.exploded = True
                self.index = 0
                entity.kill()


    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed
        self.hitbox = self.image.get_rect(center = (self.x, self.y))

        if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and Assets.sprite_list.sprites()[0].dead and Assets.sprite_list.sprites()[0].killed_by == Owl:
            self.kill()

        
        
        #Animation
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if not self.exploded:    
                self.index = (self.index + 1) % 4
                self.image = self.images[self.index]
            else:
                if self.index + 4 < 7:
                    self.image = self.images[self.index + 4]
                    self.index += 1
                else:
                    self.kill()

        self.collisionDetection()
        
        if self.x < -100:
            self.kill()


class deadOwl(Item.Item):
    ''' Poor Cedric. Never stood a chance. Just used for visual flair. Subclass of Item.Item'''
    def __init__(self, x, y):
            super().__init__(x, y)
    
    
            self.images = Assets.owl[-2:]
            self.index = 0
            self.image = self.images[self.index]
            self.rect= self.image.get_rect(center = (x, y))
            self.hitbox = self.image.get_rect(center = (x, y))
    
            self.speed = self.speed - 1
            self.i = 1

    def update(self, dt):
        self.rect.move_ip(self.speed, 3)
        self.x += self.speed

        #Animation
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image = self.images[self.index]
            self.index = (self.index + 1) % 2

        if self.x < -100:
            self.kill()
        
