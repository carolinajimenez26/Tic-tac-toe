import pytest
import sys
sys.path.append('../')
from grid_logic import Grid

def test_set_position():
  grid = Grid()
  expected = [["X","",""],["","",""],["","",""]]
  grid.set_position(0, 0, "X")
  assert grid.get_game_status() == expected 

def test_is_valid():
  grid = Grid()

  test_cases = [
    {
      "row": 0,
      "col": 0,
      "expected": True
    },
    {
      "row": 1,
      "col": 0,
      "expected": True
    },
    {
      "row": -1,
      "col": 0,
      "expected": False
    },
    {
      "row": 0,
      "col": 10,
      "expected": False
    },
    {
      "row": 10,
      "col": 10,
      "expected": False
    },
    {
      "row": 3,
      "col": 2,
      "expected": False
    },
  ]

  for test in test_cases:
    assert grid.is_valid(test["row"], test["col"]) == test["expected"]

def test_get_game_status():
  grid = Grid()
  expected = [["","",""],["","",""],["","",""]]
  assert grid.get_game_status() == expected 
  grid.set_position(2,2,"O")
  expected[2][2] = "O"
  assert grid.get_game_status() == expected 

def test_find_all_continuous_occurrances():
  grid = Grid()
  grid.game_status = [
    ["X","X","X"],
    ["O","X","O"],
    ["O","O","O"]
  ]

  test_cases = [
    {
      "row": 0,
      "col": 0,
      "target": "X",
      "delta_row": 1, # down and right
      "delta_col": 1,
      "expected": 2
    },
    {
      "row": 0,
      "col": 0,
      "target": "X",
      "delta_row": 1, # down
      "delta_col": 0,
      "expected": 1
    },
    {
      "row": 0,
      "col": 0,
      "target": "X", # right
      "delta_row": 0,
      "delta_col": 1,
      "expected": 3
    },
    {
      "row": 2,
      "col": 0,
      "target": "O", # up
      "delta_row": -1,
      "delta_col": 0,
      "expected": 2
    },
    {
      "row": 2,
      "col": 2,
      "target": "O", # up left
      "delta_row": -1,
      "delta_col": -1,
      "expected": 1
    },
    {
      "row": -1, # invalid
      "col": 0,
      "target": "O", # up left
      "delta_row": -1,
      "delta_col": -1,
      "expected": 0
    },
    {
      "row": 0,
      "col": 0,
      "target": "O",
      "delta_row": 1,
      "delta_col": 1,
      "expected": 0
    },
  ]

  for test in test_cases:
    assert grid.find_all_continuous_occurrances(test["row"], test["col"], 
                                                test["target"], test["delta_row"], 
                                                test["delta_col"]) == test["expected"]

def test_check_all():
  grid = Grid()
  grid.game_status = [
    ["X","X","X"],
    ["O","X","O"],
    ["O","O","O"]
  ]
  assert grid.check_all(0,0)
  assert grid.check_all(1,0) == False
  assert grid.check_all(2,0)
  assert grid.check_all(1,1) == False

def test_there_is_winner():
  grid = Grid()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["O","O","O"]
  ]
  assert grid.there_is_winner()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["X","O","O"]
  ]
  assert grid.there_is_winner()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["O","X","O"]
  ]
  assert grid.there_is_winner() == False

def test_all_taken():
  grid = Grid()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["O","X","O"]
  ]
  assert grid.all_taken()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["X","O",""]
  ]
  assert grid.all_taken() == False

def test_is_end_game():
  grid = Grid()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["O","X","O"]
  ]
  assert grid.is_end_game()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["X","X","O"]
  ]
  assert grid.is_end_game()
  grid.game_status = [
    ["X","O","X"],
    ["O","X","O"],
    ["","X","O"]
  ]
  assert grid.is_end_game() == False
  