import pygame, random
from .constants import ROWS, COLS, EMPTY

class Opponent:
    def __init__(self):
        self.difficulty = 0
        self.create_opponent()

    def create_opponent(self):
        pass

    def make_random_move(self, color, board):
        random_square = random.randrange(len(board.board))
        while board.board[random_square] != EMPTY:
            random_square = random.randrange(len(board.board))
        
        board.place2(random_square, color)
        board.count(random_square, color)
        
        if len(board.liberties) == 0:
            board.restore_board()
            board.set_piece(random_square, EMPTY)
            # board[random_square] = EMPTY

            try:
                return self.make_random_move(color, board)
            except:
                return '' 

        board.restore_board()
        
        # print('random move:', board.board[random_square])
