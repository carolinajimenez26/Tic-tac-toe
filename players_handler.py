def toggle_player(player1, player2):
  if (player1.get_turn()):
    player2.set_turn(True)
    player1.set_turn(False)
    return player2
  else:
    player2.set_turn(False)
    player1.set_turn(True)
    return player1

def get_winner_name(grid, player1, player2):
  winner = ""
  if (grid.winner == ""):
    winner = "No one"
  elif (grid.winner == player1.get_figure()):
    winner = player1.get_name()
  else:
    winner = player2.get_name()
  return winner