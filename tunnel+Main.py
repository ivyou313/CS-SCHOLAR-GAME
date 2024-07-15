import pygame
from player import Player
from applw import Pong
from ground import Ground
# from enemy import Enemy
import math
import pygame.mouse 
from pgzrun import *
import random as random


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
cooldown = 400
screen = pygame.display.set_mode((screenWidth, screenHeight))
# backGround = pygame.image.load('bg RESIZED.png')
# backGround = pygame.transform.scale(backGround, (screenWidth, screenHeight))

allSprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
allSprites.add(ground)
allSprites.add(player)
xPlaces = [100, 400, 260, 300, 140]

width = 500
height = 400
x0 = width//2
y0 = height//2

circleCount = 100
radiusDiff = 10
stepCol = (255-50)/circleCount

circles = []

for i in range(circleCount):
  circles.append([x0, y0, 100, 50])

def draw_circle(circle):
  angle = 0                   # Angle of movement along the ellipse to draw the next point.
  step = math.pi / 100    # Step with which the points of the ellipse are drawn.

  circle_x = circle[0]
  circle_y = circle[1]
  circle_r = circle[2]
  circle_color = circle[3]

  while angle < math.pi * 2:
      x = round(circle_x + math.sin(angle) * circle_r)
      y = round(circle_y + math.cos(angle) * circle_r // 1.5)

      if 0 < x < width and 0 < y < height:
          pygame.draw.circle(screen,(0, circle_color, circle_color), (x,y), 2)

      angle += step

global rotAngle
rotAngle = 0

pong = Pong(10,10)
last = pygame.time.get_ticks()
# lastEnemy = pygame.time.get_ticks()

while True:
  screen.fill((74, 170, 100))

  for i in range(len(circles) - 2, -1, -1):
      circle = circles[i]

      circle[2] += radiusDiff
      circle[3] += stepCol
      circles[i + 1] = circle

      draw_circle(circle)

  # Calculating X, Y coordinates for a new circle (Changes how much the tunnel rorates)
  rotAngle += 0.05
  x = x0 + math.sin(rotAngle) * 1.0
  y = y0 + math.cos(rotAngle) * 1.0

  # Add a new circle to the beginning of the list
  circles[0] = [x, y, 100, 50]

  clock.tick(60)
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
  # if (now - lastEnemy >= 500) and len(enemies) <= 5:
  #     enemy = Enemy(random.randint(200,300), random.randint(150,200), random.choice(xPlaces))
  #     enemies.add(enemy)
  #     lastEnemy = pygame.time.get_ticks()

  if pygame.sprite.spritecollide(player, enemies, True):
      print(" Minus 1 health")

  # screen.blit(backGround, (0,0))

  bullets.update(player)
  # enemies.update(lastEnemy)


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