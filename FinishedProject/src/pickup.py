from os import listdir,path
import pygame
import random
from src.constants import *

def GetPickups():
    pickups = {}
    pickup_dir = path.join(Directories.IMG_DIR.value,Directories.PICKUPS.value)

    gun_img = pygame.image.load(path.join(pickup_dir,SpriteImages.BOLT.value)).convert()
    shield_img = pygame.image.load(path.join(pickup_dir,SpriteImages.SHIELD.value)).convert()

    pickups[CollisionTypes.GUN.value] = gun_img
    pickups[CollisionTypes.SHIELD.value] = shield_img

    return pickups

def PickupTypes():
    pickups = [CollisionTypes.SHIELD.value,CollisionTypes.GUN.value]
    return pickups

class Pickup(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(PickupTypes())
        self.image = GetPickups()[self.type]
        self.image.set_colorkey(Colors.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        #kill if it moves off the top of the screen
        if self.rect.top > Config.SCREEN_HEIGHT.value:
            self.kill()
