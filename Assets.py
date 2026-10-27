import pygame as pg
import os, sys
from SpriteSheet import SpriteSheet

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



pg.init(), pg.mixer.init()

BASE_DIR = os.path.dirname(__file__)

# Establishes screen display variable. Will be initiated in main.py.
screen = 0

sprite_sheet = SpriteSheet(resource_path(os.path.join(BASE_DIR, "msastrochickenspritesheet2.png")))
background_sheet = SpriteSheet(resource_path(os.path.join(BASE_DIR, "background_stars_sheet.png")))


# Default Indices: 0 - 3
# Defeathered Indices: 4 -  11
# Exploded Indices: 12 - 16
# Fenced Indices: 17 - 20
# Kerfuffle Indices: 21 - 24
# Owl Kerfuffle Indices: 25 - 28
# Total length = 29
player1 = [sprite_sheet.parseSprite('msastrochicken_default_0.png'), sprite_sheet.parseSprite('msastrochicken_default_1.png'), 
          sprite_sheet.parseSprite('msastrochicken_default_2.png'), sprite_sheet.parseSprite('msastrochicken_default_3.png'), 
          sprite_sheet.parseSprite('msastrochicken_defeathered_0.png'), sprite_sheet.parseSprite('msastrochicken_defeathered_1.png'),
          sprite_sheet.parseSprite('msastrochicken_defeathered_2.png'), sprite_sheet.parseSprite('msastrochicken_defeathered_3.png'),
          sprite_sheet.parseSprite('msastrochicken_defeathered_4.png'), sprite_sheet.parseSprite('msastrochicken_defeathered_5.png'),
          sprite_sheet.parseSprite('msastrochicken_defeathered_6.png'), sprite_sheet.parseSprite('msastrochicken_defeathered_7.png'),
          sprite_sheet.parseSprite('msastrochicken_exploded_0.png'), sprite_sheet.parseSprite('msastrochicken_exploded_1.png'),
          sprite_sheet.parseSprite('msastrochicken_exploded_2.png'), sprite_sheet.parseSprite('msastrochicken_exploded_3.png'),
          sprite_sheet.parseSprite('msastrochicken_exploded_4.png'), sprite_sheet.parseSprite('msastrochicken_fenced_0.png'),
          sprite_sheet.parseSprite('msastrochicken_fenced_1.png'), sprite_sheet.parseSprite('msastrochicken_fenced_2.png'),
          sprite_sheet.parseSprite('msastrochicken_fenced_3.png'), sprite_sheet.parseSprite('msastrochicken_kerfuffle_0.png'),
          sprite_sheet.parseSprite('msastrochicken_kerfuffle_1.png'), sprite_sheet.parseSprite('msastrochicken_kerfuffle_2.png'),
          sprite_sheet.parseSprite('msastrochicken_kerfuffle_3.png'), sprite_sheet.parseSprite('owl_kerfuffle_0.png'),
          sprite_sheet.parseSprite('owl_kerfuffle_1.png'), sprite_sheet.parseSprite('owl_kerfuffle_2.png'),
          sprite_sheet.parseSprite('owl_kerfuffle_3.png'),]

egg = [sprite_sheet.parseSprite('egg_0.png'), sprite_sheet.parseSprite('egg_1.png'), sprite_sheet.parseSprite('egg_2.png'),
       sprite_sheet.parseSprite('egg_3.png'), sprite_sheet.parseSprite('egg_4.png'), sprite_sheet.parseSprite('egg_5.png'),
       sprite_sheet.parseSprite('egg_6.png'), sprite_sheet.parseSprite('egg_7.png'), sprite_sheet.parseSprite('egg_splat_0.png'),
       sprite_sheet.parseSprite('egg_splat_1.png'), sprite_sheet.parseSprite('egg_splat_2.png'), sprite_sheet.parseSprite('egg_splat_3.png'),
       sprite_sheet.parseSprite('egg_splat_4.png')]


farmer = [sprite_sheet.parseSprite('farmer-left.png'), sprite_sheet.parseSprite('farmer_topleft.png'),
          sprite_sheet.parseSprite('farmer_up_lefthand.png'), sprite_sheet.parseSprite('farmer_up_righthand.png'),
          sprite_sheet.parseSprite('farmer_topright.png'), sprite_sheet.parseSprite('farmer_right.png'),
          sprite_sheet.parseSprite('farmer_egged_0.png'), sprite_sheet.parseSprite('farmer_egged_1.png'),
          sprite_sheet.parseSprite('farmer_egged_2.png'), sprite_sheet.parseSprite('farmer_egged_3.png')]


windmill = [sprite_sheet.parseSprite('windmill_blades_0.png'), sprite_sheet.parseSprite('windmill_blades_1.png'),
            sprite_sheet.parseSprite('windmill_blades_2.png'), sprite_sheet.parseSprite('windmill_blades_3.png'),
            sprite_sheet.parseSprite('windmill_crash_0.png'), sprite_sheet.parseSprite('windmill_crash_1.png'),
            sprite_sheet.parseSprite('windmill_crash_2.png'), sprite_sheet.parseSprite('windmill_crash_3.png'),
            sprite_sheet.parseSprite('windmill_crash_4.png'), sprite_sheet.parseSprite('windmill_tower.png')]


dog = [sprite_sheet.parseSprite('dog_0.png'), sprite_sheet.parseSprite('dog_1.png'),
       sprite_sheet.parseSprite('dog_2.png'), sprite_sheet.parseSprite('dog_3.png'),
       sprite_sheet.parseSprite('dog_4.png'), sprite_sheet.parseSprite('dog_5.png'),
       sprite_sheet.parseSprite('dog_6.png'), sprite_sheet.parseSprite('dog_caught_0.png'),
       sprite_sheet.parseSprite('dog_caught_1.png'), sprite_sheet.parseSprite('dog_caught_2.png'), 
       sprite_sheet.parseSprite('dog_caught_3.png'), sprite_sheet.parseSprite('dog_caught_4.png'),
       sprite_sheet.parseSprite('dog_egged_0.png'), sprite_sheet.parseSprite('dog_egged_1.png'),
       sprite_sheet.parseSprite('dog_egged_2.png')]

bullet = [sprite_sheet.parseSprite('bullet.png')]

squirrel = [sprite_sheet.parseSprite('squirrel_0.png'), sprite_sheet.parseSprite('squirrel_1.png')]

cornstalk = [sprite_sheet.parseSprite('cornstalk_0.png'), sprite_sheet.parseSprite('cornstalk_1.png')]

fence = [sprite_sheet.parseSprite('fence_0.png'), sprite_sheet.parseSprite('fence_1.png')]

hill = [sprite_sheet.parseSprite('hill_0.png'), sprite_sheet.parseSprite('hill_1.png')]

grass = [sprite_sheet.parseSprite('grass.png')]

rock = [sprite_sheet.parseSprite('rock.png')]

mv_plane = [sprite_sheet.parseSprite("mv_plane_0.png"), sprite_sheet.parseSprite("mv_plane_1.png"),
            sprite_sheet.parseSprite("mv_plane_2.png"), sprite_sheet.parseSprite("mv_plane_prop_0.png")]

hat = [sprite_sheet.parseSprite("msastrochicken_hat_0.png"), sprite_sheet.parseSprite("msastrochicken_hat_1.png"), 
       sprite_sheet.parseSprite("msastrochicken_hat_2.png"), sprite_sheet.parseSprite("msastrochicken_hat_3.png"),
       sprite_sheet.parseSprite('egg_splat_0.png'), sprite_sheet.parseSprite('egg_splat_1.png'), 
       sprite_sheet.parseSprite('egg_splat_2.png'), sprite_sheet.parseSprite('egg_splat_3.png'),
       sprite_sheet.parseSprite('egg_splat_4.png')]

owl = [sprite_sheet.parseSprite("owl_0.png"), sprite_sheet.parseSprite("owl_1.png"),
       sprite_sheet.parseSprite("owl_2.png"), sprite_sheet.parseSprite("owl_3.png"),
       sprite_sheet.parseSprite("owl_dead_0.png"), sprite_sheet.parseSprite("owl_dead_1.png"), 
       sprite_sheet.parseSprite("owl_dead_2.png"), sprite_sheet.parseSprite("owl_dead_3.png"), 
       sprite_sheet.parseSprite("owl_tailspin_0.png"), sprite_sheet.parseSprite("owl_tailspin_1.png")]

bacock = [sprite_sheet.parseSprite("b.png"), sprite_sheet.parseSprite("ba.png"),
          sprite_sheet.parseSprite("bac.png"), sprite_sheet.parseSprite("baco.png"),
          sprite_sheet.parseSprite("bacoc.png"), sprite_sheet.parseSprite("bacock.png"),
          sprite_sheet.parseSprite("bacock!.png")]

lives_images = [sprite_sheet.parseSprite("extra_life_0.png"), sprite_sheet.parseSprite("extra_life_1.png")]

cursor_images = [sprite_sheet.parseSprite("ingamecursor_blue.png"), sprite_sheet.parseSprite("wait_icon.png"),
                 sprite_sheet.parseSprite("buckazoid.png")]

shed = [sprite_sheet.parseSprite("shed_0.png"), sprite_sheet.parseSprite("shed_1.png")]


# The sprites are small, everything needs to be scaled up! Uniformly, of course
SCALE_BY_FACTOR = 2

for i in range(len(player1)): player1[i] = pg.transform.scale_by(player1[i], factor=SCALE_BY_FACTOR)
for i in range(len(egg)): egg[i] = pg.transform.scale_by(egg[i], factor=SCALE_BY_FACTOR)
for i in range(len(farmer)): farmer[i] = pg.transform.scale_by(farmer[i], factor=SCALE_BY_FACTOR)
for i in range(len(windmill)): windmill[i] = pg.transform.scale_by(windmill[i], factor=SCALE_BY_FACTOR)
for i in range(len(dog)): dog[i] = pg.transform.scale_by(dog[i], factor=SCALE_BY_FACTOR)
for i in range(len(bullet)): bullet[i] = pg.transform.scale_by(bullet[i], factor=SCALE_BY_FACTOR)
for i in range(len(squirrel)): squirrel[i] = pg.transform.scale_by(squirrel[i], factor=SCALE_BY_FACTOR)
for i in range(len(cornstalk)): cornstalk[i] = pg.transform.scale_by(cornstalk[i], factor=SCALE_BY_FACTOR)
for i in range(len(fence)): fence[i] = pg.transform.scale_by(fence[i], factor=SCALE_BY_FACTOR)
for i in range(len(hill)): hill[i] = pg.transform.scale_by(hill[i], factor=SCALE_BY_FACTOR)
grass[0] = pg.transform.scale_by(grass[0], SCALE_BY_FACTOR)
rock[0] = pg.transform.scale_by(rock[0], SCALE_BY_FACTOR)
for i in range(len(mv_plane)): mv_plane[i] = pg.transform.scale_by(mv_plane[i], factor=SCALE_BY_FACTOR)
for i in range(len(hat)): hat[i] = pg.transform.scale_by(hat[i], factor=SCALE_BY_FACTOR)
for i in range(len(owl)): owl[i] = pg.transform.scale_by(owl[i], factor=SCALE_BY_FACTOR)
for i in range(len(bacock)): bacock[i] = pg.transform.scale_by(bacock[i], factor=SCALE_BY_FACTOR)
for i in range(len(lives_images)): lives_images[i] = pg.transform.scale_by(lives_images[i], factor=SCALE_BY_FACTOR)
for i in range(len(cursor_images)): cursor_images[i] = pg.transform.scale_by(cursor_images[i], factor=SCALE_BY_FACTOR)
for i in range(len(shed)): shed[i] = pg.transform.scale_by(shed[i], factor=SCALE_BY_FACTOR)

background = [background_sheet.parseSprite("background_stars_0.png"), background_sheet.parseSprite("background_stars_1.png"),
              background_sheet.parseSprite("background_stars_2.png"), background_sheet.parseSprite("background_stars_3.png"),
              background_sheet.parseSprite("background_stars_4.png"), background_sheet.parseSprite("background_stars_5.png"),
              background_sheet.parseSprite("background_stars_6.png"), background_sheet.parseSprite("background_border.png"),
              background_sheet.parseSprite("titlesplash.png"),]

for i in range(len(background)): background[i] = pg.transform.scale_by(background[i], factor=SCALE_BY_FACTOR)


ready_to_launch = True

sprite_list = pg.sprite.Group()

score = 0
lives = 2
eggs_stored = 10

animation_time = 0.10 #default = 0.10
current_time = 0.0
bg_index = 0

spawnTimer = 0.0
nextSpawn = 2.0

game_startup_timer = 0.0
game_over_timer = 0.0

title_splash_running = True
click_to_start = False
running = True
hardMode = False

# Delta Time. Used for measuring time passing, animations.
dt = 0

# Used to help spawnEnemies not spawn duplicates
last_enemy = 0

timer = 0

bgMusicPath = resource_path(os.path.join(BASE_DIR, "msastrochickenBGmusic.ogg"))
deathMusicPath = resource_path(os.path.join(BASE_DIR, "msastrochickendeath.ogg"))
launchaudioPath = resource_path(os.path.join(BASE_DIR, "launch.ogg"))
dogbarkaudioPath = resource_path(os.path.join(BASE_DIR, "dogbark.ogg"))
pulletSurpriseAudioPath = resource_path(os.path.join(BASE_DIR, "pulletsurprise.ogg"))
dogCatchAudioPath = resource_path(os.path.join(BASE_DIR, "dogcatch.ogg"))
gunshotAudioPath = resource_path(os.path.join(BASE_DIR, "gunshot.ogg"))
hitGroundAudioPath = resource_path(os.path.join(BASE_DIR, "hitGround.ogg"))
hitEnemyAudioPath = resource_path(os.path.join(BASE_DIR, "hitEnemy.ogg"))
coinInsertAudioPath = resource_path(os.path.join(BASE_DIR, "coinInsert.ogg"))
cornCollectAudioPath = resource_path(os.path.join(BASE_DIR, "collectCorn.ogg"))
crashLandingAudioPath = resource_path(os.path.join(BASE_DIR, "crashLanding.ogg"))
fenceShingAudioPath = resource_path(os.path.join(BASE_DIR, "fenceShing.ogg"))

fontPath = resource_path(os.path.join(BASE_DIR, "PrStart.ttf"))



ENEMYSPAWN = pg.USEREVENT + 1
DEATH_EVENT = pg.USEREVENT + 2
GAME_OVER = pg.USEREVENT + 3
SCREEN_SHAKE = pg.USEREVENT + 4

SCREEN_HEIGHT = 380 #380
SCREEN_WIDTH = 640 #640