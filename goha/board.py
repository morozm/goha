import pygame
from .constants import OFFBOARD, MARKER, EMPTY, LIBERTY, BOARDS, SELECTED_BOARD, STONECOLORS, BLACKCOLOR, BROWNCOLOR, ROWS, COLS, SQUARE_SIZE, BOARD_HEIGHT_OFFSET, BOARD_WIDTH_OFFSET
from .piecetodraw import PieceToDraw

class Board:
    def __init__(self):
        self.board = []
        self.block = []
        self.liberties = []
        # self.create_board()
        self.load_board()

    def draw_squares(self, win):
        win.fill(BLACKCOLOR)
        pygame.draw.rect(win, BROWNCOLOR, (BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET, SQUARE_SIZE*COLS, SQUARE_SIZE*ROWS))
        for row in range(ROWS):
            pygame.draw.line(win, BLACKCOLOR, (SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, row*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), (SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET + SQUARE_SIZE*(COLS-1), row*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET))
        for col in range(COLS):
            pygame.draw.line(win, BLACKCOLOR, (col*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), (col*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET + SQUARE_SIZE*(ROWS-1)))
    
    def calc_square(self, row, col):
        return (row+1)*(COLS+2)+col+1

    def place(self, row, col, turn):
        self.board[self.calc_square(row, col)] = turn

    def place2(self, square, turn):
        self.board[square] = turn
    
    def get_piece(self, row, col):
        return self.board[self.calc_square(row, col)]
    
    def set_piece(self, square, stone):
        self.board[square] = stone

    def create_board(self):
        for row in range(ROWS+2):
            for col in range(COLS+2):
                if row==0 or row==ROWS+2 or col==0 or col==COLS+2:
                    self.board.append(7)
                else:
                    self.board.append(0)

    def load_board(self):
        self.board = BOARDS[SELECTED_BOARD]

    def draw(self, win):
        self.draw_squares(win)
        for square in range (len(self.board)):
            piece = self.board[square]
            if piece != 0 and piece != 7:
                piece = PieceToDraw(square, STONECOLORS[piece])
                piece.draw(win)
                    
    def remove(self, pieces): # unused
        for piece in pieces:
            # self.board[self.calc_square(piece.row, piece.col)] = 0
            self.board[piece.square] = 0

    def winner(self):
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        return moves
    
    def count(self, square, color):
        piece = self.board[square]
        if piece == OFFBOARD:
            return
        if piece and (piece & color) and (piece & MARKER) == 0:
            self.block.append(square)
            self.board[square] |= MARKER
            self.count(square - (COLS+2), color)    # walk north
            self.count(square - 1, color)           # walk east
            self.count(square + (COLS+2), color)    # walk south
            self.count(square + 1, color)           # walk west
        elif piece == EMPTY:
            self.board[square] |= LIBERTY
            self.liberties.append(square)

    def clear_block(self):
        for captured in self.block: self.board[captured] = EMPTY

    def clear_groups(self):
        self.block = []
        self.liberties = []

    def clear_board(self):
        self.clear_groups()
        for square in range(len(self.board)):
            if self.board[square] != OFFBOARD: self.board[square] = 0

    def restore_board(self):
        self.clear_groups()
        for square in range((ROWS+2) * (COLS+2)):
            if self.board[square] != OFFBOARD: 
                self.board[square] &= 3

    def evaluate(self):
        pass