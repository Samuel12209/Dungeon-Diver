import pygame
import time

pygame.init()

PlayerY = 50
PlayerX = 50
PlayerWidth = 96
PlayerHeight = 96

WIDTH, HEIGHT = 620, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.image.load('Dungeon Diver\\assets\\Dungeon Diver.png')
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_caption("DungeonDiver")
pygame.display.set_icon(icon)

dungeonload = pygame.image.load('Dungeon Diver\\assets\\Dungeon.jpg').convert()
dungeonload = pygame.transform.scale(dungeonload, (650, 550))

Character1 = pygame.image.load('Dungeon Diver\\assets\\Character.png')
Player = pygame.transform.scale(Character1, (96, 96))

knight = pygame.image.load('Dungeon Diver\\assets\\Knight.png')
pygame.transform.scale(knight,(64,64))

obstacle2 = pygame.Rect(0, 250, 190, 20)
knight1 = pygame.Rect(267, 308, 315, 362)

slash_frames = [
    pygame.image.load(f'Dungeon Diver\\assets\\pixil-frame-{i}.png').convert_alpha() for i in range(3)
]
slash_frames2 = [
    pygame.image.load(f'Dungeon Diver\\assets\\pixil-frame-{i}-left.png').convert_alpha()
    for i in range(3)
]
health = 100

def slash():
  if facing == "Right":
    for frame in slash_frames:
      screen.blit(dungeonload, (-30, -50))
      screen.blit(Player, (PlayerX, PlayerY))
      screen.blit(frame, (PlayerX + 50, PlayerY))
      time.sleep(0.1)
      pygame.display.update()

  if facing == "Left":
    for frame in slash_frames2:
      screen.blit(dungeonload, (-30, -50))
      screen.blit(Player, (PlayerX, PlayerY))
      screen.blit(frame, (PlayerX - 670, PlayerY - 260))
      time.sleep(0.1)
      pygame.display.update()
fps = pygame.time.Clock()

running = True
while running:
  fps.tick(20)
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      slash()
      print("slash")
      x, y = pygame.mouse.get_pos()
      print(x, y)
    if event.type == pygame.QUIT:
      running = False
  time.sleep(0.001)
  facing = "middle"
  keys = pygame.key.get_pressed()

  dx, dy = 0, 0
  if keys[pygame.K_a] and PlayerX > 0:
    Character1 = pygame.image.load('Dungeon Diver\\assets\\Characterleft.png')
    facing = "Left"
    dx -= 4
  if keys[pygame.K_d] and PlayerX < 500:
    Character1 = pygame.image.load('Dungeon Diver\\assets\\Character.png')
    facing = "Right"
    dx += 4
  if keys[pygame.K_s] and PlayerY < 380:
    dy += 2
  if keys[pygame.K_w] and PlayerY > 25:
    dy -= 2

  new_player_rect = pygame.Rect(PlayerX + dx, PlayerY + dy, PlayerWidth,
                                PlayerHeight)
  if not new_player_rect.colliderect(
      obstacle2) and not new_player_rect.colliderect(obstacle2):
    PlayerX += dx
    PlayerY += dy

    
  if knight1.colliderect(new_player_rect):
    health -= 5
    print("Hit! -5 hp")
    print(str(health) + "Left!")
    if health <= 0:
      print("You died!")
  if health <= 0: 
    deathscreen = pygame.image.load('Dungeon Diver\\assets\\You died!.png')
    pygame.transform.scale(deathscreen,(WIDTH, HEIGHT))
    screen.blit(deathscreen, (0, 0))
    pygame.display.update()
    time.sleep(10)
    running = False


  Player = pygame.transform.smoothscale(Character1, (96, 96))
  screen.blit(dungeonload, (-30, -50))
  screen.blit(knight, (knight1x, knight1y))
  screen.blit(Player, (PlayerX, PlayerY))
  pygame.display.update()

pygame.quit()
quit()