import pygame
from config import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")
 
run = True
while run:
  # update background
  screen.fill(CUSTOM_COLOR)
  
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
