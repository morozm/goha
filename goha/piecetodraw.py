import pygame
from .constants import STONECOLORS, COLS, ROWS, GREYCOLOR, SQUARE_SIZE, BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET

class PieceToDraw:
    PADDING = 12
    OUTLINE = 2
    
    def __init__(self, square, color):
        self.square = square
        self.row = 0
        self.col = 0
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_row_col()
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE // 2 + BOARD_WIDTH_OFFSET
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE // 2 + BOARD_HEIGHT_OFFSET
    
    def calc_row_col(self):
        self.row = self.square//(COLS+2)-1
        self.col = self.square - (self.row+1)*(COLS+2) - 1

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREYCOLOR, (self.x, self.y), (radius + self.OUTLINE))
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):
        return str(self.color)