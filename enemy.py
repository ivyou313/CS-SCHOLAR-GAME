import pygame
import math
import random


screenWidth = 400
screenHeight = 300
width = 8.5
speed = 7
xPlaces = [100, 400]


#Player
class Enemy(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, finalPosx):
        super(Enemy, self,).__init__()
        self.surf = pygame.Surface((width, width))
        self.x = 7
        self.finalPosx = finalPosx
        #self.surf.fill((18, 107, 4))
        
        self.surf.fill((95,87,120))
        self.rect = self.surf.get_rect (center=(xpos,ypos))
        
    
    def update(self, time):
          #random.choice(xPlaces)
          dx, dy = self.finalPosx - self.rect.x, 400 - self.rect.y
          dist = math.hypot(dx, dy)
          if round(dist) > 1:
            dx, dy = dx / dist, dy / dist  # Normalize.
            # Move along this normalized vector towards the player at current speed.
            self.x = self.x *0.5
            self.rect.x += dx * 2
            self.rect.y += dy * 2
            pygame.transform.scale(self.surf, (self.x, self.x))
           # self.surf = pygame.Surface(width*(time%10), width*(time%10))
            self.surf.fill((18, 107, 4))

          else:
            self.kill()

  
