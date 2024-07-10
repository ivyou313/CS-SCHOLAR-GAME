import pygame


speed = 7


class Pong( pygame.sprite.Sprite):
  def __init__(self, xpos, ypos):
    super(Pong, self).__init__()
    self.surf = pygame.Surface((7, 7))
    self.surf.fill((0,0,0))
    self.rect = self.surf.get_rect(center=(xpos+30, ypos+20))

  #def update(self):
  
