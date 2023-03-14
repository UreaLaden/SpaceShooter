import pygame
from os import path
from src.constants import *
from src.gamemanager import *
from src.soundeffects import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(Directories.IMG_DIR.value,SpriteImages.LASER.value))
        self.image.set_colorkey(Colors.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

def SpawnBullet(game:GameManager,x:int,y:int):
    """Spawns a bullet at position (x,y)"""
    bullet = Bullet(x,y)
    game.all_sprites.add(bullet)
    game.bullet_group.add(bullet)
    shoot_sound.play()

