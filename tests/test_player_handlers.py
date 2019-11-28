import pytest
from game.player import Player
from game.grid_logic import Grid
import game.players_handler

def test_toggle_player():
  player1 = Player("X", True, "user")
  player1.set_turn(True)
  player2 = Player("O", False, "computer")
  assert game.players_handler.toggle_player(player1, player2) == player2

def test_get_winner_name():
  player1 = Player("X", True, "user")
  player2 = Player("O", False, "computer")
  grid = Grid()

  test_cases = [
    {
      "figure": player1.get_figure(), 
      "expected": player1.get_name()
    },
    {
      "figure": player2.get_figure(), 
      "expected": player2.get_name()
    },
    {
      "figure": "", 
      "expected": "No one"
    }
  ]

  for test in test_cases:
    grid.winner = test["figure"]
    assert game.players_handler.get_winner_name(grid, player1, player2) == test["expected"]