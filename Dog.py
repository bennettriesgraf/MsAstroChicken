import pygame as pg
import Assets, Enemy, Player

class Dog(Enemy.Enemy):
    '''Dog that jumps at the player if they get too close! One of two entities that can be egged. Hitbox (for both getting caught AND hitting with an egg) are on the head. Subclass of Enemy.Enemy.'''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.dog
        self.index = 0
        self.image = self.images[self.index]
        self.hitbox = pg.Rect(x, y, 27, 20)

        self.anchor_y = y
        self.yvelocity = 0
        self.jump_height = 15
        self.gravity = .8
        
        self.jumping = False
        self.is_egged = False
        self.rising = False
        self.caught_chicken = False
        self.caught_audio_playing = False

        self.jump_index = 0
        self.egged_index = 12

        
        
    def death_animations(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time / 2.2:
            self.current_time = 0
            if self.jumping:
                self.image = self.images[7]
            else:
                self.index = (self.index + 1) % 4
                self.image = self.images[self.index + 8]
                self.rect = self.image.get_rect(topleft = (self.x, self.anchor_y))
                


    def update(self, dt):
        
        # Only moves right to left. Will despawn once offscreen
        self.rect.move_ip(self.speed, self.yvelocity)
        self.x += self.speed
    
        #Jumps when it gets close to the player.
        if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and abs(self.x - Assets.sprite_list.sprites()[0].pos.x) < 30 and Assets.sprite_list.sprites()[0].pos.y >= Assets.SCREEN_HEIGHT / 7 and not self.jumping and not self.is_egged and not Assets.sprite_list.sprites()[0].dead:
            self.yvelocity = -self.jump_height
            self.jumping, self.rising = True, True
            self.jump_index = 1
            if not self.caught_audio_playing:
                pg.mixer.Channel(1).play(pg.mixer.Sound(Assets.dogbarkaudioPath))
                self.caught_audio_playing = True

        self.yvelocity += self.gravity
        self.y += self.yvelocity

        # Stops itself when it gets to the ground
        if self.y >= self.anchor_y:
            self.y = self.anchor_y
            self.yvelocity = 0
            self.jumping = False
        

        if isinstance(Assets.sprite_list.sprites()[0], Player.Player) and Assets.sprite_list.sprites()[0].dead and Assets.sprite_list.sprites()[0].killed_by == Dog and self.caught_chicken:
            self.death_animations(dt)

        else:        
            # Animation
            self.current_time += dt
            # Normal Animation
            if self.current_time >= self.animation_time and not self.is_egged:
                self.current_time = 0
                self.image = self.images[self.index]
                if self.jumping:
                    self.image = self.images[self.jump_index]
                    if self.rising and self.jump_index < 5:
                        self.jump_index += 1

            # Egged Animation
            elif self.current_time >= self.animation_time / 2 and self.is_egged:
                self.current_time = 0
                self.image = self.images[self.egged_index]
                if self.egged_index < 14: self.egged_index += 1
        
            self.hitbox.bottomleft = (self.rect.x, self.rect.y + 20)


        if self.x < -50:
            self.kill()
    
    
    