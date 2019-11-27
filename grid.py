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
        print(row, col)
        if (self.game_status[row][col] != ""):
          p1 = col * self.square_size + (self.square_size / 2)
          p2 = row * self.square_size + (self.square_size / 2)
          self.draw_figure(surface, p1, p2, self.game_status[row][col])

  def draw_figure(self, surface, p1, p2, figure):
    print(p1, p2)
    pygame.draw.circle(surface, colors.RED, (p1, p2), self.square_size // 3)

  def is_valid(self, row, col):
    return row >= 0 and row < 3 and col >= 0 and col < 3 and self.game_status[row][col] == ""

  def set_position(self, x, y, figure):
    row = y // self.square_size
    col = x // self.square_size
    if (self.is_valid(row,col)):
      self.game_status[row][col] = figure
      return True
    return False

  def show_game_status(self):
    for row in range(len(self.game_status)):
      print(self.game_status[row])
