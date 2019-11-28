class Grid:
  def __init__(self):
    self.game_status = [["","",""],["","",""],["","",""]]
    self.winner = ""
    self.row_size = 3
    self.col_size = 3

  def set_position(self, col, row, figure):
    """Returns if the new position was valid"""
    if (self.is_valid(row,col) and self.game_status[row][col] == ""):
      self.game_status[row][col] = figure
      return True
    return False

  def is_valid(self, row, col):
    return row >= 0 and row < self.row_size and col >= 0 and col < self.col_size

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
      return 1 + self.find_all_continuous_occurrances(new_row, new_col, target, 
                                                      delta_row, delta_col)
    
    return 0

  def check_all(self, row, col):
    # all the possible directions following the direction of clockwise
    dir_rows = [-1, -1, 0, 1, 1,  1,  0, -1] 
    dir_cols = [ 0,  1, 1, 1, 0, -1, -1, -1]
    for i in range(len(dir_rows)):
      target = self.game_status[row][col]
      new_row = row + dir_rows[i]
      new_col = col + dir_cols[i]
      # check if going in the same direction I can find 2 more figures equals to mine
      target_ocurrances = self.find_all_continuous_occurrances(new_row, new_col, 
                                                target, dir_rows[i], dir_cols[i])
      if (target_ocurrances == 2): # +1 of my own figure equals 3
        return True
    
    return False

  def there_is_winner(self):
    # There is no need to check more than the first row and the first column
    for col in range(len(self.game_status[0])):
      if (self.game_status[0][col] == ""):
        continue
      if (self.check_all(0, col)): # check if there is a winner from this cell
        self.winner = self.game_status[0][col] # save the winner for later
        return True
    
    for row in range(len(self.game_status)):
      if (self.game_status[row][0] == ""):
        continue
      if (self.check_all(row, 0)):
        self.winner = self.game_status[row][0]
        return True

    return False

  def all_taken(self):
    # checks if all the squares are taken
    for row in range(len(self.game_status)):
      for col in range(len(self.game_status[0])):
        if (self.game_status[row][col] == ""):
          return False
    return True

  def is_end_game(self):
    return self.there_is_winner() or self.all_taken()