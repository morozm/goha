import pygame, random
from .constants import OFFBOARD, MARKER, EMPTY, LIBERTY, BOARDS, STONECOLORS, BLACKCOLOR, BROWNCOLOR, WIDTH, HEIGHT
from .piecetodraw import PieceToDraw
from .settings import Settings
BOARD_MENU_SPACE = 50
BOARD_EDGE_SPACE = 20

class Board:
    def __init__(self, board_size):
        self.board = []
        self.board_copy = []
        self.block = []
        self.liberties = []
        self.legal_moves = []
        self.offsets = []
        self.board_size = board_size
        self.settings = Settings()
        self.texture = pygame.image.load("goha/textures/texture2.jpg")
        self.load_settings()
        self._init()
        # self.create_board() 

    def _init(self):
        self.board = BOARDS[self.board_size][0].copy()
        self.rows, self.cols = BOARDS[self.board_size][1], BOARDS[self.board_size][2]
        self.square_size = min((WIDTH-BOARD_MENU_SPACE)//self.cols, (HEIGHT-BOARD_MENU_SPACE)//self.rows)
        self.board_height_offset = max(0, (HEIGHT - self.square_size*self.rows)//2)
        self.board_width_offset = max(0, (WIDTH - self.square_size*self.cols)//2)
        self.create_offsets()

    def load_settings(self):
        self.settings.load_settings()
        self.stone_centering = self.settings.get_stone_centering()

    def draw_squares(self, win):
        pygame.draw.rect(win, BLACKCOLOR, ((self.board_width_offset-3, self.board_height_offset-3, self.square_size*self.cols+6, self.square_size*self.rows+6)))
        win.blit(self.texture, pygame.Rect((self.board_width_offset, self.board_height_offset, self.square_size*self.cols, self.square_size*self.rows), border_radius = 100), pygame.Rect((0, 0, self.square_size*self.cols, self.square_size*self.rows), border_radius = 100))
        # pygame.draw.rect(win, BROWNCOLOR, ((self.board_width_offset, self.board_height_offset, self.square_size*self.cols, self.square_size*self.rows)), border_radius = 40)
        for row in range(self.rows):
            pygame.draw.line(win, BLACKCOLOR, (self.square_size//2 + self.board_width_offset, row*self.square_size + self.square_size//2 + self.board_height_offset), (self.square_size//2 + self.board_width_offset + self.square_size*(self.cols-1), row*self.square_size + self.square_size//2 + self.board_height_offset), 3)
        for col in range(self.cols):
            pygame.draw.line(win, BLACKCOLOR, (col*self.square_size + self.square_size//2 + self.board_width_offset, self.square_size//2 + self.board_height_offset), (col*self.square_size + self.square_size//2 + self.board_width_offset, self.square_size//2 + self.board_height_offset + self.square_size*(self.rows-1)), 3)
    
    def calc_square(self, row, col):
        return (row+1)*(self.cols+2)+col+1

    def place(self, row, col, turn):
        self.place2(self.calc_square(row, col), turn)

    def place2(self, square, turn):
        self.board[square] = turn
    
    def get_piece(self, row, col):
        return self.board[self.calc_square(row, col)]
    
    def set_piece(self, square, stone):
        self.board[square] = stone

    def create_board(self):
        for row in range(self.rows+2):
            for col in range(self.cols+2):
                if row==0 or row==self.rows+2 or col==0 or col==self.cols+2:
                    self.board.append(7)
                else:
                    self.board.append(0)

    def create_offsets(self):
        for row in range(self.rows+2):
            for col in range(self.cols+2):
                self.offsets.append([round(random.randrange(-7, 7)/100 * self.square_size), round(random.randrange(-7, 7)/100 * self.square_size)])
                
    def load_board(self):
        self.board = BOARDS[self.board_size][0].copy()

    def draw(self, win):
        self.draw_squares(win)
        for square in range (len(self.board)):
            piece = self.board[square]
            if piece != 0 and piece != 7:
                piece = PieceToDraw(square, STONECOLORS[piece], self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
                if (self.stone_centering == 0):
                    piece.draw(self.offsets[square], win)
                else:
                    piece.draw([0, 0], win)
                    
    def remove(self, pieces): # unused
        for piece in pieces:
            # self.board[self.calc_square(piece.row, piece.col)] = 0
            self.board[piece.square] = 0

    def winner(self):
        return None 
    
    def count(self, square, color): # count liberties
        piece = self.board[square]
        if piece == OFFBOARD:
            return
        if piece and (piece & color) and (piece & MARKER) == 0:
            self.block.append(square)
            self.board[square] |= MARKER
            self.count(square - (self.cols+2), color)   # walk north
            self.count(square - 1, color)               # walk east
            self.count(square + (self.cols+2), color)   # walk south
            self.count(square + 1, color)               # walk west
        elif piece == EMPTY:
            self.board[square] |= LIBERTY
            self.liberties.append(square)

    def clear_block(self):
        for captured in self.block:
            self.board[captured] = EMPTY

    def clear_groups(self):
        self.block = []
        self.liberties = []

    def clear_board(self):
        self.clear_groups()
        for square in range(len(self.board)):
            if self.board[square] != OFFBOARD: self.board[square] = 0

    def restore_board(self):
        self.clear_groups()
        for square in range((self.rows+2) * (self.cols+2)):
            if self.board[square] != OFFBOARD: 
                self.board[square] &= 3

    def captures(self, color):
        for square in range(len(self.board)):
            piece = self.board[square]
            if piece == OFFBOARD:
                continue
            if piece & color:
                self.count(square, color)
                if len(self.liberties) == 0:
                    self.clear_block()
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('goha/soundeffects/stonescaptured.wav'))
                self.restore_board()

    def find_legal_moves(self, color):
        self.legal_moves = []
        self.board_copy = self.board.copy()
        for square in range(len(self.board)):
            piece = self.board[square]
            if piece != EMPTY:
                continue
            else:
                self.place2(square, color)
                
                neighbours = [square - (self.cols+2), square - 1, square + (self.cols+2), square + 1] # captures but only for neighbours
                for square2 in neighbours:
                    piece = self.board[square2]
                    if piece == OFFBOARD:
                        continue
                    if piece & (3- color):
                        self.count(square2, (3 - color))
                        if len(self.liberties) == 0:
                            self.clear_block()
                        self.restore_board()

                self.count(square, color)
                if len(self.liberties) != 0:
                    self.legal_moves.append(square)
                self.clear_groups()
                self.board = self.board_copy.copy()

    def detect_edge(self, square):
        neighbours = [square - (self.cols+2), square - 1, square + (self.cols+2), square + 1]
        for neighbour in neighbours:
            if self.board[neighbour] == OFFBOARD: 
                return 1
        return 0

    def evaluate(self, color):
        best_count = 0
        best_liberty = False
        # loop over the liberties within the list
        for liberty in self.liberties:
            # put stone on board
            self.board[liberty] = color
            # count new liberties
            self.count(liberty, color)
            # found more liberties
            if len(self.liberties) > best_count and not self.detect_edge(liberty) and liberty in self.legal_moves:
                best_liberty = liberty
                best_count = len(self.liberties)     
            # restore board
            self.restore_board()
            # remove stone off board
            self.board[liberty] = EMPTY
        # return best liberty
        return best_liberty