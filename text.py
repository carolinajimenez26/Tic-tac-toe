import pygame

class Text:
  def __init__(self, size, x, y, text, color):
    self.size = size
    self.x = x
    self.y = y
    self.text = text
    self.color = color

  def draw(self,surface):        
    font = pygame.font.SysFont('comicsans', self.size)
    text = font.render(self.text, 1, self.color)
    surface.blit(text, (self.x, self.y))