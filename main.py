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
