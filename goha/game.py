import pygame
from .board import Board
from .opponent import Opponent
from .constants import BLACK, WHITE, BLUECOLOR, SQUARE_SIZE, BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def _init(self):
        self.board = Board()
        self.opponent = Opponent()
        self.turn = BLACK
        self.gamestate = 'active'
        self.board.find_legal_moves(self.turn)
        self.check_if_legal_moves_exist()

    def winner(self):
        return self.board.winner()

    def place(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece == 0:
            if self.board.calc_square(row, col) in self.board.legal_moves:
                self.board.place(row, col, self.turn)
                return True
            else:
                print('place is illegal')
                return False
        else:
            print('place is occupied')
            return False
    
    def process_move(self):
        self.board.captures(3 - self.turn)
        self.change_turn()
        self.board.find_legal_moves(self.turn)
        self.check_if_legal_moves_exist()

    def opponent_moves(self):
        if self.gamestate == 'active':
            self.opponent.gen_move(self.turn, self.board)

    def draw_valid_moves(self, moves): #unused
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUECOLOR, (col * SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, row * SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), SQUARE_SIZE//6)

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
    
    def check_if_legal_moves_exist(self):
        if len(self.board.legal_moves) == 0:
            print('No more legal moves! Game ends.')
            self.gamestate = 'inactive'
            return False
        else:
            return True