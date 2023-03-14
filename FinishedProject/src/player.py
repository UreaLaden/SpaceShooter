from src.gamemanager import *
from src.bullets import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,game:GameManager):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load(Directories.PLAYER_IMG.value),(80,48))
        self.image.set_colorkey(Colors.BLACK.value) #Any pixels with the same color will be transparent
        self.rect = self.image.get_rect()
        self.radius = Config.PLAYER_RADIUS.value
        self.rect.centerx = Config.SCREEN_WIDTH.value / 2
        self.rect.bottom = Config.SCREEN_HEIGHT.value - 10
        self.speedx = 0
       
        self.shield = 100
        self.lives = 3
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.power = 1
        self.hide_time = pygame.time.get_ticks()
        self.hidden = False

    def update(self):
        #timeout of powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > Config.POWERUP_TIME.value:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        #Unhide if hidden   
        if self.hidden and pygame.time.get_ticks() - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = Config.SCREEN_WIDTH.value / 2
            self.rect.bottom = Config.SCREEN_HEIGHT.value - 10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -9.5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 9.5
        if keystate[pygame.K_SPACE]:
            self.shoot()   
        
        self.rect.x += self.speedx

        # Keep sprite on screen
        if self.rect.right > Config.SCREEN_WIDTH.value:
            self.rect.right = Config.SCREEN_WIDTH.value
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                SpawnBullet(self.game,self.rect.centerx,self.rect.centery)
            if self.power >= 2:
                SpawnBullet(self.game,self.rect.left,self.rect.centery)
                SpawnBullet(self.game,self.rect.right,self.rect.centery)

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (Config.SCREEN_WIDTH.value / 2, Config.SCREEN_HEIGHT.value + 200)
    
    def die(self):
        self.hide()
        self.lives -= 1
        self.shield = 100

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def heal(self):
        self.shield += random.randrange(10,30)
        if self.shield >= 100:
            self.shield = 100

    