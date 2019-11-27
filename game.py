import pygame
import colors
import players_handler
from text import Text
import time

def get_winner_name(grid, player1, player2):
  winner = ""
  if (grid.winner == ""):
    winner = "No one"
  elif (grid.winner == player1.get_figure()):
    winner = player1.get_name()
  else:
    winner = player2.get_name()
  return winner

def should_restart(elements):
  screen = elements["screen"]
  clock = elements["clock"]
  grid = elements["grid"]
  button = elements["button"]
  player1 = elements["player1"]
  player2 = elements["player2"]
  curr_player = elements["curr_player"]
  text_should_restart = elements["text_should_restart"]

  text_should_restart.draw(screen)
  count = 5
  x = 750
  while (count > 0):
    clicked_pos = -1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return False
      if event.type == pygame.MOUSEBUTTONDOWN:
        clicked_pos = pygame.mouse.get_pos()

    if (clicked_pos != -1 and button.was_clicked(clicked_pos[0], clicked_pos[1])):
      return True
    
    text_count_down = Text(25, x, 550, str(count), colors.RED)
    msg = "The winner is: " + get_winner_name(grid, player1, player2)
    text_winner = Text(40, 710, 50, msg, colors.ORANGE)

    # --- Drawing code should go here
    text_count_down.draw(screen)
    text_winner.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)
    time.sleep(1)
    count -= 1
    x += 50

  return False

def run(elements):
  done = False
  screen = elements["screen"]
  clock = elements["clock"]
  grid = elements["grid"]
  button = elements["button"]
  player1 = elements["player1"]
  player2 = elements["player2"]
  curr_player = elements["curr_player"]
  text_should_restart = elements["text_should_restart"]

  while not done:
    clicked_pos = -1
    wait = False
    # --- Main event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return False
      if event.type == pygame.MOUSEBUTTONDOWN:
        clicked_pos = pygame.mouse.get_pos()

    if (curr_player.get_name() == "computer"): # make it slower to show the message
      time.sleep(1)

    # --- Game logic should go here
    if (clicked_pos != -1 and button.was_clicked(clicked_pos[0], clicked_pos[1])):
      return True

    if (curr_player.is_user() and clicked_pos != -1):
      # grid.show_game_status() # just for debugging
      moved = grid.set_position(clicked_pos[0], clicked_pos[1], curr_player.figure, True)
      if (moved):
        curr_player = players_handler.toggle_player(player1, player2)
      wait = True
      # grid.show_game_status() # just for debugging

    if (not curr_player.is_user() and not wait):
      [row, col] = curr_player.play(grid.get_game_status())
      if (row != -1):
        grid.set_position(col, row, curr_player.figure, False)
        curr_player = players_handler.toggle_player(player1, player2)

    if (grid.is_end_game()):
      done = True

    msg = curr_player.get_name() + "'s turn"
    text_player = Text(50, 750, 150, msg, colors.PINK)

    # --- Screen-clearing code goes here
    screen.fill(colors.WHITE)

    # --- Drawing code should go here
    grid.draw(screen)
    button.draw(screen)
    text_player.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)

  return should_restart(elements)