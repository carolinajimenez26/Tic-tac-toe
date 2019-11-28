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
  elements.text_should_restart.draw(elements.screen)
  count = 5 # let the user decide in 5 seconds
  x = 750
  while (count > 0):
    clicked_pos = -1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return False
      if event.type == pygame.MOUSEBUTTONDOWN:
        clicked_pos = pygame.mouse.get_pos()

    # If the user clicks the re-start button, end this current game and start 
    # a new one
    if (clicked_pos != -1 and elements.button.was_clicked(clicked_pos[0], 
        clicked_pos[1])):
      return True
    
    text_count_down = Text(25, x, 550, str(count), colors.RED)
    msg = "The winner is: " + get_winner_name(elements.grid, elements.player1, 
                                              elements.player2)
    text_winner = Text(40, 710, 50, msg, colors.ORANGE)

    # --- Drawing code should go here
    text_count_down.draw(elements.screen)
    text_winner.draw(elements.screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

    # --- Limit to 60 frames per second
    elements.clock.tick(60)
    time.sleep(1)
    count -= 1
    x += 50

  # The user didn't press the re-start button, the end will be close
  return False

def run(elements):
  done = False
  while not done:
    clicked_pos = -1
    wait = False
    # --- Main event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return False
      if event.type == pygame.MOUSEBUTTONDOWN:
        clicked_pos = pygame.mouse.get_pos()

    # make it slower to show the message
    if (elements.curr_player.get_name() == "computer"): 
      time.sleep(1)

    # --- Game logic should go here
    # If the user clicks the re-start button, end this current game and start 
    # a new one
    if (clicked_pos != -1 and 
      elements.button.was_clicked(clicked_pos[0], clicked_pos[1])):
      return True

    if (elements.curr_player.is_user() and clicked_pos != -1):
      x, y = elements.grid.convert_ui_position(clicked_pos[0], clicked_pos[1])
      moved = elements.grid.set_position(x, y, elements.curr_player.figure)
      if (moved):
        elements.curr_player = players_handler.toggle_player(elements.player1, 
                                                              elements.player2)
      wait = True # this is needed at the end of the game, avoid the computer move

    if (not elements.curr_player.is_user() and not wait):
      [row, col] = elements.curr_player.play(elements.grid.get_game_status())
      if (row != -1):
        elements.grid.set_position(col, row, elements.curr_player.figure)
        elements.curr_player = players_handler.toggle_player(elements.player1, 
                                                              elements.player2)

    if (elements.grid.is_end_game()):
      done = True

    msg = elements.curr_player.get_name() + "'s turn"
    text_player = Text(50, 750, 150, msg, colors.PINK)

    # --- Screen-clearing code goes here
    elements.screen.fill(colors.WHITE)

    # --- Drawing code should go here
    elements.grid.draw(elements.screen)
    elements.button.draw(elements.screen)
    text_player.draw(elements.screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()

    # --- Limit to 60 frames per second
    elements.clock.tick(60)

  # if we get here is because there was a winner of a tie
  return should_restart(elements) # ask the user if they want to start again