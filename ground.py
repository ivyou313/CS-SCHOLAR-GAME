import pygame

speed = 5
class Ground(pygame.sprite.Sprite):

  def __init__(self):
    super(Ground, self).__init__()
    self.surf = pygame.Surface((500, 20))
    self.surf.fill((0,0,0))
    self.rect = self.surf.get_rect (center=(250,390))

#   def update(self):

#     self.rect.move_ip((-speed, 0))

#     if self.rect.right < 0:
#       self.rect.topleft = (410,260)

    