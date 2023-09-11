import pygame, random
from .constants import ROWS, COLS, EMPTY

class Opponent:
    def __init__(self):
        self.difficulty = 0
        self.create_opponent()

    def create_opponent(self):
        pass

    def make_random_move(self, color, board):
        if len(board.legal_moves) != 0:
            random_square = board.legal_moves[random.randrange(len(board.legal_moves))]
            board.place2(random_square, color)
        else:
            print
        # print('random move:', random_square)
