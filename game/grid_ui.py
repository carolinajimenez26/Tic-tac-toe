import pygame
import colors

class GridUI:
  def __init__(self):
    self.square_size = 200
    self.lines = [
      # start x from 0 to 3 times the square size
      ((0, self.square_size), (3 * self.square_size, self.square_size)), # horizontal
      # this time y is 2 times square size down
      ((0, 2 * self.square_size), (3 * self.square_size, 2 * self.square_size)), # horizontal
      # start y from 0 to 3 times square size
      ((self.square_size, 0), (self.square_size, 3 * self.square_size)), # vertical
      # this time x is 2 times squares size right
      ((2 * self.square_size, 0), (2 * self.square_size, 3 * self.square_size)), # vertical
    ]

  def draw(self, surface):
    thickness = 2
    for line in self.lines:
      p1 = line[0]
      p2 = line[1]
      pygame.draw.line(surface, colors.BLACK, p1, p2, thickness)

  def draw_figure(self, surface, col, row, figure):
    # we need to get the center of the square
    x = col * self.square_size + (self.square_size / 2)
    y = row * self.square_size + (self.square_size / 2)
    delta = self.square_size // 3
    if (figure == "O"):
      # the circle is drawn in the middle because it expands itself by its radius
      pygame.draw.circle(surface, colors.BLUE, (x, y), delta, width=2)
    elif (figure == "X"):
      # draw left to right line
      p1 = (x - delta, y - delta)
      p2 = (x + delta, y + delta)
      pygame.draw.line(surface, colors.GREEN, p1, p2, 2)
      # draw right to left line
      p1 = (x + delta, y - delta)
      p2 = (x - delta, y + delta)
      pygame.draw.line(surface, colors.GREEN, p1, p2, 2) 

  def convert_ui_position(self, x, y):
    return x // self.square_size, y // self.square_size

  
