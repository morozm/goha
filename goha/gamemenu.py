import pygame
from .game import Game
from .constants import BOARD_HEIGHT_OFFSET, BOARD_WIDTH_OFFSET, SQUARE_SIZE, ROWS, COLS

class Gamemenu:
    def __init__(self, win):
        self.win = win
        self.game = Game(self.win)
        self._init()

    def _init(self):
        self.running = True
        self.clock = pygame.time.Clock()
        # self.run_menu()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = (y - BOARD_HEIGHT_OFFSET) // SQUARE_SIZE
        col = (x - BOARD_WIDTH_OFFSET) // SQUARE_SIZE
        if (row<0 or col<0 or row>=ROWS or col>=COLS):
            return False
        return row, col
    
    def draw_game_menu(self):
        if self.game.winner() != None:
            print(self.game.winner())
            self.running = False
        self.game.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (self.get_row_col_from_mouse(pos) != False and self.game.gamestate == 'active'):
                    row, col = self.get_row_col_from_mouse(pos)
                    if self.game.place(row, col):
                        self.game.process_move()
                        self.game.opponent_moves() # comment these 2 lines to play solo
                        self.game.process_move()   # comment these 2 lines to play solo
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False     