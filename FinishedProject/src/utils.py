from sys import exit
from src.gamemanager import *
from src.mob import *
from src.player import *
from src.enemy import *
import json

def ShowTitleScreen(game:GameManager):
    background = game.background[Config.SURFACE.value]
    rect = game.background[Config.RECT.value]
    game.screen.blit(background,rect)
    game.DrawUIText(Config.TITLE.value,64,Config.SCREEN_WIDTH.value / 2, Config.SCREEN_HEIGHT.value / 4)
    game.DrawUIText(Config.CONTROLS.value,22,Config.SCREEN_WIDTH.value / 2,Config.SCREEN_HEIGHT.value / 2)
    game.DrawUIText(Config.INSTRUCTIONS.value,18, Config.SCREEN_WIDTH.value / 2, Config.SCREEN_HEIGHT.value * 3 / 4)
    pygame.display.flip()
    game.waiting = True
    while game.waiting:
        game.clock.tick(Config.FPS.value)
        keystate = keystate = pygame.key.get_pressed()
        for _ in pygame.event.get():
            if keystate[pygame.K_ESCAPE]:
                pygame.quit()
                exit()
            if keystate[pygame.K_RETURN]:
                game.waiting = False

def ConfigureSprites(game:GameManager):
    """Initialize Sprite Groups"""
    #Sprite Objects
    game.all_sprites = pygame.sprite.Group()
    game.mob_group = pygame.sprite.Group()
    game.bullet_group = pygame.sprite.Group()
    game.enemy_group = pygame.sprite.Group()
    game.power_group = pygame.sprite.Group()
    game.player = Player(game)
    
    for _ in range(game.mob_size):
        SpawnMob(game)
    
    for _ in range(game.fireteam):
        SpawnFireTeam(game)

    game.all_sprites.add(game.bullet_group)
    game.all_sprites.add(game.player)

def ProcessEvents(game:GameManager):
    """Handles events and user input
    Returns false when user quits"""
    key = pygame.key.get_pressed()
    game.score_data[game.user] = game.score
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            if game.score > game.top_score['score']:
                game.top_score['user'] = game.user
                game.top_score['score'] = game.score
            game.running = False
            pygame.quit()
            exit()

def RenderGraphics(game:GameManager):
        """Update the full display Surface to the screen after drawing everything"""

        ScrollBackground(game)

        game.all_sprites.draw(game.screen)

        game.DrawUIText(str(game.score),18,Config.SCREEN_WIDTH.value / 2, 10)
        game.DrawHealthBar(5,5,game.player.shield)
        game.DrawLives(Config.SCREEN_WIDTH.value - 100,5,game.player.lives)

        pygame.display.flip()

def ScrollBackground(game:GameManager):
    """Scroll the Background image vertically"""
    #This explicit declaration is required to remind us that we are actually modifying
    #the value of the variable in the outer scope
    x1 = game.x1
    x2 = game.x2
    y1 = game.y1
    y2 = game.y2
    background_surface = game.background[Config.SURFACE.value]
    rect = game.background[Config.RECT.value]
    
    game.screen.blit(background_surface,rect)

    game.y2 += 10
    game.y1 += 10
    
    game.screen.blit(background_surface,(x1,y1))
    game.screen.blit(background_surface,(x2,y2))
    
    if y1 > Config.SCREEN_HEIGHT.value:
        game.y1 = -Config.SCREEN_HEIGHT.value
    if y2 > Config.SCREEN_HEIGHT.value:
        game.y2 = -Config.SCREEN_HEIGHT.value

def RetrieveScoreData(game:GameManager):
    try:
        with open('player_scores.txt') as scores:
            old_scores = json.load(scores)
            highscore = game.score
            user = game.user
            for k in old_scores.keys():
                game.score_data[k] = old_scores[k]
                if old_scores[k] > highscore:
                    highscore = old_scores[k]
                    user = k
            game.top_score['user'] = user
            game.top_score['score'] = highscore
    except:
        game.top_score['user'] = game.user
        game.top_score['score'] = game.score
        print("Creating for first time")