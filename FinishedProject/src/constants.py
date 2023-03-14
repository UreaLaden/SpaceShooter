from os import path
from enum import Enum

class Colors(Enum):
    """Contains Colors stored as tuples (R,G,B)"""
    WHITE:tuple[int,int,int] = (255,255,255)
    BLACK:tuple[int,int,int] = (0,0,0)
    RED:tuple[int,int,int] = (255,0,0)
    GREEN:tuple[int,int,int] = (0,255,0)
    BLUE:tuple[int,int,int] = (0,0,255)
    YELLOW:tuple[int,int,int] = (255,255,0)

class Config(Enum):
    """Contains all configuration and setup variables"""
    TITLE:str = 'ARC SURVIVAL 2.0'
    CONTROLS:str = 'Use the Arrow keys to move and Space Bar to fire'
    INSTRUCTIONS:str = 'Press Return key to begin or Escape to Exit'
    USER_PROMPT:str = "What's your name pilot? "
    SURFACE:str = 'surface'
    RECT:str = 'rect'
    FONT:str = 'arial'
    FPS:int = 60
    SCREEN_HEIGHT:int = 600
    SCREEN_WIDTH:int = 480

    PLAYER_HEIGHT:int = 80
    PLAYER_WIDTH:int = 48
    PLAYER_RADIUS:int = 20
    POWERUP_TIME:int = 5000
    MOB_SIZE:int = 8
    FIRE_TEAM_SIZE:int = 3
    BAR_LENGTH:int = 100
    BAR_HEIGHT:int = 10    
    DROP_CHANCE:float = 0.1
    SHOT_VOLUME:float = 0.5

class AudioFiles(Enum):
    """Contains the names of all audio files"""
    LASER:str = 'Laser1.wav'
    SHIELD:str = 'shieldPowerup.wav'
    GUN:str = 'gunPowerup.wav'
    EXPLOSION:str = 'Explosion2.wav'
    PLAYER_DEATH:str = 'playerExplosion.wav'
    BACKGROUND_MUSIC:str = 'Orbital Colossus.mp3'
    HIGHSCORE:str = 'highscore.wav'

class SpriteImages(Enum):
    BOLT:str = 'bolt_gold.png'
    SHIELD:str = 'shield_gold.png'
    LASER:str = 'laserRed16.png'

class CollisionTypes(Enum):
    """Contains the names of all pickups"""
    SHIELD:str = 'shield'
    GUN:str = 'gun'

class ExplosionClass(Enum):
    """Contains the different types of explosions"""
    SMALL:str = 'sm'
    LARGE:str = 'lg'
    PLAYER:str = 'player'

class Directories(Enum):
    """Contains File Directory and Folder strings"""
    CURRENT_FILE_DIR:str = path.dirname(__file__)
    ROOT_DIR:str = path.realpath(path.join(CURRENT_FILE_DIR,'..'))
    IMG_DIR:str = path.join(ROOT_DIR,'assets','img')
    AUDIO_DIR:str = path.join(ROOT_DIR,'assets','audio')
    PLAYER_IMG:str = path.join(IMG_DIR,'player_ship.png')
    ASSETS:str = 'assets'
    AUDIO:str = 'audio'
    IMAGE:str = 'img'
    ENEMIES:str = 'Enemies'
    METEORS:str = 'Meteors'
    PICKUPS:str = 'Pickups'
    EXPLOSIONS:str = 'Explosions'


