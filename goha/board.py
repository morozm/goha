import pygame, random
from .constants import OFFBOARD, MARKER, EMPTY, LIBERTY, BOARDS, STONECOLORS, BLACKCOLOR, BROWNCOLOR, WIDTH, HEIGHT, BLACK, WHITE
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
        self.territory = [[], [], [], []]
        self.board_size = board_size
        self.territory_drawn = False
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
    
    def draw_dots(self, win):
        if (self.board_size == 0):
            self.draw_dot(win, 2, 6)
            self.draw_dot(win, 6, 2)
            self.draw_dot(win, 6, 6)
            self.draw_dot(win, 2, 2)
            self.draw_dot(win, 4, 4)
            self.draw_dot(win, 4, 2)
            self.draw_dot(win, 4, 6)
            self.draw_dot(win, 2, 4)
            self.draw_dot(win, 6, 4)
        elif self.board_size == 1:
            self.draw_dot(win, 3, 9)
            self.draw_dot(win, 9, 3)
            self.draw_dot(win, 9, 9)
            self.draw_dot(win, 3, 3)
            self.draw_dot(win, 6, 6)
            self.draw_dot(win, 6, 3)
            self.draw_dot(win, 6, 9)
            self.draw_dot(win, 3, 6)
            self.draw_dot(win, 9, 6)
        elif self.board_size == 2:
            self.draw_dot(win, 3,  15)
            self.draw_dot(win, 15, 3 )
            self.draw_dot(win, 15, 15)
            self.draw_dot(win, 3,  3 )
            self.draw_dot(win, 9,  9 )
            self.draw_dot(win, 9,  3 )
            self.draw_dot(win, 9,  15)
            self.draw_dot(win, 3,  9 )
            self.draw_dot(win, 15, 9 )

    def draw_dot(self, win, row, col):
        pygame.draw.circle(win, BLACKCOLOR, (col*self.square_size + self.square_size//2 + self.board_width_offset, row*self.square_size + self.square_size//2 + self.board_height_offset), 10)

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
        self.draw_dots(win)
        for square in range (len(self.board)):
            piece = self.board[square]
            if piece != 0 and piece != 7:
                piece = PieceToDraw(square, STONECOLORS[piece], self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
                if (self.stone_centering == 0):
                    piece.draw(self.offsets[square], win)
                else:
                    piece.draw([0, 0], win)

    def draw_territory(self, win):
        if self.territory_drawn == True:
            for square in range (len(self.board)):
                if square in self.territory[BLACK]:
                    piece = PieceToDraw(square, STONECOLORS[BLACK], self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
                    if (self.stone_centering == 0):
                        piece.draw_territory(self.offsets[square], win)
                    else:
                        piece.draw_territory([0, 0], win)
                elif square in self.territory[WHITE]:
                    piece = PieceToDraw(square, STONECOLORS[WHITE], self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
                    if (self.stone_centering == 0):
                        piece.draw_territory(self.offsets[square], win)
                    else:
                        piece.draw_territory([0, 0], win)
                elif self.board[square] != 7 and self.board[square] != BLACK and self.board[square] != WHITE:
                    piece = PieceToDraw(square, (128, 128, 128), self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
                    if (self.stone_centering == 0):
                        piece.draw_territory(self.offsets[square], win)
                    else:
                        piece.draw_territory([0, 0], win)

    def draw_last_move(self, win, square):
        if square != None:
            piece = self.board[square]
            if piece == 1 or piece == 2:
                piece = PieceToDraw(square, STONECOLORS[3 - piece], self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
                if (self.stone_centering == 0):
                    piece.draw_last_move(self.offsets[square], win)
                else:
                    piece.draw_last_move([0, 0], win)
    
    def draw_hover_piece(self, win, square, color):
        if self.board[square] == 0:
            piece = PieceToDraw(square, STONECOLORS[color], self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
            if (self.stone_centering == 0):
                piece.draw_hover_piece(self.offsets[square], win)
            else:
                piece.draw_hover_piece([0, 0], win)
                    
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
            self.count(square - 1, color)               # walk west
            self.count(square + (self.cols+2), color)   # walk south
            self.count(square + 1, color)               # walk east
        elif piece == EMPTY:
            self.board[square] |= LIBERTY
            self.liberties.append(square)

    def count_territory(self):
        self.territory[BLACK] = []
        self.territory[WHITE] = []
        for square in range(len(self.board)):
            notwhite = notblack = False
            self.count_territory2(square)
            for i in self.territory[3]:
                if self.board[i] == BLACK:
                    notwhite = True
                elif self.board[i] == WHITE:
                    notblack = True
            if (notwhite and notblack): # noones terriotry
                pass    
            elif (notwhite): # blacks terriotry
                self.territory[BLACK] += (self.territory[0].copy())
            elif (notblack): # whites territory
                self.territory[WHITE] += (self.territory[0].copy())
            self.territory[0] = []
            self.territory[3] = []
        self.restore_board()

    def count_territory2(self, square):
        piece = self.board[square]
        if piece == EMPTY:
            self.territory[0].append(square)
            self.board[square] |= MARKER
            self.count_territory2(square - (self.cols+2))   # walk north
            self.count_territory2(square - 1)               # walk west
            self.count_territory2(square + (self.cols+2))   # walk south
            self.count_territory2(square + 1)               # walk east
        elif piece == BLACK or piece == WHITE:
            self.territory[3].append(square)
        else:
            return

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
        captured = 0
        for square in range(len(self.board)):
            piece = self.board[square]
            if piece == OFFBOARD:
                continue
            if piece & color:
                self.count(square, color)
                if len(self.liberties) == 0:
                    self.clear_block()
                    captured += len(self.block)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('goha/soundeffects/stonescaptured.wav'))
                self.restore_board()
        return captured

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

    def acknowledge_super_ko(self, board_history, color):
        self.board_copy = self.board.copy()
        for square in self.legal_moves:
            piece = self.board[square]
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
            positions = [i for i in range(len(board_history)) if i % 2 == 2-color]
            for i in positions:
                if self.board == board_history[i]:
                    self.legal_moves.remove(square)
            self.board = self.board_copy.copy()

    def detect_edge(self, square):
        neighbours = [square - (self.cols+2), square - 1, square + (self.cols+2), square + 1]
        for neighbour in neighbours:
            if self.board[neighbour] == OFFBOARD: 
                return 1
        return 0

    def evaluate_0(self, color): # find a liberty with best count
        best_count = 0
        best_liberty = False
        # loop over the liberties within the list
        for liberty in self.liberties:
            # put stone on board
            self.board[liberty] = color
            # count new liberties
            self.count(liberty, color)
            # found more liberties
            if len(self.liberties) > best_count and liberty in self.legal_moves:
                best_liberty = liberty
                best_count = len(self.liberties)     
            # restore board
            self.restore_board()
            # remove stone off board
            self.board[liberty] = EMPTY
        # return best liberty
        return best_liberty
    
    def evaluate_1(self, color): # find a liberty with best count > 1 AND not on the edge
        best_count = 1
        best_liberty = False
        current_liberties = self.liberties.copy()
        for liberty in current_liberties:
            self.restore_board()
            self.board[liberty] = color
            self.count(liberty, color)
            # self.print_board() # test
            if len(self.liberties) > best_count and not self.detect_edge(liberty) and liberty in self.legal_moves:
                best_liberty = liberty
                best_count = len(self.liberties)     
            self.restore_board()
            self.board[liberty] = EMPTY
        return best_liberty
    
    def evaluate_2(self, color): # find a liberty with best count BUT it cant have less than 2 liberties itself
        best_count = 0
        best_liberty = False
        current_liberties = self.liberties.copy()
        for liberty in current_liberties:
            self.restore_board()
            self.board[liberty] = color    
            self.count(liberty, color)
            liberties_length = len(self.liberties)
            # self.print_board() # test
            if liberties_length > best_count:
                self.restore_board()
                self.board[liberty] = 3 - color
                self.count(liberty, 3 - color)
                # self.print_board() # test
                if len(self.liberties) > 1:
                    best_liberty = liberty
                    best_count = liberties_length
            self.restore_board()
            self.board[liberty] = EMPTY
        return best_liberty
    
    def print_board(self):
        files = '     a b c d e f g h j k l m n o p q r s t'
        pieces = '.#o  bw +'
        for row in range(BOARDS[self.board_size][1] + 2):
            for col in range(BOARDS[self.board_size][1] + 2):
                square = row * (BOARDS[self.board_size][1] + 2) + col
                stone = self.board[square]
                if col == 0 and row > 0 and row < BOARDS[self.board_size][1] + 2 - 1:
                    rank = BOARDS[self.board_size][1] + 2 - 1 - row
                    space = '  ' if len(self.board) == 121 else '   '
                    print((space if rank < 10 else '  ') + str(rank), end='')
                print(pieces[stone] + ' ', end='')    
            print()
        print(('' if len(self.board) == 121 else ' ') + files[0:(BOARDS[self.board_size][1] + 2)*2] + '\n')