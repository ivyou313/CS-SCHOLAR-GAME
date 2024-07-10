import pygame
import pygame.gfxdraw
from applw import Pong

from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_SPACE,
  QUIT
)
screenWidth = 400
screenHeight = 300
snakeWidth = 40
speed = 7


#Player
class Player( pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.Surface((snakeWidth, 40), pygame.SRCALPHA)
    #self.surf.fill((18, 107, 4))
    pygame.gfxdraw.filled_circle(self.surf, 20, 20, 18, (245, 154, 178))
    #pygame.gfxdraw.aacircle(self.surf, 20, 20, 18, (0,0,0))
   # pygame.gfxdraw.filled_circle(self.surf, 15, 15, 14, (144, 10, 100)) pygame.SRCALPHA

    
    self.rect = self.surf.get_rect(center=(480,100))
    self.yOffset = 0
    self.gravity = 1


  # Player movement
  def update(self, playerkeys, isFlor):
   # self.isGrounded = pygame.sprite.spritecollideany(self,group)

    if isFlor == True:
      self.yOffset = 0
      if playerkeys[K_UP]:
        self.yOffset = -18
    else:
      self.yOffset += 1 
      
    

      # self.yOffset = self.yOffset + self.gravity

    self.rect.move_ip((0, self.yOffset))

    #elif playerkeys[K_DOWN] and self.rect.y < 382:
     #self.rect.move_ip(0,7)
    if playerkeys[K_LEFT] and self.rect.x >0:
     self.rect.move_ip(-7,0) 
    elif playerkeys[K_RIGHT] and self.rect.x < 483:
     self.rect.move_ip(7,0)

  def createBull(self):
      
         return Pong(self.rect.x, self.rect.y)

  