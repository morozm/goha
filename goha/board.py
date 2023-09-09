import pygame
from .constants import BOARDS, SELECTED_BOARD, STONECOLORS, WHITECOLOR, BLACKCOLOR, BROWNCOLOR, ROWS, COLS, SQUARE_SIZE, BOARD_HEIGHT_OFFSET, BOARD_WIDTH_OFFSET
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        # self.create_board()
        self.load_board()

    def draw_squares(self, win):
        win.fill(BLACKCOLOR)
        pygame.draw.rect(win, BROWNCOLOR, (BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET, SQUARE_SIZE*COLS, SQUARE_SIZE*ROWS))
        for row in range(ROWS):
            pygame.draw.line(win, BLACKCOLOR, (SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, row*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), (SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET + SQUARE_SIZE*(COLS-1), row*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET))
        for col in range(COLS):
            pygame.draw.line(win, BLACKCOLOR, (col*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), (col*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET + SQUARE_SIZE*(ROWS-1)))
    
    def is_piece(self, piece):
        return isinstance(piece, Piece)
    
    def recalculate_row_col(self, row, col):
        return (row+1)*(COLS+2)+col+1

    def place(self, row, col, turn):
        self.board[self.recalculate_row_col(row, col)] = turn

    # def move(self, piece, row, col):
    #     if self.is_piece(piece):
    #         self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
    #         piece.move(row, col)
    
    def get_piece(self, row, col):
        return self.board[self.recalculate_row_col(row, col)]

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
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[self.recalculate_row_col(row, col)]
                if piece != 0 and piece != 7:
                    piece = Piece(row, col, STONECOLORS[piece])
                    piece.draw(win)
                    
    def remove(self, pieces):
        for piece in pieces:
            self.board[self.recalculate_row_col(piece.row, piece.col)] = 0

    def winner(self):
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        return moves