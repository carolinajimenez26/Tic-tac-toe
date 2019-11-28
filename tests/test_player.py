import pytest
import sys
sys.path.append('../')
from player import Player

def test_get_turn():
  player = Player("X", True, "user")
  assert player.get_turn() == False

def test_set_turn():
  player = Player("X", True, "user")
  player.set_turn(True)
  assert player.get_turn()

def test_is_user():
  player = Player("X", True, "user")
  assert player.is_user()

def test_get_name():
  player = Player("X", True, "user")
  assert player.get_name() == "user"

def test_get_figure():
  player = Player("X", True, "user")
  assert player.get_figure() == "X"

def test_play():
  grid = [
    ["", "X","O"],
    ["O","X","O"],
    ["X","O","X"],
  ]
  player = Player("X", True, "user")
  assert player.play(grid) == [0,0]