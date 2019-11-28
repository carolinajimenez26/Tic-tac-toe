import pygame
from text import Text
import colors

class Button:
  def __init__(self, color, x, y, width, height, text=''):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    size_text = 40
    x_text = x + (width / 2 - width // 3)
    y_text = y + (height / 2 - 8)
    self.text = Text(size_text, x_text, y_text, text, colors.BLACK)

  def draw(self,surface):        
    pygame.draw.rect(surface, self.color, (self.x , self.y, self.width, self.height), 0)
    self.text.draw(surface)

  def was_clicked(self, x, y):
    return x >= self.x and x <= (self.x + self.width) and y >= self.y and y <= (self.y + self.height)