import pygame
import colors
from grid import Grid
 
# ======= Initializations =========
pygame.init()

size = (1000, 600) # [width, height]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tic-tac-toe")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

grid = Grid()
 
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      clicked_pos = pygame.mouse.get_pos()
      grid.show_game_status()
      grid.set_position(clicked_pos[0], clicked_pos[1], "X")
      grid.show_game_status()

  # --- Game logic should go here

  # --- Screen-clearing code goes here

  # Here, we clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.

  # If you want a background image, replace this clear with blit'ing the
  # background image.
  screen.fill(colors.WHITE)

  # --- Drawing code should go here
  grid.draw(screen)

  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()
  pygame.display.update()

  # --- Limit to 60 frames per second
  clock.tick(60)
 
# Close the window and quit.
pygame.quit()