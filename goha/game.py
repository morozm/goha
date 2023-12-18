import pygame
from .board import Board
from .opponent import Opponent
from .constants import BLACK, WHITE, BLUECOLOR

class Game:
    def __init__(self, win, opponent_difficulty=0, player_color=0, handicap=0, time=0, board_size=0):
        self.win = win
        self.opponent_difficulty = opponent_difficulty
        self.player_color = player_color + 1
        self.handicap = handicap
        self.time = time
        self.board_size = board_size
        self._init()

    def _init(self):
        self.board = Board(self.board_size)
        self.opponent = Opponent(self.opponent_difficulty)
        self.turn = BLACK
        self.gamestate = 'active'
        self.board.find_legal_moves(self.turn)
        self.check_if_legal_moves_exist()
        self.place_whole_handicap()
        self.opponent_makes_first_move()
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()

    def place(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece == 0:
            if self.board.calc_square(row, col) in self.board.legal_moves:
                self.board.place(row, col, self.turn)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('goha/soundeffects/stoneplaced.wav'))
                return True
            else:
                print('place is illegal')
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('goha/soundeffects/incorrectmove.wav'))
                return False
        else:
            print('place is occupied')
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('goha/soundeffects/incorrectmove.wav'))
            return False
    
    def process_move(self):
        self.board.captures(3 - self.turn)
        self.change_turn()
        self.board.find_legal_moves(self.turn)
        self.check_if_legal_moves_exist()

    def opponent_moves(self):
        if self.gamestate == 'active':
            self.opponent.gen_move(self.turn, self.board)

    def opponent_makes_first_move(self):
        if self.gamestate == 'active' and self.player_color == 2:
            self.opponent_moves()
            self.process_move()

    # def draw_valid_moves(self, moves): #unused
    #     for move in moves:
    #         row, col = move
    #         pygame.draw.circle(self.win, BLUECOLOR, (col * SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_WIDTH_OFFSET, row * SQUARE_SIZE + SQUARE_SIZE//2 + BOARD_HEIGHT_OFFSET), SQUARE_SIZE//6)

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
    
    def check_if_legal_moves_exist(self):
        if len(self.board.legal_moves) == 0:
            print('No more legal moves! Game ends.')
            self.gamestate = 'inactive'
            return False
        else:
            return True
        
    def place_whole_handicap(self):
        self.board.find_legal_moves(self.turn)
        self.check_if_legal_moves_exist()
        self.handicap_copy = self.handicap
        if self.board_size == 0:
            self.place_handicap_stone(2, 6)
            self.place_handicap_stone(6, 2)
            self.place_handicap_stone(6, 6)
            self.place_handicap_stone(2, 2)
            self.place_handicap_stone(4, 4)
            self.place_handicap_stone(4, 2)
            self.place_handicap_stone(4, 6)
            self.place_handicap_stone(2, 4)
            self.place_handicap_stone(6, 4)
        elif self.board_size == 1:
            self.place_handicap_stone(3, 9)
            self.place_handicap_stone(9, 3)
            self.place_handicap_stone(9, 9)
            self.place_handicap_stone(3, 3)
            self.place_handicap_stone(6, 6)
            self.place_handicap_stone(6, 3)
            self.place_handicap_stone(6, 9)
            self.place_handicap_stone(3, 6)
            self.place_handicap_stone(9, 6)
        elif self.board_size == 2:
            self.place_handicap_stone(3,  15)
            self.place_handicap_stone(15, 3 )
            self.place_handicap_stone(15, 15)
            self.place_handicap_stone(3,  3 )
            self.place_handicap_stone(9,  9 )
            self.place_handicap_stone(9,  3 )
            self.place_handicap_stone(9,  15)
            self.place_handicap_stone(3,  9 )
            self.place_handicap_stone(15, 9 )
    def place_handicap_stone(self, row, col):
        if self.handicap_copy > 0:
            self.place(row, col)
            self.handicap_copy -= 1
