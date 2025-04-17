import pygame
from .board import Board
from .clock import Clock
from .gamesimple import Gamesimple
from .opponent import Opponent
from .settings import Settings
from .constants import BLACK, WHITE
from .utils import resource_path

class Game:
    def __init__(self, win, opponent_difficulty=0, player_color=0, handicap=0, time=0, board_size=0):
        self.win = win
        self.opponent_difficulty = opponent_difficulty
        self.player_color = player_color + 1
        self.handicap = handicap
        self.time = time
        self.board_size = board_size
        self.info_text = ['', '']
        self.settings = Settings()
        self.load_settings()
        self._init()

    def _init(self):
        self.board = Board(self.board_size)
        self.opponent = Opponent(self.opponent_difficulty)
        self.player_clock = Clock(self.time)
        self.oponent_clock = Clock(self.time)
        self.turn = BLACK
        self.turn_number = 1
        self.board_history = [self.board.board.copy()]
        self.score = [None, 0, 0]
        self.last_move = None
        self.gamestate = 'active'
        self.board.find_legal_moves(self.turn)
        self.board.estimate_move_power(self.turn)
        self.board.print_estimation()
        self.check_if_legal_moves_exist()
        self.place_whole_handicap()
        self.initialize_score()

    def load_settings(self):
        self.settings.load_settings()
        self.language = self.settings.get_language()

    def reset(self):
        self._init()

    def place(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece == 0:
            if self.board.calc_square(row, col) in self.board.legal_moves:
                self.board.place(row, col, self.turn)
                self.last_move = self.board.calc_square(row, col)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/stoneplaced.wav')))
                return True
            else:
                print('place is illegal')
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/incorrectmove.wav')))
                return False
        else:
            print('place is occupied')
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/incorrectmove.wav')))
            return False
    
    def process_move(self):
        captured = self.board.captures(3 - self.turn)
        self.score[self.turn] += captured
        self.change_turn()
        self.turn_number += 1
        self.board_history.append(self.board.board.copy())
        self.board.find_legal_moves(self.turn)
        self.board.acknowledge_super_ko(self.board_history, self.turn)
        self.board.count_territory()
        self.board.estimate_move_power(self.turn) # optional
        if (self.turn == self.player_color):
            self.oponent_clock.pause()
            self.oponent_clock.add_time()
            self.player_clock.resume()
        else:
            self.player_clock.pause()
            self.player_clock.add_time()
            self.oponent_clock.resume()
        self.check_if_legal_moves_exist()
        if self.turn_number > 2:
            if (self.board_history[-1] == self.board_history[-3]):
                print('Both players passed!')
                self.end_game()
        self.board.print_board()
        self.board.print_estimation()

    def end_game(self):
        self.gamestate = 'inactive'
        self.board.territory_drawn = True
        self.player_clock.pause()
        self.oponent_clock.pause()
        self.score[BLACK] += len(self.board.territory[BLACK])
        self.score[WHITE] += len(self.board.territory[WHITE])
        if self.score[self.player_color] < self.score[3-self.player_color] and self.opponent_difficulty != 4:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/gamelost.wav')))
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/gamewon.wav')))
        self.info_text[0] = self.language['Game ends.']
        self.info_text[1] = str(self.score[BLACK]) + ' - ' + str(self.score[WHITE])

    def end_game_by_time(self):
        self.gamestate = 'inactive'
        self.board.territory_drawn = True
        self.player_clock.pause()
        self.oponent_clock.pause()
        if self.player_clock.miliseconds == 0 and self.opponent_difficulty != 4:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/gamelost.wav')))
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/gamewon.wav')))
        if self.player_clock.miliseconds == 0:
            if self.player_color == BLACK:
                self.info_text[0] = self.language['Game ends. White won.']
                self.info_text[1] = self.language['(Black ran out of time.)']
            elif self.player_color == WHITE:
                self.info_text[0] = self.language['Game ends. Black won.']
                self.info_text[1] = self.language['(White ran out of time.)']
        elif self.oponent_clock.miliseconds == 0:
            if self.player_color == BLACK:
                self.info_text[0] = self.language['Game ends. Black won.']
                self.info_text[1] = self.language['(White ran out of time.)']
            elif self.player_color == WHITE:
                self.info_text[0] = self.language['Game ends. White won.']
                self.info_text[1] = self.language['(Black ran out of time.)']

    def end_game_by_resignation(self):
        self.gamestate = 'inactive'
        self.board.territory_drawn = True
        self.player_clock.pause()
        self.oponent_clock.pause()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(resource_path('soundeffects/gamelost.wav')))
        self.info_text[0] = self.language['Game ends.']
        self.info_text[1] = self.language['Player resigned.']

    def opponent_moves(self):
        if self.gamestate == 'active':
            move = self.opponent.gen_move(self.turn, self.board, self)
            if move != None:
                self.last_move = move
    
    def simple_copy(self):
        copy = Gamesimple(self.player_color, self.board_size)

        copy.board.board = self.board.board.copy()
        copy.board.board_copy = self.board.board_copy.copy()
        copy.board.block = self.board.block.copy()
        copy.board.liberties = self.board.liberties.copy()
        copy.board.legal_moves = self.board.legal_moves.copy()
        copy.board.territory = self.board.territory.copy()
        copy.board.estimation = self.board.estimation.copy()

        copy.turn = self.turn
        copy.board_history = self.board_history.copy()
        copy.score = self.score.copy()
        copy.last_move = self.last_move
        copy.gamestate = self.gamestate

        return copy

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
    
    def check_if_legal_moves_exist(self):
        if len(self.board.legal_moves) == 0:
            print('No more legal moves!')
            self.end_game()
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
        if self.handicap > 1:
            self.change_turn()

    def place_handicap_stone(self, row, col):
        if self.handicap_copy > 0:
            if self.handicap != 1:
                self.place(row, col)
            self.handicap_copy -= 1

    def initialize_score(self):
        self.score[BLACK] = 0.0
        if (self.handicap == 0):
            self.score[WHITE] = 6.5
        else: 
            self.score[WHITE] = 0.5