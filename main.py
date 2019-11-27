import pygame
import colors
from grid import Grid
from player import Player
import players_handler
import time
from button import Button
 
def run(elements):
  done = False
  screen = elements["screen"]
  clock = elements["clock"]
  grid = elements["grid"]
  button = elements["button"]
  player1 = elements["player1"]
  player2 = elements["player2"]
  curr_player = elements["curr_player"]

  while not done:
    clicked_pos = -1
    # --- Main event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return False
      if event.type == pygame.MOUSEBUTTONDOWN:
        clicked_pos = pygame.mouse.get_pos()

    # --- Game logic should go here
    if (clicked_pos != -1 and button.was_clicked(clicked_pos[0], clicked_pos[1])):
      print("WAS CLICKED!")
      return True

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
    button.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)
  
  return False

def initialize():
  size = (1000, 600) # [width, height]
  screen = pygame.display.set_mode(size)
  
  pygame.display.set_caption("Tic-tac-toe")
  
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()

  grid = Grid()
  button = Button(colors.PURPLE, 750, 400, 200, 100, "START")
  player1 = Player("X", True)
  player2 = Player("O", False)

  player1.set_turn(True)
  curr_player = player1

  elements = {}
  elements["screen"] = screen
  elements["clock"] = clock
  elements["grid"] = grid
  elements["button"] = button
  elements["player1"] = player1
  elements["player2"] = player2
  elements["curr_player"] = curr_player
  return elements

if __name__ == "__main__":
  pygame.init()
  elements = initialize()
  done = False
  re_start = run(elements)
  while (re_start and not done):
    elements = initialize()
    re_start = run(elements)
    
  pygame.quit()