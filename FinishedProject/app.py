from src.gamemanager import GameManager
from src.utils import *
from src.explosions import *
from src.collisions import *

def main():
    game = GameManager()
    SetExplosions()
    RetrieveScoreData(game)

    # Game Loop
    while game.running:
        if game.game_over:
            if game.score > game.top_score['score']:
                highscore_sound.play()
                print("New High Score!!")
            with open('player_scores.txt','w') as scores:
                json_obj = json.dumps(game.score_data,indent=4)
                scores.write(json_obj)
            game.reset()
            ShowTitleScreen(game)
            ConfigureSprites(game)

        #Updates the clock 60 Frames Per Second
        game.clock.tick(Config.FPS.value)         
        game.all_sprites.update()

        RenderGraphics(game)
        ProcessCollisions(game)
        ProcessEvents(game)

        game.all_sprites.draw(game.screen)
        pygame.display.flip()

    pygame.quit()
#If this module is executing the script 
#the global variable __name__ gets set to __main__
if __name__ == "__main__":
    main()
