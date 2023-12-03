import pygame
import sys
from .game import Game
from .constants import BOARD_HEIGHT_OFFSET, BOARD_WIDTH_OFFSET, SQUARE_SIZE, ROWS, COLS

FPS = 60

class Gamemenu:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.run = True
        self.clock = pygame.time.Clock()
        self.run_menu()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = (y - BOARD_HEIGHT_OFFSET) // SQUARE_SIZE
        col = (x - BOARD_WIDTH_OFFSET) // SQUARE_SIZE
        if (row<0 or col<0 or row>=ROWS or col>=COLS):
            return False
        return row, col
    
    def run_menu(self):
        game = Game(self.win)
        while self.run:
            # self.clock.tick(FPS)

            if game.winner() != None:
                print(game.winner())
                self.run = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (self.get_row_col_from_mouse(pos) != False and game.gamestate == 'active'):
                        row, col = self.get_row_col_from_mouse(pos)
                        if game.place(row, col):
                            game.process_move()
                            game.opponent_moves() # comment these 2 lines to play solo
                            game.process_move()   # comment these 2 lines to play solo
            game.update()
        pygame.quit()
        sys.exit()