import pygame
from .constants import STONECOLORS, GREYCOLOR

class PieceToDraw:
    PADDING = 15    #percents
    OUTLINE = 2     #pixels
    
    def __init__(self, square, color, rows, cols, square_size, board_height_offset, board_width_offset):
        self.square = square
        self.row = 0
        self.col = 0
        self.rows = rows
        self.cols = cols
        self.square_size = square_size
        self.board_height_offset = board_height_offset
        self.board_width_offset = board_width_offset
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_row_col()
        self.calc_pos()

    def calc_pos(self):
        self.x = self.square_size*self.col + self.square_size // 2 + self.board_width_offset
        self.y = self.square_size*self.row + self.square_size // 2 + self.board_height_offset
    
    def calc_row_col(self):
        self.row = self.square//(self.cols+2)-1
        self.col = self.square - (self.row+1)*(self.cols+2) - 1

    def draw(self, offset, win):
        radius = round((100 - self.PADDING)/100 * self.square_size / 2)
        pygame.draw.circle(win, GREYCOLOR, (self.x + offset[0], self.y + offset[1]), (radius + self.OUTLINE))
        pygame.draw.circle(win, self.color, (self.x + offset[0], self.y + offset[1]), radius)

    def __repr__(self):
        return str(self.color)