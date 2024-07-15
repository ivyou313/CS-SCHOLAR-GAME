import pygame
from player import Player
from applw import Pong
from ground import Ground
from enemy import Enemy
import math
import pygame.mouse
from pgzrun import *
import random as random

# Ask what we should do for health bar like 3 lives or idk
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




player = Player()
#enemy = Enemy()
screenWidth = 500
screenHeight = 400
isFlor = False
ground = Ground()
cooldown = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
backGround = pygame.image.load('bg RESIZED.png')
backGround = pygame.transform.scale(backGround, (screenWidth, screenHeight))

allSprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
allSprites.add(ground)
allSprites.add(player)
xPlaces = [100, 400, 260, 300, 140]


pong = Pong(10,10)
last = pygame.time.get_ticks()
lastEnemy = pygame.time.get_ticks()

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
  if (now - lastEnemy >= 500) and len(enemies) <= 5:
      enemy = Enemy(random.randint(200,300), random.randint(150,200), random.choice(xPlaces))
      enemies.add(enemy)
      lastEnemy = pygame.time.get_ticks()

  if pygame.sprite.spritecollide(player, enemies, True):
      print(" Minus 1 health")
  if pygame.sprite.groupcollide(bullets, enemies, True, True):
      print(" End the squares")

  screen.blit(backGround, (0,0))

  bullets.update(player)
  enemies.update()


  if hasFloored:
      isFlor = True
  else:
      isFlor = False

  for sprite in allSprites:
            screen.blit(sprite.surf, sprite.rect)
  

  for en in enemies:
    screen.blit(en.surf, en.rect)
          
            

  player.update(playerkeys, isFlor)
 

  pygame.display.update()
 # while moving == True:
  # player.rect.x += 1
