import pygame
import time

pygame.init()

PlayerY = 50
PlayerX = 50
PlayerWidth = 96
PlayerHeight = 96

WIDTH, HEIGHT = 620, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.image.load('Dungeon Diver\Dungeon Diver.png')
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_caption("DungeonDiver")
pygame.display.set_icon(icon)

dungeonload = pygame.image.load('Dungeon Diver\Dungeon.jpg').convert()
dungeonload = pygame.transform.scale(dungeonload, (650, 600))

Character1 = pygame.image.load('Dungeon Diver\Character.png')
Player = pygame.transform.scale(Character1, (96, 96))


obstacle2 = pygame.Rect(0, 250, 190, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(0.001)

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0
    if keys[pygame.K_a] and PlayerX > 0:
        Character1 = pygame.image.load('Dungeon Diver\Characterleft.png')
        dx -= 2
    if keys[pygame.K_d] and PlayerX < 500:
        Character1 = pygame.image.load('Dungeon Diver\Character.png')
        dx += 2
    if keys[pygame.K_s] and PlayerY < 380:
        dy += 0.5
    if keys[pygame.K_w] and PlayerY > 25:
        dy -= 0.5
    
    if keys[pygame.K_]

    new_player_rect = pygame.Rect(PlayerX + dx, PlayerY + dy, PlayerWidth, PlayerHeight)
    if not new_player_rect.colliderect(obstacle2) and not new_player_rect.colliderect(obstacle2):

        PlayerX += dx
        PlayerY += dy
    
    Player = pygame.transform.scale(Character1, (96, 96))
    screen.blit(dungeonload, (-30, -50))
    screen.blit(Player, (PlayerX, PlayerY))

    pygame.display.update()

pygame.quit()
quit()