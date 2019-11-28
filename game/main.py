import pygame
import colors
from grid_logic import Grid
from grid_ui import GridUI
from player import Player
from button import Button
from game import run
from text import Text
from game_elements import GameElements

def initialize():
  size = (1100, 600) # [width, height]
  screen = pygame.display.set_mode(size)
  
  pygame.display.set_caption("Tic-tac-toe")
  
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()

  grid = Grid()
  grid_ui = GridUI()
  button = Button(colors.PURPLE, 750, 300, 200, 100, "RE-START")
  msg = "If you want to play again press RE-START button"
  text_should_restart = Text(25, 650, 450, msg, colors.RED)
  player1 = Player("X", True, "user")
  player2 = Player("O", False, "computer")

  player1.set_turn(True)
  curr_player = player1

  elements = {}
  elements["screen"] = screen
  elements["clock"] = clock
  elements["grid"] = grid
  elements["grid_ui"] = grid_ui
  elements["button"] = button
  elements["player1"] = player1
  elements["player2"] = player2
  elements["curr_player"] = curr_player
  elements["text_should_restart"] = text_should_restart
  game_elements = GameElements(elements)
  return game_elements

if __name__ == "__main__":
  pygame.init()
  elements = initialize()
  re_start = run(elements)
  while (re_start):
    elements = initialize()
    re_start = run(elements)
  pygame.quit()