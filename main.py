import pygame
import colors
from grid import Grid
from player import Player
import time
from button import Button
from game import run

def initialize():
  size = (1000, 600) # [width, height]
  screen = pygame.display.set_mode(size)
  
  pygame.display.set_caption("Tic-tac-toe")
  
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()

  grid = Grid()
  button = Button(colors.PURPLE, 750, 400, 200, 100, "START")
  player1 = Player("X", True)
  player2 = Player("O", False)

  player1.set_turn(True)
  curr_player = player1

  elements = {}
  elements["screen"] = screen
  elements["clock"] = clock
  elements["grid"] = grid
  elements["button"] = button
  elements["player1"] = player1
  elements["player2"] = player2
  elements["curr_player"] = curr_player
  return elements

if __name__ == "__main__":
  pygame.init()
  elements = initialize()
  done = False
  re_start = run(elements)
  while (re_start and not done):
    elements = initialize()
    re_start = run(elements)
    
  pygame.quit()