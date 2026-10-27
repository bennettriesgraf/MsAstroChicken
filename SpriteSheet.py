import pygame as pg
import json

class SpriteSheet:
    '''Parses through given spritesheet. Needs matching .json file with locations to work.'''
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename)
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def getSprite(self, x, y, w, h):
        sprite = pg.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite


    def parseSprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.getSprite(x, y, w, h)
        return image


