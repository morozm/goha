import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE, BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET

class Piece:
    PADDING = 12
    OUTLINE = 2
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE // 2 + BOARD_WIDTH_OFFSET
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE // 2 + BOARD_HEIGHT_OFFSET

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), (radius + self.OUTLINE))
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)