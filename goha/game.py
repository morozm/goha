import pygame
from .board import Board
from .constants import BLACK, WHITE, BLUECOLOR, SQUARE_SIZE, BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        # self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def _init(self):
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def place(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece == 0:
            self.board.place(row, col, self.turn)
            self.change_turn()
            return True
        else:
            return False
    
    def draw_valid_moves(self, moves): #unused
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUECOLOR, (col * SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, row * SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), SQUARE_SIZE//6)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK