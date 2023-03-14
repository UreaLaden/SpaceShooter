import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("ARC SURVIVAL")
screen = pygame.display.set_mode((480,600))

while True:
    key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    
    pygame.time.Clock().tick(60)