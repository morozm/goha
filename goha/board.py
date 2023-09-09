import pygame
from .constants import RED, WHITE, BLACK, BROWN, ROWS, COLS, SQUARE_SIZE, BOARD_HEIGHT_OFFSET, BOARD_WIDTH_OFFSET
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        pygame.draw.rect(win, BROWN, (BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET, SQUARE_SIZE*COLS, SQUARE_SIZE*ROWS))
        for row in range(ROWS):
            pygame.draw.line(win, BLACK, (SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, row*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), (SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET + SQUARE_SIZE*(COLS-1), row*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET))
        for col in range(COLS):
            pygame.draw.line(win, BLACK, (col*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), (col*SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET + SQUARE_SIZE*(ROWS-1)))
    def is_piece(self, piece):
        return isinstance(piece, Piece)

    def place(self, row, col, turn):
        self.board[row][col] = Piece(row, col, turn)

    def move(self, piece, row, col):
        if self.is_piece(piece):
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
            piece.move(row, col)
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
                    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    def winner(self):
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        return moves