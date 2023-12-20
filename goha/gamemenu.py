import pygame
import sys
from .constants import WIDTH, HEIGHT, GREYCOLOR, PADDING, OUTLINE, STONECOLORS
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

        self.name_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 20)
        self.score_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 30)

        self.usericon = pygame.image.load("goha/assets/usericon64.png")
        self.boticon = pygame.image.load("goha/assets/boticon64.png")
        self.passicon = pygame.image.load("goha/assets/hand-shake32.png")
        self.resignicon = pygame.image.load("goha/assets/white-flag32.png")

        self.button_width = 70
        self.button_height = 40
        self.button_pass_rect =     pygame.Rect((WIDTH - self.game.board.square_size*self.game.board.cols) // 4 - self.button_width // 2 - 20, HEIGHT * 3 // 4 + 150, self.button_width, self.button_height)
        self.button_resign_rect =   pygame.Rect((WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + self.button_width // 2 + 20, HEIGHT * 3 // 4 + 150, self.button_width, self.button_height)
        self.button_pass_rect.center = ((WIDTH - self.game.board.square_size*self.game.board.cols) // 4 - self.button_width // 2 - 20, HEIGHT * 3 // 4 + 150)
        self.button_resign_rect.center = ((WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + self.button_width // 2 + 20, HEIGHT * 3 // 4 + 150)

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
        self.game.board.draw(self.win)
        self.draw_icon(self.win, self.usericon, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4, 64, 64)
        self.draw_icon(self.win, self.boticon,  (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4, 64, 64)
        self.draw_name(self.win, self.username_input_text,                                      (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4 + 50)
        self.draw_name(self.win, self.language['Difficulties'][self.game.opponent_difficulty],  (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4 - 50)
        self.draw_score(self.win, 1, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4 - 60)
        self.draw_score(self.win, 2, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4 + 60)
        self.draw_current_player_move(self.win, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + 100, HEIGHT * 1 // 4)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_pass_hovered = self.button_pass_rect.collidepoint(mouse_x, mouse_y)
        self.is_resign_hovered = self.button_resign_rect.collidepoint(mouse_x, mouse_y)
        self.draw_button(self.win, self.passicon,   (WIDTH - self.game.board.square_size*self.game.board.cols) // 4 - self.button_width // 2 - 20, HEIGHT * 3 // 4 + 150, self.button_width, self.button_height, self.is_pass_hovered)
        self.draw_button(self.win, self.resignicon, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + self.button_width // 2 + 20, HEIGHT * 3 // 4 + 150, self.button_width, self.button_height, self.is_resign_hovered)

    def draw_icon(self, screen, icon, x, y, width, height):
        icon_rect = pygame.Rect(0, 0, width, height)
        icon_rect2 = pygame.Rect(0, 0, width + 8, height + 8)
        icon_rect.center = (x, y)
        icon_rect2.center = (x, y)
        pygame.draw.rect(screen, self.theme['maincolor1'], icon_rect2, border_radius=10)
        pygame.draw.rect(screen, self.theme['backgroundcolor'], icon_rect, border_radius=10)
        icon = pygame.transform.scale(icon, (icon_rect.width, icon_rect.height))
        screen.blit(icon, icon_rect)

    def draw_name(self, screen, text, x, y):
        text_surface = self.name_font.render(text, True, self.theme['maincolor1'])
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw_score(self, screen, player, x, y):
        if self.game.player_color == 2: player = 3 - player
        text_surface = self.score_font.render(str(self.game.score[player]), True, self.theme['maincolor1'])
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw_button(self, screen, icon, x, y, width, height, is_hovered):
        backgroundcolor = self.theme['maincolor2'] if is_hovered else self.theme['backgroundcolor']
        icon_rect = pygame.Rect(0, 0, 32, 32)
        button_rect = pygame.Rect(0, 0, width+8, height+8)
        button_rect2 = pygame.Rect(0, 0, width, height)
        icon_rect.center = (x, y)
        button_rect.center = (x, y)
        button_rect2.center = (x, y)
        pygame.draw.rect(screen, self.theme['maincolor1'], button_rect, border_radius=10)
        pygame.draw.rect(screen, backgroundcolor, button_rect2, border_radius=10)
        screen.blit(icon, icon_rect)

    def draw_current_player_move(self, screen, x, y):
        color = STONECOLORS[self.game.turn]
        radius = round((100 - PADDING)/100 * self.game.board.square_size / 2)
        if (self.game.player_color == self.game.turn):
            add_height = y*2
        else:
            add_height = 0
        pygame.draw.circle(screen, GREYCOLOR, (x, y+add_height), (radius + OUTLINE))
        pygame.draw.circle(screen, color, (x, y+add_height), radius)

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
                        if (self.game.opponent_difficulty != 4): # if not playing solo
                            self.game.opponent_moves()
                            self.game.process_move()
                        self.game.board.print_board()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False     