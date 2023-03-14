from src.gamemanager import *

explosion_anim = {}
explosion_anim[ExplosionClass.LARGE.value] = []
explosion_anim[ExplosionClass.SMALL.value] = []
explosion_anim[ExplosionClass.PLAYER.value] = []

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 25

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def SetExplosions():
    """Gather all of the explosion images into a dictionary for reference later"""
    global explosion_anim

    for i in range(24):
        filename = 'expl_01_{}.png'.format(i)
        img = pygame.image.load(path.join(Directories.IMG_DIR.value,Directories.EXPLOSIONS.value,filename)).convert()
        img.set_colorkey(Colors.BLACK.value)

        img_lg = pygame.transform.scale(img,(75,75))
        img_sm = pygame.transform.scale(img,(32,32))

        explosion_anim[ExplosionClass.LARGE.value].append(img_lg)
        explosion_anim[ExplosionClass.SMALL.value].append(img_sm)

        #player explosion images same 24
        filename = 'expl_10_00{}.png'.format(i)
        img = pygame.image.load(path.join(Directories.IMG_DIR.value,Directories.EXPLOSIONS.value,filename)).convert()
        img.set_colorkey(Colors.BLACK.value)
        explosion_anim[ExplosionClass.PLAYER.value].append(img)
