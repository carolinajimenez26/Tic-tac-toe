class Player:
  def __init__(self, figure):
    self.figure = figure
    self.turn = False

  def set_turn(self, turn):
    self.turn = turn

  def get_turn(self):
    return self.turn