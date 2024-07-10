import pygame
from player import Player
from applw import Pong
from ground import Ground


from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_SPACE,
  QUIT 

)

pygame.init()

screen = pygame.display.set_mode((500, 400))
player = Player()
screenWidth = 400
screenHeight = 300
#pong = Pong()
isFlor = False
ground = Ground()
shootAgain = pygame.USEREVENT + 1
bulletShot = pygame.USEREVENT + 2
deez = True

allSprites = pygame.sprite.Group()
#bullets = pygame.sprite.Group()
allSprites.add(ground)
allSprites.add(player)
#allSprites.add(pong)





clock = pygame.time.Clock()

moving = False
speed = 7


while True:
  clock.tick(60)
  screen.fill((255,255,255))
  playerkeys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
    if event.type == shootAgain:
        deez = True
    elif event.type == bulletShot:
        deez = False
    

    
    # if event.type == playerkeys[K_SPACE]:
    #    screen.blit(pong.surf, (pong.rect))
       


  

#  if player.rect.colliderect(pong.rect):
  #  pong.rect.move_ip(-100,-10)
    #pong.rect.y =- speed
    



  playerkeys = pygame.key.get_pressed()
  hasFloored = pygame.sprite.collide_rect(player, ground)
  if deez == True and playerkeys[K_SPACE]:
    allSprites.add(player.createBull())
    pygame.time.set_timer(bulletShot, 100)
  else:
    pygame.time.set_timer(shootAgain, 100)

  if hasFloored:
      isFlor = True
  else:
      isFlor = False

  
  #screen.blit(ground.surf, (ground.rect))
 # screen.blit(player.surf, (player.rect))
  for sprite in allSprites:
            screen.blit(sprite.surf, sprite.rect)
  
  #screen.blit(player.surf, (player.rect))

  player.update(playerkeys, isFlor)
  
  #player.movement()
  #player.move(moving, playerkeys)

    


 # player.rect.x += 4




  #player.rect.x += 1
 


    


  pygame.display.update()
 # while moving == True:
  # player.rect.x += 1
