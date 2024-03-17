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

Character1 = pygame.image.load('Dungeon Diver\Character.png')
Player = pygame.transform.scale(Character1,(96,96))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and PlayerX > -15:
        PlayerX -= 0.3

    if keys[pygame.K_d] and PlayerX < 710 :
        PlayerX += 0.3

    if keys[pygame.K_s] and PlayerY < 510:
        PlayerY += 0.3
    
    if keys[pygame.K_w] and PlayerY > -7 :
        PlayerY -= 0.3


    screen.fill((0, 0, 0))
    screen.blit(Player, (PlayerX,PlayerY))
    pygame.display.update()


pygame.quit()
quit()