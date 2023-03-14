import pygame
from src.constants import *
from enum import Enum

pygame.mixer.init()
audio_dir = Directories.AUDIO_DIR.value
laser = AudioFiles.LASER.value
shield = AudioFiles.SHIELD.value
gun = AudioFiles.GUN.value
explosion = AudioFiles.EXPLOSION.value
player = AudioFiles.PLAYER_DEATH.value
highscore = AudioFiles.HIGHSCORE.value

shoot_sound = pygame.mixer.Sound(path.join(audio_dir,laser))
shield_sound = pygame.mixer.Sound(path.join(audio_dir,shield))
powerup_sound = pygame.mixer.Sound(path.join(audio_dir,gun))
explosion = pygame.mixer.Sound(path.join(audio_dir,explosion))
player_die_sound = pygame.mixer.Sound(path.join(audio_dir,player))
highscore_sound = pygame.mixer.Sound(path.join(audio_dir,highscore))
shoot_sound.set_volume(0.5)

def LoadAudio():
    pygame.mixer.music.load(path.join(audio_dir,AudioFiles.BACKGROUND_MUSIC.value))
    # Include in pygame.__init__ to address module import error os.add_dll_directory(pygame_dir)
    #https://github.com/pygame/pygame/issues/2647
    pygame.mixer.music.play(loops = -1)