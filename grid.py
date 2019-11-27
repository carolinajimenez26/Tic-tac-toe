import pygame
import colors

class Grid:
  def __init__(self):
    self.square_size = 200
    self.lines = [
      ((0, self.square_size), (3 * self.square_size, self.square_size)), # horizontal
      ((0, 2 * self.square_size), (3 * self.square_size, 2 * self.square_size)), # horizontal
      ((self.square_size, 0), (self.square_size, 3 * self.square_size)), # vertical
      ((2 * self.square_size, 0), (2 * self.square_size, 3 * self.square_size)), # vertical
    ]

    self.game_status = [["","",""],["","",""],["","",""]]
    self.winner = ""

  def draw(self, surface):
    thickness = 2
    for line in self.lines:
      p1 = line[0]
      p2 = line[1]
      pygame.draw.line(surface, colors.BLACK, p1, p2, thickness)
    
    self.draw_figures(surface)

  def draw_figures(self, surface):
    for row in range(len(self.game_status)):
      for col in range(len(self.game_status[0])):
        if (self.game_status[row][col] != ""):
          x = col * self.square_size + (self.square_size / 2)
          y = row * self.square_size + (self.square_size / 2)
          self.draw_figure(surface, x, y, self.game_status[row][col])

  def draw_figure(self, surface, x, y, figure):
    delta = self.square_size // 3
    if (figure == "O"):
      pygame.draw.circle(surface, colors.BLUE, (x, y), delta, width=2)
    elif (figure == "X"):
      p1 = (x - delta, y - delta)
      p2 = (x + delta, y + delta)
      pygame.draw.line(surface, colors.GREEN, p1, p2, 2) 
      p1 = (x + delta, y - delta)
      p2 = (x - delta, y + delta)
      pygame.draw.line(surface, colors.GREEN, p1, p2, 2) 

  def is_valid(self, row, col):
    return row >= 0 and row < 3 and col >= 0 and col < 3

  def set_position(self, x, y, figure, should_traslate):
    if (should_traslate):
      row = y // self.square_size
      col = x // self.square_size
    else:
      row = y
      col = x
    if (self.is_valid(row,col) and self.game_status[row][col] == ""):
      self.game_status[row][col] = figure
      return True
    return False

  def show_game_status(self):
    for row in range(len(self.game_status)):
      print(self.game_status[row])

  def get_game_status(self):
    return self.game_status

  def find_all_continuous_occurrances(self, row, col, target, delta_row, delta_col):
    if (not self.is_valid(row,col)):
      return 0

    if (self.game_status[row][col] == target):
      new_row = row + delta_row
      new_col = col + delta_col
      return 1 + self.find_all_continuous_occurrances(new_row, new_col, target, delta_row, delta_col)
    
    return 0

  def check_all(self, row, col):
    # all the possible directions following the direction of clockwise
    dir_rows = [-1, -1, 0, 1, 1,  1,  0, -1] 
    dir_cols = [ 0,  1, 1, 1, 0, -1, -1, -1]
    for i in range(len(dir_rows)):
      target = self.game_status[row][col]
      new_row = row + dir_rows[i]
      new_col = col + dir_cols[i]
      target_ocurrances = self.find_all_continuous_occurrances(new_row, new_col, 
                                                target, dir_rows[i], dir_cols[i])
      if (target_ocurrances == 2):
        return True
    
    return False

  def there_is_winner(self):
    for col in range(len(self.game_status[0])):
      if (self.game_status[0][col] == ""):
        continue
      if (self.check_all(0, col)):
        self.winner = self.game_status[0][col]
        return True
    
    for row in range(len(self.game_status)):
      if (self.game_status[row][0] == ""):
        continue
      if (self.check_all(row, 0)):
        self.winner = self.game_status[row][0]
        return True

    return False

  def there_is_tie(self):
    for row in range(len(self.game_status)):
      for col in range(len(self.game_status[0])):
        if (self.game_status[row][col] == ""):
          return False
    return True

  def is_end_game(self):
    return self.there_is_winner() or self.there_is_tie()
