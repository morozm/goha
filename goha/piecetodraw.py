import pygame
from .constants import GREYCOLOR, PADDING, OUTLINE

class PieceToDraw:
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
        radius = round((100 - PADDING)/100 * self.square_size / 2)
        pygame.draw.circle(win, GREYCOLOR, (self.x + offset[0], self.y + offset[1]), (radius + OUTLINE))
        pygame.draw.circle(win, self.color, (self.x + offset[0], self.y + offset[1]), radius)

    def draw_last_move(self, offset, win):
        radius = round((100 - PADDING)/100 * self.square_size / 4)
        pygame.draw.circle(win, GREYCOLOR, (self.x + offset[0], self.y + offset[1]), (radius + OUTLINE))
        pygame.draw.circle(win, self.color, (self.x + offset[0], self.y + offset[1]), radius)

    def draw_hover_piece(self, offset, win):
        radius = round((100 - PADDING)/100 * self.square_size / 2)
        transparent_color = self.color + (128,)
        surface = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(surface, transparent_color, (radius, radius), radius)
        win.blit(surface, (self.x + offset[0] - radius, self.y + offset[1] - radius))

    def __repr__(self):
        return str(self.color)