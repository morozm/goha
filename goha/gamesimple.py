from .boardsimple import Boardsimple
from .constants import BLACK, WHITE
from copy import deepcopy

class Gamesimple:
    def __init__(self, player_color=0, board_size=0):
        self.player_color = player_color + 1
        self.board_size = board_size
        self._init()

    def _init(self):
        self.board = Boardsimple(self.board_size)
        self.turn = BLACK
        self.board_history = [self.board.board.copy()]
        self.score = [None, 0, 0]
        self.last_move = None
        self.gamestate = 'active'
        self.board.find_legal_moves(self.turn)
        self.board.estimate_move_power(self.turn)
        print(self.board.take_top_estimation(5))
        self.check_if_legal_moves_exist()

    def check_if_legal_moves_exist(self):
        if len(self.board.legal_moves) == 0:
            self.end_game()
            return False
        else:
            return True

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def end_game(self):
        self.gamestate = 'inactive'
        self.score[BLACK] += len(self.board.territory[BLACK])
        self.score[WHITE] += len(self.board.territory[WHITE])

    def place(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece == 0:
            if self.board.calc_square(row, col) in self.board.legal_moves:
                self.board.place(row, col, self.turn)
                self.last_move = self.board.calc_square(row, col)
                return True
            else:
                return False
        else:
            return False
        
    def bot3_move(self, move):
        self.board.place2(move, self.turn)
        captured = self.board.captures(3 - self.turn)
        self.score[self.turn] += captured
        self.change_turn()
        self.board_history.append(self.board.board.copy())
        self.board.find_legal_moves(self.turn)
        self.board.acknowledge_super_ko(self.board_history, self.turn)
        self.board.count_territory()
        self.board.estimate_move_power(self.turn)
        self.check_if_legal_moves_exist()

        return self.board
    
    def simple_copy(self):
        return deepcopy(self)