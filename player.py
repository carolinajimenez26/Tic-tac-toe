import random

class Player:
  def __init__(self, figure, user, name):
    self.figure = figure
    self.turn = False
    self.user = user
    self.name = name

  def set_turn(self, turn):
    self.turn = turn

  def get_turn(self):
    return self.turn

  def is_user(self):
    return self.user

  def get_name(self):
    return self.name

  def play(self, grid):
    availables = []
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if (grid[row][col] == ""):
          availables.append([row, col])

    if (len(availables) == 0):
      return [-1,-1] # error
    
    i = random.randrange(0, len(availables), 1)
    return availables[i]
    
