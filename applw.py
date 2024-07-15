import pygame
import math
import pygame.gfxdraw
#from player import Player


speed = 7
width = 20


class Pong(pygame.sprite.Sprite):
  def __init__(self, xpos, ypos):
    super(Pong, self).__init__()
    self.x = 7
    self.surf = pygame.Surface((width, width), pygame.SRCALPHA)
    pygame.gfxdraw.filled_circle(self.surf, round(width/2), round(width/2),round((width/2)-2), (255, 183, 28))
   # self.surf.fill((255, 183, 28))
    self.rect = self.surf.get_rect(center=(xpos+30, ypos-20))

  def update(self, player):
  
          
        
          dx, dy = 260 - self.rect.x, 200 - self.rect.y
          dist = math.hypot(dx, dy)
          if round(dist) > 1:
            dx, dy = dx / dist, dy / dist  # Normalize.
            # Move along this normalized vector towards the player at current speed.
            self.x = self.x *0.5
            self.rect.x += dx * 2
            self.rect.y += dy * 2
            pygame.transform.scale(self.surf, (self.x, self.x))
            # size = round((width*(self.x))*50)
            # self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
            # pygame.gfxdraw.filled_circle(self.surf, round(width/2), round(width/2),round((width/2)-2), (255, 183, 28))

          else:
            self.kill()
    # x = 1
    # self.rect.move_ip(0,-2)
    # #  self.surf = pygame.Surface((7*(0.80**x),7*(0.80**x))) MAKE BULLET SMALLER FARTHER AWAY IT GETS
    # x = x + 1
        # if self.rect.top < 30:
        #   self.kill()

    
