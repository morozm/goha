import pygame, random
from .constants import OFFBOARD, MARKER, EMPTY, LIBERTY, BOARDS, STONECOLORS, BLACKCOLOR, BROWNCOLOR, WIDTH, HEIGHT, BLACK, WHITE
from .piecetodraw import PieceToDraw
from .settings import Settings
BOARD_MENU_SPACE = 50
BOARD_EDGE_SPACE = 20

class Boardsimple:
    def __init__(self, board_size):
        self.board = []
        self.board_copy = []
        self.block = []
        self.liberties = []
        self.legal_moves = []
        self.territory = [[], [], [], []]
        self.estimation = []
        self.board_size = board_size
        self._init()

    def _init(self):
        self.board = BOARDS[self.board_size][0].copy()
        self.rows, self.cols = BOARDS[self.board_size][1], BOARDS[self.board_size][2]
        self.square_size = min((WIDTH-BOARD_MENU_SPACE)//self.cols, (HEIGHT-BOARD_MENU_SPACE)//self.rows)
        self.board_height_offset = max(0, (HEIGHT - self.square_size*self.rows)//2)
        self.board_width_offset = max(0, (WIDTH - self.square_size*self.cols)//2)
        self.estimation = [0] * ((BOARDS[self.board_size][1]+2)*(BOARDS[self.board_size][2]+2))

    def calc_square(self, row, col):
        return (row+1)*(self.cols+2)+col+1
    
    def calc_row_col(self, square):
        cols_with_padding = self.cols + 2
        row = square // cols_with_padding - 1
        col = square % cols_with_padding - 1
        return row, col

    def place(self, row, col, turn):
        self.place2(self.calc_square(row, col), turn)

    def place2(self, square, turn):
        self.board[square] = turn
    
    def get_piece(self, row, col):
        return self.board[self.calc_square(row, col)]
    
    def set_piece(self, square, stone):
        self.board[square] = stone
    
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
    
    def estimate_move_power(self, color):
        self.estimation = [[0] * 7 for _ in range((BOARDS[self.board_size][1]+2)*(BOARDS[self.board_size][2]+2))] #[capture, save, defend, surround, on territory, od edge]
        for square in range(len(self.board)):
            piece = self.board[square]
            if piece == OFFBOARD:
                continue

            if piece & (3 - color):         # capture
                self.count(square, (3 - color))
                if len(self.liberties) == 1 and (self.liberties[0] in self.legal_moves):
                    if self.estimation[self.liberties[0]][0] < 2*(len(self.block)+3):
                        self.estimation[self.liberties[0]][0] = 2*(len(self.block)+3)
                self.restore_board()

            if piece & (color):             # save
                self.count(square, color)
                if len(self.liberties) == 1 and (self.liberties[0] in self.legal_moves):
                    length = len(self.block)
                    current_liberties = self.liberties.copy()
                    self.restore_board()
                    for liberty in current_liberties:
                        self.board[liberty] = color
                        self.count(liberty, color)
                        if len(self.liberties) > 1 and liberty in self.legal_moves:
                            if self.estimation[self.liberties[0]][1] < 2*(length+2):
                                self.estimation[liberty][1] = 2*(length+2)    
                        self.restore_board()
                        self.board[liberty] = EMPTY
                self.restore_board()

            if piece & color:               # defend
                self.count(square, color)
                if len(self.liberties) == 2:
                    length = len(self.block)
                    current_liberties = self.liberties.copy()
                    self.restore_board()
                    for liberty in current_liberties:
                        self.board[liberty] = color
                        self.count(liberty, color)
                        if len(self.liberties) > 1 and liberty in self.legal_moves:
                            if self.estimation[self.liberties[0]][2] < (length+1):
                                self.estimation[liberty][2] = (length+1)    
                        self.restore_board()
                        self.board[liberty] = EMPTY
                self.restore_board()

            if piece & (3 - color):         # surround
                self.count(square, (3 - color))
                if len(self.liberties) > 1:
                    current_liberties = self.liberties.copy()
                    self.restore_board()
                    for liberty in current_liberties:
                        self.board[liberty] = color
                        self.count(liberty, color)
                        if len(self.liberties) > 1:
                            self.estimation[liberty][3] = 1
                        self.restore_board()
                        self.board[liberty] = EMPTY
                self.restore_board()

            if square in self.territory[BLACK] or square in self.territory[WHITE]:
                self.estimation[square][4] = -1

            if self.detect_edge(square):
                self.estimation[square][5] = -1

            row, col = self.calc_row_col(square)
            self.estimation[square][6] = -round((abs((self.rows-1)/2 - row)/(self.rows-1)/4 + abs((self.cols-1)/2 - col)/(self.cols-1)/4), 3)

        self.estimation = [sum(row) for row in self.estimation]
        # print(self.estimation)

    def take_top_estimation(self, how_many):
        estimation_available_moves = []
        for i in range(len(self.legal_moves)):
            estimation_available_moves.append(self.estimation[self.legal_moves[i]])
        moves_estimation_dict = dict(zip(self.legal_moves, estimation_available_moves))
        sorted_moves_estimation = sorted(moves_estimation_dict.items(), key=lambda item: item[1], reverse=True)
        top_moves = sorted_moves_estimation[:how_many]
        top_moves = [element[0] for element in top_moves]
        # print(top_moves)
        return top_moves
    
    def draw_green_circle(self, win, square):
        piece = PieceToDraw(square, (0, 255, 0), self.rows, self.cols, self.square_size, self.board_height_offset, self.board_width_offset)
        piece.draw_green_circle([0, 0], win)