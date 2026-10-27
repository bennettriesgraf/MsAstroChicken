import pygame as pg
import array
from Enemy import Enemy
import Projectile, Assets, Owl, Bacock, Hat, AnimatedSprite, Squirrel, EnemyProjectile, Windmill, Dog, MV_Plane


class Player(AnimatedSprite.AnimatedSprite):
    '''Ms. AstroChicken herself! Control the player with the mouse, WASD, or arrow keys, and fire eggs with Right Click or Spacebar. Uses Vector positions (pos) instead of self.x or self.y. A Subclass of AnimatedSprite.AnimatedSprite.'''
    
    def __init__(self, x, y):
        super().__init__(x, y)

        self.images = Assets.player1
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect(center=(x, y))
        self.pos = self.target = self.direction = pg.math.Vector2(self.rect.center)
        self.hitbox = pg.Rect(x, y, 30, 30)
        self.corn_hitbox = pg.Rect(x, y, 10, 20)

        self.fence_protection = 0
        self.invincibility_timer = 0
        self.fence_index = 0

        self.dead = False
        self.killed_by = 0
        self.fall_timer = 0.0
        self.reset_time_after_death = 2.2
        self.death_soundeffect_playing = False
        self.crash_soundeffect_playing = False
        self.half_index = 0.0
        self.owl_timer = 0.0

        self.anchor_x, self.anchor_y = 0, 0
        
        
    def active_gameplay(self, dt):
        key = pg.key.get_pressed()
        mouse_press = pg.mouse.get_pressed()
        mouse_pos = array.array('i', pg.mouse.get_pos())
        
        offsetX, offsetY = 0, 0
        dist = 3

        if (key[pg.K_d] or key[pg.K_RIGHT]):
            offsetX += dist
            self.target = self.pos
        if key[pg.K_w] or key[pg.K_UP]:
            offsetY -= dist
            self.target = self.pos
        if key[pg.K_s] or key[pg.K_DOWN]:
            offsetY += dist
            self.target = self.pos
        if key[pg.K_a] or key[pg.K_LEFT]:
            offsetX -= dist
            self.target = self.pos
        if mouse_press[2] or key[pg.K_SPACE]:
            self.launch()
        if mouse_press[0]:
            if mouse_pos[0] <= 150:
                mouse_pos[0] = 150
            elif mouse_pos[0] >= Assets.SCREEN_WIDTH - 180:
                mouse_pos[0] = Assets.SCREEN_WIDTH - 180
            if mouse_pos[1] <= 50:
                mouse_pos[1] = 50
            elif mouse_pos[1] >= Assets.SCREEN_HEIGHT - 120:
                mouse_pos[1] = Assets.SCREEN_HEIGHT - 120
            self.target = pg.math.Vector2(mouse_pos)
            
        self.direction = self.target - self.pos


        
        self.rect.move_ip(offsetX, offsetY)
        self.pos.x += offsetX
        self.pos.y += offsetY
        
        # Invisible Walls
        if self.pos.x <= 150 or self.pos.x >= Assets.SCREEN_WIDTH - 180:
            self.rect.move_ip(-offsetX, 0)
            self.pos.x -= offsetX
        if self.pos.y <= 50 or self.pos.y >= Assets.SCREEN_HEIGHT - 120:
            self.rect.move_ip(0, -offsetY)
            self.pos.y -= offsetY



        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

            if (self.target - self.pos).length() < dist:
                self.pos = self.target
            else:
                self.pos += self.direction * dist
            self.rect.center = self.pos

        self.hitbox.center = (self.pos.x, self.pos.y)
        self.corn_hitbox.center = (self.pos.x, self.pos.y)


        # Fence Armor animation location
        self.fence_index = 17 if self.fence_protection > 0 else 0
        

        # Animation 
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % 4
            self.image = self.images[self.index + self.fence_index]
            if self.invincibility_timer > 0:
                self.invincibility_timer -= 1


        
        self.collisionDetection()   



    def launch(self):
        if Assets.ready_to_launch and Assets.eggs_stored > 0:
            Assets.ready_to_launch = False
            egg = Projectile.Projectile(x=self.rect.midbottom[0], y=self.rect.midbottom[1] - 10)
            Assets.sprite_list.add(egg)
            Assets.eggs_stored -= 1



    def collisionDetection(self):
        for entity in Assets.sprite_list:
            if pg.Rect.colliderect(self.hitbox, entity.hitbox) and issubclass(type(entity), Enemy) and not entity.is_egged:
                if isinstance(entity, Squirrel.Squirrel):
                    if self.fence_protection > 0 and self.invincibility_timer <= 0:
                        self.fence_protection -= 1
                        self.invincibility_timer = 5
                    elif self.invincibility_timer > 0:
                        self.invincibility_timer = 5
                    else: # For if you hit a Squirrel and don't have armor
                        self.index = 0
                        self.dead = True
                        self.fall_timer = 0.0
                        self.killed_by = type(entity)
                        pg.mixer.music.pause()
                        pg.mixer.music.load(Assets.deathMusicPath)
                        pg.mixer.music.play()
                        entity.kill()
                else: # For if you are hit by any other Enemy
                    if type(entity) == Dog.Dog or type(entity) == Windmill.Windmill: entity.caught_chicken = True
                    self.dead = True
                    self.fall_timer = 0.0
                    self.killed_by = type(entity)
                    entity.index = 0
                    self.anchor_x, self.anchor_y = self.rect.bottomright[0], self.rect.bottomright[1]
                    if type(entity) != Owl.Owl:
                            pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[1]))
                            pg.mixer.music.pause()
                            if type(entity) == Dog.Dog: pg.mixer.music.load(Assets.dogCatchAudioPath)
                            else: pg.mixer.music.load(Assets.deathMusicPath)
                            pg.mixer.music.play()
                    
    

    def death_animations(self, enemy, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if enemy == Squirrel.Squirrel:
                self.fall_timer += dt
                self.index = (self.index + 1) % 4
                self.image = self.images[self.index + 21]
                self.rect.move_ip(-10, 0)
            
            elif enemy == EnemyProjectile.EnemyProjectile:  
                if self.index + 4 < 11:    
                    self.index += 1
                    self.image = self.images[self.index + 4]
                    self.rect = self.image.get_rect(bottomright = (self.anchor_x, self.anchor_y))
                elif self.index + 4 == 11:
                    self.current_time += dt * 2
                    self.fall_timer += dt
                    if self.fall_timer >= 0.5:
                        self.rect.move_ip(0, 30)
                        if not self.death_soundeffect_playing:
                            pg.mixer.Channel(0).play(pg.mixer.Sound(Assets.launchaudioPath))
                            self.death_soundeffect_playing = True
                    if self.fall_timer >= 1:
                        if not self.crash_soundeffect_playing:
                            # pg.mixer.Channel(0).play(pg.mixer.Sound(Assets.crashAudioPath))
                            pg.event.post(pg.event.Event(Assets.SCREEN_SHAKE))
                            self.crash_soundeffect_playing = True

            elif enemy == MV_Plane.MV_Plane:
                self.fall_timer += dt
                if self.index + 12 < 16:
                    self.half_index += 0.5
                    self.index = int(self.half_index)
                    self.image = self.images[self.index + 12]
                    self.rect = self.image.get_rect(bottomright = (self.anchor_x, self.anchor_y))
                elif self.index + 12 == 16:
                    hat = Hat.Hat(self.rect.midbottom[0], self.rect.midbottom[1])
                    Assets.sprite_list.add(hat)                   
                    self.index += 1
                elif self.index + 12 == 17:
                    self.rect.move_ip(-3, 3)
                    
            elif enemy == Owl.Owl:
                self.image = self.images[self.index + 25]
                self.index = (self.index + 1) % 4
                self.owl_timer += dt
                if self.owl_timer >= 0.75:
                    self.dead = False
                    self.killed_by = 0
                    self.index = 0
                    Assets.score += 25
                    bacock = Bacock.Bacock(Assets.SCREEN_WIDTH / 4, Assets.SCREEN_HEIGHT / 2)
                    Assets.sprite_list.add(bacock)
                    deadOwl = Owl.deadOwl(self.pos.x, self.pos.y)
                    Assets.sprite_list.add(deadOwl)
                    self.owl_timer = 0.0

            elif enemy == Windmill.Windmill:
                self.rect = self.image.get_rect(topleft = (Assets.SCREEN_WIDTH, Assets.SCREEN_HEIGHT))            
                self.fall_timer += dt

            elif enemy == Dog.Dog:
                self.rect = self.image.get_rect(topleft = (Assets.SCREEN_WIDTH, Assets.SCREEN_HEIGHT))
                self.fall_timer += dt * 2.2

            if self.fall_timer >= self.reset_time_after_death:
                pg.mixer.Channel(0).pause()
                if Assets.lives > 0:   
                    pg.event.post(pg.event.Event(Assets.DEATH_EVENT))
                else:
                    pg.event.post(pg.event.Event(Assets.GAME_OVER))



    def update(self, dt):
        if not self.dead:
            self.active_gameplay(dt)
        else:
            self.death_animations(self.killed_by, dt)