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
        self.move_time = pygame.time.get_ticks()
        self._init()

    def _init(self):
        self.rows = self.game.board.rows
        self.cols = self.game.board.cols
        self.square_size = self.game.board.square_size
        self.board_height_offset = self.game.board.board_height_offset
        self.board_width_offset = self.game.board.board_width_offset

        self.name_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 20)
        self.score_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 30)
        self.info_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 20)

        self.usericon = pygame.image.load("goha/assets/usericon64.png")
        self.boticon = pygame.image.load("goha/assets/boticon64.png")
        self.passicon = pygame.image.load("goha/assets/hand-shake32.png")
        self.resignicon = pygame.image.load("goha/assets/white-flag32.png")
        self.toolsicon = pygame.image.load("goha/assets/settings32.png")
        self.menuicon = pygame.image.load("goha/assets/menu32.png")

        self.button_width = 70
        self.button_height = 40
        self.button_pass_rect =     pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_resign_rect =   pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_tools_rect =    pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_menu_rect =     pygame.Rect(0, 0, self.button_width, self.button_width)
        self.button_pass_rect.center =      ((WIDTH - self.game.board.square_size*self.game.board.cols) // 4 - self.button_width // 2 - 20,     HEIGHT * 3 // 4 + 150)
        self.button_resign_rect.center =    ((WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + self.button_width // 2 + 20,     HEIGHT * 3 // 4 + 150)
        self.button_tools_rect.center =     ((WIDTH * 3 + self.game.board.square_size*self.game.board.cols) // 4,                               HEIGHT * 3 // 4 + 150)
        self.button_menu_rect.center =      (WIDTH - self.button_width, self.button_width)

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
        self.game.board.draw_last_move(self.win, self.game.last_move)
        self.game.board.draw_territory(self.win)
        self.draw_icon(self.win, self.usericon, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4, 64, 64)
        self.draw_icon(self.win, self.boticon,  (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4, 64, 64)
        self.draw_name(self.win, self.username_input_text,                                      (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4 + 50)
        self.draw_name(self.win, self.language['Difficulties'][self.game.opponent_difficulty],  (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4 - 50)
        self.draw_score(self.win, 1, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4 - 60)
        self.draw_score(self.win, 2, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4 + 60)
        self.draw_current_player_move(self.win, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + 100, HEIGHT * 1 // 4)
        self.game.player_clock.draw(self.win, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 3 // 4 - 140, 120, 60, self.theme['maincolor1'], self.theme['backgroundcolor'])
        self.game.oponent_clock.draw(self.win, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 4 + 140, 120, 60, self.theme['maincolor1'], self.theme['backgroundcolor'])
        self.draw_info_text(self.win, (WIDTH * 3 + self.game.board.square_size*self.game.board.cols) // 4, HEIGHT * 1 // 2, 340, 100, self.game.info_text[0], self.game.info_text[1], self.theme['maincolor1'], self.theme['backgroundcolor'])

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_pass_hovered = self.button_pass_rect.collidepoint(mouse_x, mouse_y)
        self.is_resign_hovered = self.button_resign_rect.collidepoint(mouse_x, mouse_y)
        self.is_tools_hovered = self.button_tools_rect.collidepoint(mouse_x, mouse_y)
        self.is_menu_hovered = self.button_menu_rect.collidepoint(mouse_x, mouse_y)
        self.draw_button(self.win, self.passicon,   (WIDTH - self.game.board.square_size*self.game.board.cols) // 4 - self.button_width // 2 - 20,      HEIGHT * 3 // 4 + 150, self.button_width, self.button_height, self.is_pass_hovered)
        self.draw_button(self.win, self.resignicon, (WIDTH - self.game.board.square_size*self.game.board.cols) // 4 + self.button_width // 2 + 20,      HEIGHT * 3 // 4 + 150, self.button_width, self.button_height, self.is_resign_hovered)
        self.draw_button(self.win, self.toolsicon,  (WIDTH * 3 + self.game.board.square_size*self.game.board.cols) // 4,                                HEIGHT * 3 // 4 + 150, self.button_width, self.button_height, self.is_tools_hovered)
        self.draw_button(self.win, self.menuicon,   WIDTH - self.button_width, self.button_width, self.button_width, self.button_width, self.is_menu_hovered)
        if (self.get_row_col_from_mouse((mouse_x, mouse_y)) != False and self.game.gamestate == 'active'):
            if (self.game.turn == self.game.player_color) or self.game.opponent_difficulty == 4:
                row, col = self.get_row_col_from_mouse((mouse_x, mouse_y))
                square = self.game.board.calc_square(row, col)
                if square in self.game.board.legal_moves:
                    self.draw_hover_piece(self.win, square)

    def draw_hover_piece(self, screen, square):
        self.game.board.draw_hover_piece(screen, square, self.game.turn)

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
    
    def draw_info_text(self, screen, x, y, width, height, text1, text2, color1, color2):
        if (text1 != ''):
            rect1 = pygame.Rect(0, 0, width+8, height+8)
            rect2 = pygame.Rect(0, 0, width, height)
            rect1.center = (x, y)
            rect2.center = (x, y)
            pygame.draw.rect(screen, color1, rect1, border_radius=0)
            pygame.draw.rect(screen, color2, rect2, border_radius=0)
            text1 = self.info_font.render(text1, True, color1)
            text2 = self.info_font.render(text2, True, color1)
            screen.blit(text1, (x - text1.get_width()//2, y - text1.get_height()))
            screen.blit(text2, (x - text2.get_width()//2, y))

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
                if (self.button_pass_rect.collidepoint(event.pos) and self.game.gamestate == 'active' and (self.game.turn == self.game.player_color or self.game.opponent_difficulty == 4)):
                    self.move_time = pygame.time.get_ticks()
                    self.game.process_move()
                if (self.button_resign_rect.collidepoint(event.pos) and self.game.gamestate == 'active' and (self.game.turn == self.game.player_color or self.game.opponent_difficulty == 4)):
                    self.game.end_game_by_resignation()
                if (self.button_tools_rect.collidepoint(event.pos)):
                    self.game.board.territory_drawn = not self.game.board.territory_drawn
                if (self.button_menu_rect.collidepoint(event.pos)):
                    self.running = False
                pos = pygame.mouse.get_pos()
                if (self.get_row_col_from_mouse(pos) != False and self.game.gamestate == 'active' and (self.game.turn == self.game.player_color or self.game.opponent_difficulty == 4)):
                    row, col = self.get_row_col_from_mouse(pos)
                    if self.game.place(row, col):
                        self.move_time = pygame.time.get_ticks()
                        self.game.process_move()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        if self.game.player_color == self.game.turn:
            self.move_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.move_time >= 500:
            if (self.game.opponent_difficulty != 4 and self.game.gamestate == 'active'): # if not playing solo
                self.game.opponent_moves()
                self.game.process_move()
        
        if self.game.time != 0 and self.game.gamestate == 'active':
            if self.game.player_clock.miliseconds == 0 or self.game.oponent_clock.miliseconds == 0:
                self.game.end_game_by_time()