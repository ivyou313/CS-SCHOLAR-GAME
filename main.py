import pygame
from player import Player
from applw import Pong
from ground import Ground
import math
import pygame.mouse 
from pgzrun import *


from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_SPACE,
  QUIT 

)

pygame.init()
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 600

X0 = WIDTH // 2
Y0 = HEIGHT // 2

COUNT_CIRCLES = 100                     # Total number of circles in the tunnel
STEP_RADIUS = 10                         # Space between circles
STEP_COLOR = (255-50) / COUNT_CIRCLES    # Brightness of the circles? 

# a list containing ellipses, each element of this list is also
# list of numbers representing center coordinates, radius and tint:
# [X, Y, RADIUS, COLOR]
сircles = []




screen = pygame.display.set_mode((500, 400))
player = Player()
screenWidth = 400
screenHeight = 300
isFlor = False
ground = Ground()
cooldown = 400

allSprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
allSprites.add(ground)
allSprites.add(player)

pong = Pong(10,10)
last = pygame.time.get_ticks()


while True:
  clock.tick(60)
  screen.fill((255,255,255))
  playerkeys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()

  playerkeys = pygame.key.get_pressed()
  hasFloored = pygame.sprite.collide_rect(player, ground)

  now = pygame.time.get_ticks()
  if (now - last >= cooldown) and playerkeys[K_SPACE]:
    pong = Pong(player.rect.x - 5, player.rect.y + 10)
    allSprites.add(pong)
    bullets.add(pong)
    last = pygame.time.get_ticks()


  bullets.update()


  if hasFloored:
      isFlor = True
  else:
      isFlor = False

  for sprite in allSprites:
            screen.blit(sprite.surf, sprite.rect)
            

  player.update(playerkeys, isFlor)
 

  pygame.display.update()
 # while moving == True:
  # player.rect.x += 1
