import pygame
import colors
from grid import Grid
from player import Player
import players_handler
import time
 
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
player1 = Player("X", True)
player2 = Player("O", False)

player1.set_turn(True)
curr_player = player1
 
# -------- Main Program Loop -----------
while not done:
  clicked_pos = -1
  # --- Main event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      clicked_pos = pygame.mouse.get_pos()

  # --- Game logic should go here
  if (curr_player.is_user() and clicked_pos != -1):
    # grid.show_game_status() # just for debugging
    moved = grid.set_position(clicked_pos[0], clicked_pos[1], curr_player.figure, True)
    if (moved):
      curr_player = players_handler.toggle_player(player1, player2)
    
    # grid.show_game_status() # just for debugging

  if (not curr_player.is_user()):
    [row, col] = curr_player.play(grid.get_game_status())
    if (row != -1):
      grid.set_position(col, row, curr_player.figure, False)
      curr_player = players_handler.toggle_player(player1, player2)

  if (grid.is_end_game()):
    done = True
  # --- Screen-clearing code goes here
  screen.fill(colors.WHITE)

  # --- Drawing code should go here
  grid.draw(screen)

  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()
  pygame.display.update()

  # --- Limit to 60 frames per second
  clock.tick(60)
  
  if (done):
    time.sleep(5) # to see what was the last move
 
# Close the window and quit.
pygame.quit()