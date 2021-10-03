import pygame
import soldier

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

player = soldier.Soldier(200,200,3)
enemy = soldier.Soldier(400,400,3)

run = True
while run:

  player.draw(screen)
  enemy.draw(screen)

  for event in pygame.event.get():
    # quit game
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()

pygame.quit()