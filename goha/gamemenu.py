import pygame
import sys
from .settings import Settings

class Gamemenu:
    def __init__(self, win, game):
        self.win = win
        self.game = game
        self.settings = Settings()
        self.load_settings()
        self.running = False
        self._init()

    def _init(self):
        self.rows = self.game.board.rows
        self.cols = self.game.board.cols
        self.square_size = self.game.board.square_size
        self.board_height_offset = self.game.board.board_height_offset
        self.board_width_offset = self.game.board.board_width_offset

    def adjust_game_settings(self, difficulty, player_color, handicap, time, board_size):
        self.game.turn = player_color - 1

    def load_settings(self):
        self.game.board.load_settings()
        self.settings.load_settings()
        self.username_input_text = self.settings.get_username()
        self.theme_select_text = self.settings.get_selected_theme()
        self.theme = self.settings.get_theme()
        self.language_select_text = self.settings.get_selected_language()
        self.language = self.settings.get_language()
        self.stone_centering = self.settings.get_stone_centering()
        self.volume = self.settings.get_volume()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = (y - self.board_height_offset) // self.square_size
        col = (x - self.board_width_offset) // self.square_size
        if (row<0 or col<0 or row>=self.rows or col>=self.cols):
            return False
        return row, col
    
    def draw_game_menu(self):
        if self.game.winner() != None:
            print(self.game.winner())
            self.running = False
        self.game.update()

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (self.get_row_col_from_mouse(pos) != False and self.game.gamestate == 'active'):
                    row, col = self.get_row_col_from_mouse(pos)
                    if self.game.place(row, col):
                        self.game.process_move()
                        self.game.board.print_board()
                        self.game.opponent_moves()
                        self.game.process_move()
                        self.game.board.print_board()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False     