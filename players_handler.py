def toggle_player(player1, player2):
  if (player1.get_turn()):
    player2.set_turn(True)
    player1.set_turn(False)
    return player2
  else:
    player2.set_turn(False)
    player1.set_turn(True)
    return player1