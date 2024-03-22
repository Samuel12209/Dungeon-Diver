import pygame
import time
pygame.init()

PlayerY = 50
PlayerX = 50

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('Dungeon Diver\Dungeon Diver.png')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_caption("DungeonDiver")
pygame.display.set_icon(icon)
dungeonload = pygame.image.load('Dungeon Diver\Dungeon.jpg')
dungeon = pygame.Surface((600, 600))
Character1 = pygame.image.load('Dungeon Diver\Character.png')
Player = pygame.transform.scale(Character1,(96,96))



running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and PlayerX > -15:
        PlayerX -= 0.1

    if keys[pygame.K_d] and PlayerX < 460 :
        PlayerX += 0.1

    if keys[pygame.K_s] and PlayerY < 380:
        PlayerY += 0.1
    
    if keys[pygame.K_w] and PlayerY > -10 :
        PlayerY -= 0.1


    screen.blit(dungeon, (0,0))
    screen.blit(Player, (PlayerX,PlayerY))
  

    pygame.display.update()


pygame.quit()
quit()