class GameElements:
  def __init__(self, elements):
    self.screen = elements["screen"]
    self.clock = elements["clock"]
    self.grid = elements["grid"]
    self.grid_ui = elements["grid_ui"]
    self.button = elements["button"]
    self.player1 = elements["player1"]
    self.player2 = elements["player2"]
    self.curr_player = elements["curr_player"]
    self.text_should_restart = elements["text_should_restart"]