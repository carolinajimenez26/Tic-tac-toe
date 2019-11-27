import pygame

class Button:
  def __init__(self, color, x, y, width, height, text=''):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text

  def draw(self,surface):        
    pygame.draw.rect(surface, self.color, (self.x , self.y, self.width, self.height), 0)
    
    if self.text != '':
      font = pygame.font.SysFont('comicsans', 40)
      text = font.render(self.text, 1, (0,0,0))
      # put the text in the middle
      x = self.x + (self.width / 2 - text.get_width() / 2)
      y = self.y + (self.height / 2 - text.get_height() / 2)
      surface.blit(text, (x, y))

  def was_clicked(self, x, y):
    return x >= self.x and x <= (self.x + self.width) and y >= self.y and y <= (self.y + self.height)