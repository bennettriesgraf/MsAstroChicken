import Assets, Enemy, Player, Item

class Windmill(Enemy.Enemy):
    '''The humble Windmill. Try not to get chopped. A Subclass of Enemy.Enemy'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.windmill
        
        self.index = 0
        self.image_blades = self.images[:9]
        
        self.image = self.image_blades[self.index]
        self.windmill_tower = Windmill_Tower(x - 2, y + 39)
        self.caught_chicken = False
        
        
    def death_animations(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0

            if self.index + 3 < 8:
                self.index += 1
                self.image = self.images[self.index + 3]

    def update(self, dt):
        
        # Only moves right to left. Will despawn once offscreen
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed

        if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and Assets.sprite_list.sprites()[0].dead and Assets.sprite_list.sprites()[0].killed_by == Windmill and self.caught_chicken:
            self.death_animations(dt)

        else:
            self.current_time += dt
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % 4
                self.image = self.images[self.index]
                        
        if self.x < -50:
            self.kill()


class Windmill_Tower(Item.Item):
    '''No blades, no problem. Created at the same time as Windmill. A Subclass of Item.Item.'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Assets.windmill[-1]


    def update(self, dt):
        self.rect.move_ip(self.speed, 0)
        self.x += self.speed

        if self.x < -50:
            self.kill()

    
    
    