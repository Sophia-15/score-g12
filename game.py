import pygame
import os
from time import sleep

pygame.init()
pygame.font.init()

cont = 0
letra = 0

colors = [
   (22, 163, 74),
   (240, 253, 244)
]

alfabeto = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
  'Y', 'Z'
]

screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

name = ['A', 'A', 'A']

blink_interval = 500 
last_blink_time = pygame.time.get_ticks()
show_text = True

while True:
    font = pygame.font.Font('retro.ttf', 36)
    color = colors[0] if show_text else colors[1]
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            if cont == 0:
               cont = 25
            else:
              cont -= 1
            name[letra] = alfabeto[cont]
          elif event.key == pygame.K_DOWN:
            if cont == 25:
               cont = 0
            else:
              cont += 1

            name[letra] = alfabeto[cont]
          elif event.key == pygame.K_RETURN:
            if letra != 2:
              letra += 1
               
    current_time = pygame.time.get_ticks()
    if current_time - last_blink_time > blink_interval:
        show_text = not show_text
        last_blink_time = current_time
        

    # Draw the game
    screen.fill((5, 46, 22))

    # Draw the score to the screen

    score_text = font.render(f"{name}", True,  color)

    
    screen.blit(score_text, (250 - 36, 250 - 36))
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

   