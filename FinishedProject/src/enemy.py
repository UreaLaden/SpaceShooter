from src.gamemanager import *
import random
from os import listdir

def GetEnemies() -> pygame.Surface:
    """Take all of our alien images to a list for later"""
    enemy_dir = path.join(Directories.IMG_DIR.value,Directories.ENEMIES.value)
    enemy_list = listdir(enemy_dir)
    enemies = []
    for img in enemy_list:
        enemies.append(pygame.image.load(path.join(enemy_dir,img)).convert())
    return enemies

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(GetEnemies()),(100,60))
        self.image.set_colorkey(Colors.WHITE.value)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(Config.SCREEN_WIDTH.value - self.rect.width)
        self.rect.y = random.randrange(-200,-40)
        self.speedy = random.randrange(1,13)
        self.speedx = random.randrange(-3,3)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (
            (self.rect.top > Config.SCREEN_HEIGHT.value + 10) or 
            (self.rect.left < -25) or 
            (self.rect.right > Config.SCREEN_WIDTH.value + 20)
            ):
            self.rect.x = random.randrange(Config.SCREEN_WIDTH.value - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(1,10)

def SpawnFireTeam(game:GameManager):
    """Instantiate a new Meteor Mob and add to Sprite group and Mob group"""
    e = Enemy()
    game.all_sprites.add(e)
    game.enemy_group.add(e)
