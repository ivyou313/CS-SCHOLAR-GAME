import pygame


speed = 7


class Pong(pygame.sprite.Sprite):
  def __init__(self, xpos, ypos):
    super(Pong, self).__init__()
    self.surf = pygame.Surface((7, 7))
    self.surf.fill((0,0,0))
    self.rect = self.surf.get_rect(center=(xpos+30, ypos-20))

  def update(self):
    x = 1
    
   
    self.rect.move_ip(0,-2)
    #  self.surf = pygame.Surface((7*(0.80**x),7*(0.80**x)))
    x = x + 1
    if self.rect.top < 30:
      self.kill()
