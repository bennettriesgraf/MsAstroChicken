import pygame as pg
from Player import Player
import sys, asyncio, os, random, time
import Owl, MV_Plane, Dog, Farmer, Windmill, Background, Assets, Squirrel, Cornstalk, Fence



# Welcome! This is the main loop file for my recreation of the arcade-like mini game
# from Space Quest IV, Ms. AstroChicken.

# Space Quest is a series of point-and-click adventure games created by Sierra Entertainment, Inc. 
# I do not claim to own the original assets of this property. All rights reserved.

# This particular implentation was put together by Bennett Riesgraf. 





pg.init(), pg.display.init(), pg.font.init(), pg.mixer.init()




Assets.screen = pg.display.set_mode(size=(Assets.SCREEN_WIDTH, Assets.SCREEN_HEIGHT)) 
Assets.screen.set_colorkey(None)
Assets.screen.fill(color="black")

pg.mixer.music.load(Assets.bgMusicPath)
pg.mixer.music.set_volume(0.7)

pg.display.set_caption("Ms. AstroChicken - Flight of the Pullet")


clock = pg.time.Clock()

player = Player(Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 4.17)


Assets.sprite_list.add(player)

# Uses "Press Start Regular"
font = pg.font.Font(Assets.fontPath, size=20)

titletext = font.render('"Flight of the Pullet."', True, "purple", "black")
titletext = pg.transform.scale_by(titletext, .6)
titletextRect = titletext.get_rect()
titletextRect.center = (Assets.SCREEN_WIDTH / 4, Assets.SCREEN_HEIGHT - 122)

eggtext = font.render('Eggs:' + str(Assets.eggs_stored), True, (255, 241, 84), (0, 0, 0))
eggtext = pg.transform.scale_by(eggtext, .6)
eggtextRect = eggtext.get_rect()
eggtextRect.center = (Assets.SCREEN_WIDTH / 2 + 22, Assets.SCREEN_HEIGHT - 16)

scoretext = font.render('Score:' + str(Assets.score), True, (255, 241, 84), (0, 0, 0))
scoretext = pg.transform.scale_by(scoretext, .6)
scoretextRect = scoretext.get_rect()
scoretextRect.center = (Assets.SCREEN_WIDTH - 100, Assets.SCREEN_HEIGHT - 16)

gameOvertext = font.render('Game Over', True, (0, 0, 0), "grey")
gameOvertextrect = gameOvertext.get_rect()
gameOvertextrect.center = (Assets.SCREEN_WIDTH/2, Assets.SCREEN_HEIGHT/2 - 20)

lives_image = Assets.lives_images[Assets.lives - 1]
lives_image_rect = lives_image.get_rect()
lives_image_rect.bottomleft = (25, Assets.SCREEN_HEIGHT - 6)

pulletSurprise_text1 = font.render('Congratulations! In achieving the coveted rank of', True, 'purple', 'black')
pulletSurprise_text1 = pg.transform.scale_by(pulletSurprise_text1, .5)
pulletSurprise_text1_rect = pulletSurprise_text1.get_rect()
pulletSurprise_text1_rect.center = (Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 4)

pulletSurprise_text2 = font.render('"Corn-Wheezer", you have won the Pullet Surprise!', True, 'purple', 'black')
pulletSurprise_text2 = pg.transform.scale_by(pulletSurprise_text2, .5)
pulletSurprise_text2_rect = pulletSurprise_text2.get_rect()
pulletSurprise_text2_rect.center = (Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 4 + 40)

pulletSurprise_bonus = font.render('5 X ' + str(Assets.eggs_stored) + ' eggs = ' + str(Assets.eggs_stored * 5) + ' bonus points', True, 'yellow', 'black')
pulletSurprise_bonus = pg.transform.scale_by(pulletSurprise_bonus, .5)
pulletSurprise_bonus_rect = pulletSurprise_bonus.get_rect()
pulletSurprise_bonus_rect.center = (Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 2)

hardmode_text = font.render('Hard Mode', True, 'red', 'black')
hardmode_text = pg.transform.scale_by(hardmode_text, .5)
hardmode_text_rect = hardmode_text.get_rect()
hardmode_text_rect.center = (Assets.SCREEN_WIDTH - 100, Assets.SCREEN_HEIGHT - 16)



cursor_image = Assets.cursor_images[1]
cursor_image_rect = cursor_image.get_rect()
cursor_image_rect.center = (0, 0)


cursor = pg.cursors.Cursor((13, 13), cursor_image)
pg.mouse.set_cursor(cursor)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8]




def spawnEnemy(factor):
    #[ 0 = Farmer, 1 = Windmill, 2 = Dog, 
    #   3 = Squirrel, 4 = Cornfield, 5 = Fence, 
    #    6 = Hill, 7 = MV_Plane, 8 = Owl]
    if Assets.eggs_stored < 3:
        weights = [11, 11, 11, 11, 17, 4, 11, 5, 1]
    elif Assets.sprite_list.sprites()[0].fence_protection > 0:
        weights = [14, 11, 14, 13, 4, 1, 13, 6, 1]
    else:
        weights = [14, 11, 14, 11, 4, 6, 12, 6, 1]
    
    num = random.choices(a, weights, k=1)
    enemy = 0
    
    if num[0] == 0 and Assets.last_enemy != Farmer.Farmer and Assets.last_enemy != Background.Hill: #spawn Farmer
        enemy = Farmer.Farmer(Assets.SCREEN_WIDTH + 10 + factor,
                                 Assets.SCREEN_HEIGHT - 90)
        Assets.sprite_list.add(enemy)

    elif num[0] == 1 and Assets.last_enemy != Windmill.Windmill: #spawn Windmill
        enemy = Windmill.Windmill(Assets.SCREEN_WIDTH + 10 + factor,
                        Assets.SCREEN_HEIGHT - 225)
        Assets.sprite_list.add(enemy.windmill_tower)
        Assets.sprite_list.add(enemy)

    elif num[0] == 2 and Assets.last_enemy != Dog.Dog: #spawn Dog
        enemy = Dog.Dog(Assets.SCREEN_WIDTH + 10 + factor,
                        Assets.SCREEN_HEIGHT - 125)
        Assets.sprite_list.add(enemy)

    elif num[0] == 3 and Assets.last_enemy != Squirrel.Squirrel: #spawn Squirrel
        enemy = Squirrel.Squirrel(Assets.SCREEN_WIDTH + 30 + factor, Assets.sprite_list.sprites()[0].pos.y)
        Assets.sprite_list.add(enemy)

    elif num[0] == 4 and Assets.last_enemy != Cornstalk.Cornstalk: #spawn Cornfield
        cornRows = random.randint(1, 3)
        for j in range(cornRows):
            cornCount = random.randint(2, 6)
            for i in range(cornCount):
                enemy = Cornstalk.Cornstalk(Assets.SCREEN_WIDTH + (22 * i + 2) + factor + (150 * j),
                                    Assets.SCREEN_HEIGHT - 157)
                Assets.sprite_list.add(enemy)
                if i == cornCount and random.randint(0, 2) == 2:
                    enemy = Dog.Dog(Assets.SCREEN_WIDTH + 10 + factor + (22* i),
                                            Assets.SCREEN_HEIGHT - 125)
                    Assets.sprite_list(enemy)
            
    elif num[0] == 5 and Assets.last_enemy != Fence.Fence: #spawn Fence
        enemy = Fence.Fence(Assets.SCREEN_WIDTH + 10 + factor,
                                Assets.SCREEN_HEIGHT - 180)
        Assets.sprite_list.add(enemy)

    elif num[0] == 6 and Assets.last_enemy != Background.Hill and Assets.last_enemy != Farmer.Farmer: #spawn Hill
        t = random.randint(0, 2)
        if t == 1: #Spawn Farmer on Hill
            enemy = Farmer.Farmer(Assets.SCREEN_WIDTH + 50 + factor,
                                    Assets.SCREEN_HEIGHT - 110)
            Assets.sprite_list.add(enemy)
        elif t == 2: #Spawn Dog on Hill
            enemy = Dog.Dog(Assets.SCREEN_WIDTH + 30 + factor,
                                    Assets.SCREEN_HEIGHT - 150)
            Assets.sprite_list.add(enemy)
        enemy = Background.Hill(Assets.SCREEN_WIDTH + 10 + factor,
                                Assets.SCREEN_HEIGHT - 80)
        Assets.sprite_list.add(enemy)

    elif num[0] == 7 and Assets.last_enemy != MV_Plane.MV_Plane: #Spawn MV Plane
        enemy = MV_Plane.MV_Plane(Assets.SCREEN_WIDTH + 30 + factor, 75)
        Assets.sprite_list.add(enemy)

    elif num[0] == 8 and Assets.last_enemy != Owl.Owl: #Spawn Cedric the Owl
        enemy = Owl.Owl(Assets.SCREEN_WIDTH + 260 + factor, 65)
        Assets.sprite_list.add(enemy)

    if enemy == 0:
        spawnEnemy(factor = factor)
    else: Assets.last_enemy = type(enemy)




def spawnBackgroundEntities(dt):
    '''Spawns the grass and rocks in the foreground, on a random timer.'''
    Assets.spawnTimer += dt
    if Assets.spawnTimer >= Assets.nextSpawn:
        Assets.spawnTimer = 0.0
        Assets.nextSpawn = random.uniform(2.0, 4.0)
        if random.randint(0, 1) == 0:
            # Random choice for y value here is for the entity to be closer or further in the foreground.
            # Speed increases if further forward
            grass = Background.Grass(Assets.SCREEN_WIDTH + 10,
                                     Assets.SCREEN_HEIGHT - random.choice([50, 68]))
            Assets.sprite_list.add(grass)
        else:
            rock = Background.Rock(Assets.SCREEN_WIDTH + 10,
                                    Assets.SCREEN_HEIGHT - random.choice([50, 68]))
            Assets.sprite_list.add(rock)



def restart():
    '''Restarts the game. Fades in and out if you have enough lives, or if restarting from a gameover, simply starts you over from the beginning.'''
    if Assets.lives > 0:

        fade_in_or_out('spot', 1)

        Assets.lives -= 1
        Assets.eggs_stored = 10
        Assets.sprite_list.empty()
        player = Player(Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 4.17)
        
        Assets.sprite_list.add(player)

        fade_in_or_out('spot', 0)
        
    else:
        Assets.lives = 2
        Assets.score = 0
        Assets.eggs_stored = 10 
        Assets.sprite_list.empty()
        player = Player(Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 4.17)
        Assets.sprite_list.add(player)

    eggtext = font.render('Eggs:' + str(Assets.eggs_stored), True, (255, 241, 84), (0, 0, 0))
    eggtext = pg.transform.scale_by(eggtext, .5)
    eggtextRect = eggtext.get_rect()
    eggtextRect.center = (Assets.SCREEN_WIDTH / 2 + 22, Assets.SCREEN_HEIGHT - 16)
    
    pg.mixer.music.load(Assets.bgMusicPath)
    pg.mixer.music.play(-1)
    pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[0]))
    Assets.timer = 0
    pg.event.post(pg.event.Event(Assets.ENEMYSPAWN))

def fade_in_or_out(type = 'curtain', direction = 0, ending = False):
    ''' Direction = 1 means looping range is from (0, 6, 1), or 'in'. Direction = 0 means looping range is from (6, 0, -1), or 'out' '''
    
    dir = [0, 6, 1] if direction == 1 else [6, 0, -1]
    
    if type == 'curtain':
        for i in range (dir[0], dir[1], dir[2]):
            Assets.screen.fill("black")
            drawBackground()

            if direction == 1:
                Assets.sprite_list.draw(surface=Assets.screen)
            else:
                Assets.screen.blit(Assets.background[8], Assets.background[8].get_rect(center = (Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 2 - 20)))
                Assets.screen.blit(titletext, titletextRect)
            if ending:
                Assets.screen.blit(Assets.shed[0], Assets.shed[0].get_rect(topleft = (Assets.SCREEN_WIDTH / 2 + 30, Assets.SCREEN_HEIGHT - 170)))
                Assets.screen.blit(Assets.shed[1], Assets.shed[1].get_rect(topleft = (Assets.SCREEN_WIDTH / 2 + 70, Assets.SCREEN_HEIGHT - 170)))

            fadeout_rect1 = pg.Rect((-Assets.SCREEN_WIDTH/2) + ((Assets.SCREEN_WIDTH / 12) * i), 0, Assets.SCREEN_WIDTH/2, Assets.SCREEN_HEIGHT)
            fadeout_rect2 = pg.Rect(Assets.SCREEN_WIDTH - ((Assets.SCREEN_WIDTH / 12) * i), 0, Assets.SCREEN_WIDTH/2, Assets.SCREEN_HEIGHT)
            
            pg.draw.rect(Assets.screen, color=(0, 0, 0),
                            rect = fadeout_rect1)
            pg.draw.rect(Assets.screen, color=(0, 0, 0),
                            rect = fadeout_rect2)
            pg.display.flip()
            pg.display.update()
            time.sleep(.05)

    elif type == "spot":
        for i in range(dir[0], dir[1], dir[2]):
            Assets.screen.fill("black")
            drawBackground()
            Assets.sprite_list.draw(surface=Assets.screen)
            renderText()
            
            fadeout_rect = pg.Rect(0, 0, 160 + (160*i), 95 + (95*i))
            fadeout_rect.center = (Assets.SCREEN_WIDTH/2, Assets.SCREEN_HEIGHT/2)
            pg.draw.rect(Assets.screen, color=(0, 0, 0),
                            rect = fadeout_rect)
            pg.display.flip()
            pg.display.update()
            time.sleep(.03)



def gameOver():
    while Assets.click_to_start:
        Assets.dt = clock.tick(30) / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT:
                Assets.running = False
                Assets.click_to_start = False


        Assets.sprite_list.draw(surface=Assets.screen)
        Assets.screen.blit(Assets.background[7], Assets.background[7].get_rect(topleft = (0,0)))

        Assets.screen.blit(gameOvertext, gameOvertextrect)
        renderText()

        Assets.current_time += Assets.dt
        if Assets.current_time > Assets.animation_time:
            Assets.current_time = 0
            Assets.game_over_timer += Assets.dt
        
        
        if Assets.game_over_timer > 1.5:
            pg.mouse.set_cursor(pg.cursors.Cursor((0, 0), Assets.cursor_images[2]))
        else:
            pg.mouse.set_cursor(pg.cursors.Cursor((0, 0), Assets.cursor_images[1]))


        mouse_press = pg.mouse.get_pressed()
        key = pg.key.get_pressed()
        if (mouse_press[0] or key[pg.K_SPACE]) and Assets.game_over_timer > 1.5:
            Assets.click_to_start = False
            Assets.title_splash_running = True
            Assets.game_startup_timer = 0
            pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[1]))
            pg.mixer.Channel(1).play(pg.mixer.Sound(Assets.coinInsertAudioPath))

            fade_in_or_out("curtain", 1)
            startup_screen()
            restart()

        pg.event.pump() #updates events
        pg.display.update()
    

def drawBackground():
    '''Draws the background and runs the star animation. NOTE: You still need to draw the border of the screen (Assets.background[7]) in the main loop AFTER drawing your sprites, but BEFORE rendering the text. '''

    rect = Assets.background[Assets.bg_index % 6].get_rect(topleft = (0, 0))

    Assets.screen.blit(Assets.background[Assets.bg_index % 6], rect)

    Assets.current_time += Assets.dt
    if Assets.current_time >= Assets.animation_time:
        Assets.current_time = 0.0
        Assets.screen.blit(Assets.background[Assets.bg_index % 6], rect)
        Assets.bg_index += 1




def renderText():
    '''Renders and displays the text at the bottom of the screen: 1. Lives 2. Egg Count 3. Score'''
    eggtext = font.render('Eggs: ' + str(Assets.eggs_stored), True, (255, 241, 84), (0, 0, 0))
    scoretext = font.render('Score:' + str(Assets.score), True, (255, 241, 84), (0, 0, 0))
    eggtext = pg.transform.scale_by(eggtext, .6)
    scoretext = pg.transform.scale_by(scoretext, .6)

    
    scoretextRect = scoretext.get_rect()
    scoretextRect.center = (Assets.SCREEN_WIDTH - 100, Assets.SCREEN_HEIGHT - 16)
    eggtextRect = eggtext.get_rect()
    eggtextRect.center = (Assets.SCREEN_WIDTH / 2 + 22, Assets.SCREEN_HEIGHT - 16)
    
    Assets.screen.blit(eggtext, eggtextRect)
    Assets.screen.blit(scoretext, scoretextRect)
    if Assets.lives > 0:
        lives_image = Assets.lives_images[Assets.lives - 1]
        lives_image.get_rect()
        lives_image_rect.bottomleft = (25, Assets.SCREEN_HEIGHT - 6)
        Assets.screen.blit(lives_image, lives_image_rect)




def startup_screen():
    fade_in_or_out("curtain", 0)
    while Assets.title_splash_running:
        Assets.dt = clock.tick(30) / 1000
        Assets.game_startup_timer += Assets.dt
        if Assets.game_startup_timer > 5:
            Assets.title_splash_running = False
            pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[0]))
        Assets.screen.fill("black")

        
        drawBackground()
        Assets.screen.blit(Assets.background[8], Assets.background[8].get_rect(center = (Assets.SCREEN_WIDTH / 2, Assets.SCREEN_HEIGHT / 2 - 20)))
        Assets.screen.blit(Assets.background[7], Assets.background[7].get_rect(topleft = (0,0)))
        Assets.screen.blit(titletext, titletextRect)
        if Assets.hardMode:
            Assets.screen.blit(hardmode_text, hardmode_text_rect)

        pg.display.flip()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Assets.running = False
                Assets.title_splash_running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not Assets.hardMode:
                        Assets.hardMode = True
                        pg.mixer.Channel(2).play(pg.mixer.Sound(Assets.coinInsertAudioPath))
                    else:
                        Assets.hardMode = False
                        pg.mixer.Channel(2).play(pg.mixer.Sound(Assets.cornCollectAudioPath))
        pg.event.pump() #updates events
        pg.display.update()






def pulletSurprise():
    '''Ending Sequence'''
    Assets.score += (5 * Assets.eggs_stored)
    temp = Assets.sprite_list.sprites()[0]
    Assets.sprite_list.empty()
    Assets.sprite_list.add(temp)
    i = 0
    targets = [(Assets.SCREEN_WIDTH/ 2 - 30, Assets.SCREEN_HEIGHT - 115), (Assets.SCREEN_WIDTH / 2 + 95, Assets.SCREEN_HEIGHT - 115)]
    bacocks = Assets.bacock
    for i in range(3): bacocks.append(Assets.bacock[-1])
    bacock_index = 0

    pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[1]))
    Assets.sprite_list.sprites()[0].target = pg.math.Vector2(targets[0])
    Assets.sprite_list.sprites()[0].direction = Assets.sprite_list.sprites()[0].target - Assets.sprite_list.sprites()[0].pos
    finished_ending = False
    shed_in_place = False
    
    while not finished_ending:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Assets.running = False
                pg.quit()
                sys.exit()
        Assets.dt = clock.tick(30) / 1000
        Assets.screen.fill("black")
        drawBackground()
        renderText()
        Assets.screen.blit(Assets.shed[0], Assets.shed[0].get_rect(topleft = (Assets.SCREEN_WIDTH - i, Assets.SCREEN_HEIGHT - 170)))

        # SEQUENCE OF THE ENDING
        # First step: Move shed into place
        if not shed_in_place:
            i += 3
            if Assets.SCREEN_WIDTH - i <= Assets.SCREEN_WIDTH / 2 + 30:
                shed_in_place = True

        # Second step: Move player to front of shed
        # Third step: Move player inside shed
        elif targets: 
            current_target = targets[0]

            Assets.sprite_list.sprites()[0].pos.move_towards_ip(current_target, 2)
            if Assets.sprite_list.sprites()[0].pos == current_target:
                targets.pop(0)

        # Fourth step: Bacock!
        elif bacock_index < len(bacocks):
            Assets.screen.blit(bacocks[bacock_index], bacocks[bacock_index].get_rect(bottomleft = (Assets.SCREEN_WIDTH/2, Assets.SCREEN_HEIGHT/2)))
            time.sleep(.1)
            bacock_index += 1
            
            if bacock_index == len(bacocks):
                pg.mixer.music.set_volume(.3)
                pg.mixer.Channel(1).set_volume(.7)
                pg.mixer.Channel(1).play(pg.mixer.Sound(Assets.pulletSurpriseAudioPath))

        # Final step: Render congratulation text, and GG!
        else:
            pulletSurprise_bonus = font.render('5 X ' + str(Assets.eggs_stored) + ' eggs = ' + str(Assets.eggs_stored * 5) + ' bonus points', True, 'yellow', 'black')
            pulletSurprise_bonus = pg.transform.scale_by(pulletSurprise_bonus, .5)
            
            Assets.screen.blit(pulletSurprise_text1, pulletSurprise_text1_rect)
            Assets.screen.blit(pulletSurprise_text2, pulletSurprise_text2_rect)
            Assets.screen.blit(pulletSurprise_bonus, pulletSurprise_bonus_rect)
            
            pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[2]))

            mouse_press = pg.mouse.get_pressed()
            key = pg.key.get_pressed()
            if mouse_press[0] or key[pg.K_SPACE]:
                
                Assets.title_splash_running = True
                Assets.game_startup_timer = 0
                pg.mouse.set_cursor(pg.cursors.Cursor((13, 13), Assets.cursor_images[1]))
                pg.mixer.music.pause()
                pg.mixer.music.set_volume(.7)
                pg.mixer.Channel(1).play(pg.mixer.Sound(Assets.coinInsertAudioPath))
                Assets.screen.fill("black")
                
                fade_in_or_out("curtain", 1, True)
                
                Assets.score = 0
                Assets.lives = 0
                Assets.finished_ending = True
                
                startup_screen()
                restart()
                break
                
        # This is necessary to render the player sprite without using the update() function
        Assets.sprite_list.sprites()[0].rect.center = Assets.sprite_list.sprites()[0].pos
        Assets.sprite_list.sprites()[0].current_time += Assets.dt
        if Assets.sprite_list.sprites()[0].current_time >= Assets.sprite_list.sprites()[0].animation_time:
            Assets.sprite_list.sprites()[0].current_time = 0
            Assets.sprite_list.sprites()[0].index = (Assets.sprite_list.sprites()[0].index + 1) % 4
            Assets.sprite_list.sprites()[0].image = Assets.sprite_list.sprites()[0].images[Assets.sprite_list.sprites()[0].index + Assets.sprite_list.sprites()[0].fence_index]

        Assets.sprite_list.draw(surface=Assets.screen)

        Assets.screen.blit(Assets.shed[1], Assets.shed[1].get_rect(topleft = (Assets.SCREEN_WIDTH + 40 - i, Assets.SCREEN_HEIGHT - 170)))
        Assets.screen.blit(Assets.background[7], Assets.background[7].get_rect(topleft = (0,0)))
        renderText()
        
        pg.display.flip()
        pg.event.pump()
        pg.display.update()
    



def screenShake():
    '''Essentially a full copy of the standard rendering loop, but with all assets moving up and down rapidly. Can't use the standard functions because the movement needs to be changed semi-manually here.'''

    pg.mixer.Channel(0).play(pg.mixer.Sound(Assets.crashLandingAudioPath))
    for i in range(6):
        movement = -20 if i % 2 else 20 
        Assets.dt = clock.tick(30) / 1000
        Assets.screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Assets.running = False
                break
        
        rect = Assets.background[Assets.bg_index % 6].get_rect(topleft = (0, movement))
        
        Assets.screen.blit(Assets.background[Assets.bg_index % 6], rect)
        
        spawnBackgroundEntities(Assets.dt)
        
        for sprite in Assets.sprite_list.sprites(): 
            sprite.rect.move_ip(0, movement)
        Assets.sprite_list.draw(surface=Assets.screen)
        Assets.screen.blit(Assets.background[7], Assets.background[7].get_rect(topleft = (0, movement)))

        eggtext = font.render('Eggs: ' + str(Assets.eggs_stored), True, (255, 241, 84), (0, 0, 0))
        scoretext = font.render('Score:' + str(Assets.score), True, (255, 241, 84), (0, 0, 0))
        eggtext = pg.transform.scale_by(eggtext, .6)
        scoretext = pg.transform.scale_by(scoretext, .6)
        
            
        scoretextRect = scoretext.get_rect()
        scoretextRect.center = (Assets.SCREEN_WIDTH - 100, Assets.SCREEN_HEIGHT - 16 + movement)
        eggtextRect.center = (Assets.SCREEN_WIDTH / 2 + 22, Assets.SCREEN_HEIGHT - 16 + movement)
                
        Assets.screen.blit(eggtext, eggtextRect)
        Assets.screen.blit(scoretext, scoretextRect)
        if Assets.lives > 0:
            lives_image = Assets.lives_images[Assets.lives - 1]
            lives_image.get_rect()
            lives_image_rect.bottomleft = (25, Assets.SCREEN_HEIGHT - 6 + movement)
            Assets.screen.blit(lives_image, lives_image_rect)

        pg.display.flip()
        pg.event.pump() 
        pg.display.update()



async def main():
    '''Main game loop'''
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)


    startup_screen()

    if Assets.running:
        spawnEnemy(0)
        pg.mixer.music.play(loops = -1)
    
    paused = False
    while Assets.running:
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate
        # independent physics, should usually be 0.033
        Assets.dt = clock.tick(30) / 1000
        await asyncio.sleep(0)
        Assets.screen.fill("black")
        if not paused:
            Assets.timer += 1
        
        if Assets.timer >= 70 and Assets.hardMode:
            pg.event.post(pg.event.Event(Assets.ENEMYSPAWN))
            Assets.timer = 0
        elif Assets.timer >= 110 and not Assets.hardMode:
            pg.event.post(pg.event.Event(Assets.ENEMYSPAWN))
            Assets.timer = 0

    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Assets.running = False
            elif event.type == Assets.ENEMYSPAWN:
                if Assets.score < 300:
                    spawnEnemy(0)
                else:
                    pulletSurprise()
                if Assets.score >= 20 and random.randint(0, 1) == 1:
                    spawnEnemy(random.randint(-10, 60)) 
                
            elif event.type == Assets.DEATH_EVENT:
                restart()

            elif event.type == Assets.SCREEN_SHAKE:
                screenShake()
            elif event.type == Assets.GAME_OVER:
                Assets.click_to_start = True
                Assets.game_over_timer = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if paused:
                        paused = False
                        pg.mixer.music.unpause()
                    else:
                        paused = True
                        pg.mixer.music.pause()
                        pg.mixer.Channel(2).play(pg.mixer.Sound(Assets.coinInsertAudioPath))


        drawBackground()
            
        
        spawnBackgroundEntities(Assets.dt)

        if Assets.click_to_start:
            while Assets.click_to_start:
                if Assets.lives <= 0:
                    pg.mouse.set_cursor(pg.cursors.Cursor((0, 0), Assets.cursor_images[0]))
                    gameOver()
                else:
                    restart()

        # Runs the "update" function on every sprite in the list.
        # "update" does nothing if the sprite class doesn't have that function.
        # Essentially this is what the sprite is expected to do frame-by-frame.
        if not paused:
            Assets.sprite_list.update(Assets.dt)
        Assets.sprite_list.draw(surface=Assets.screen)

        # This is for rendering the border OVER the other sprites. The placement here is important.
        Assets.screen.blit(Assets.background[7], Assets.background[7].get_rect(topleft = (0,0)))

        renderText()

        # updates the display each loop
        pg.display.flip()
        pg.event.pump() #updates events
        pg.display.update()
    pg.quit()


asyncio.run(main())