import pygame
import sys
from .settings import Settings
from .constants import WIDTH

class Newgamemenu:
    def __init__(self, win, game):
        self.win = win
        self.game = game
        self.settings = Settings()
        self.load_settings()
        self.running = False
        self._init()

    def _init(self):
        self.difficulty = 0
        self.player_color = 0
        self.handicap = 0
        self.time = 0
        self.board_size = 0
        self.game_settings_changed = False

        self.button_font_size = 36
        self.title_font_size = 100
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", self.button_font_size)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", self.title_font_size)

        self.options = ["Bot Difficulty", "Play As", "Handicap", "Time", "Board Size"]
        self.options_start_y = 300
        self.options_height = 60
        self.options_spacing = 20
        self.options_spacing_horizontal = 80
        self.options_input_length = 400
        
        self.triangle_spacing = 30

        self.button_width = 400
        self.button_height = 70
        self.button_spacing = 45
        self.button_start_y = 300 + 460

        self.difficulty_input_rect =    pygame.Rect(WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 0 * (self.options_height + self.options_spacing) - self.options_height // 2, self.options_input_length, self.options_height)
        self.player_color_input_rect =  pygame.Rect(WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 1 * (self.options_height + self.options_spacing) - self.options_height // 2, self.options_input_length, self.options_height)
        self.handicap_input_rect =      pygame.Rect(WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 2 * (self.options_height + self.options_spacing) - self.options_height // 2, self.options_input_length, self.options_height)
        self.time_input_rect =          pygame.Rect(WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 3 * (self.options_height + self.options_spacing) - self.options_height // 2, self.options_input_length, self.options_height)
        self.board_size_input_rect =    pygame.Rect(WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 4 * (self.options_height + self.options_spacing) - self.options_height // 2, self.options_input_length, self.options_height)

        self.button_start_rect =    pygame.Rect((WIDTH - self.button_width) // 2 - self.button_width // 2 - self.button_spacing, self.button_start_y, self.button_width, self.button_height)
        self.button_cancel_rect =   pygame.Rect((WIDTH - self.button_width) // 2 + self.button_width // 2 + self.button_spacing, self.button_start_y, self.button_width, self.button_height)

    def load_settings(self):
        self.settings.load_settings()
        self.theme = self.settings.get_theme()
        self.language = self.settings.get_language()

    def draw_button(self, screen, text, x, y, width, height, base_color, hover_color, text_color, is_hovered):
        color = hover_color if is_hovered else base_color
        pygame.draw.rect(screen, text_color, (x - 5, y - 5, width + 10, height + 10))
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_field(self, screen, text, x, y, width, height, base_color, text_color):
        pygame.draw.rect(screen, base_color, (x, y - height // 2, width, height))
        triangle_mid_point_x = x + width - self.triangle_spacing
        triangle_mid_point_y = y
        triangle_vertices = [(triangle_mid_point_x + self.triangle_spacing // 2, triangle_mid_point_y), (triangle_mid_point_x - self.triangle_spacing // 2, triangle_mid_point_y + self.triangle_spacing // 2), (triangle_mid_point_x - self.triangle_spacing // 2, triangle_mid_point_y - self.triangle_spacing // 2)]
        pygame.draw.polygon(screen, text_color, triangle_vertices, 0)
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y))
        screen.blit(text_surface, text_rect)

    def draw_title(self, screen):
        text_surface = self.title_font.render("GOHA", True, self.theme['maincolor1'])
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 150))
        screen.blit(text_surface, text_rect)

    def draw_new_game_menu(self):
        self.draw_title(self.win)

        for i, option in enumerate(self.options):
            text_surface = self.button_font.render(self.language[option], True, self.theme['maincolor1'])
            text_rect = text_surface.get_rect(midright=(WIDTH // 2 - self.options_spacing_horizontal // 2, self.options_start_y + i * (self.options_height + self.options_spacing)))
            self.win.blit(text_surface, text_rect)

        self.draw_field(self.win, self.language['Difficulties'][self.difficulty],   WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 0 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, self.theme['maincolor2'], self.theme['maincolor1'])
        self.draw_field(self.win, self.language['PlayerColors'][self.player_color], WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 1 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, self.theme['maincolor2'], self.theme['maincolor1'])
        self.draw_field(self.win, self.language['Handicaps'][self.handicap],        WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 2 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, self.theme['maincolor2'], self.theme['maincolor1'])
        self.draw_field(self.win, self.language['Times'][self.time],                WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 3 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, self.theme['maincolor2'], self.theme['maincolor1'])
        self.draw_field(self.win, self.language['BoardSizes'][self.board_size],     WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 4 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, self.theme['maincolor2'], self.theme['maincolor1'])

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_start_hovered = self.button_start_rect.collidepoint(mouse_x, mouse_y)
        self.is_cancel_hovered = self.button_cancel_rect.collidepoint(mouse_x, mouse_y)
        self.draw_button(self.win, self.language['Start'],  (WIDTH - self.button_width) // 2 - self.button_width // 2 - self.button_spacing, self.button_start_y, self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['maincolor2'],  self.theme['maincolor1'], self.is_start_hovered)
        self.draw_button(self.win, self.language['Cancel'], (WIDTH - self.button_width) // 2 + self.button_width // 2 + self.button_spacing, self.button_start_y, self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['cancelcolor'], self.theme['maincolor1'], self.is_cancel_hovered)

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.difficulty_input_rect.collidepoint(event.pos):
                    self.difficulty = (self.difficulty + 1) % len(self.language['Difficulties'])
                elif self.player_color_input_rect.collidepoint(event.pos):
                    self.player_color = (self.player_color + 1) % len(self.language['PlayerColors'])
                elif self.handicap_input_rect.collidepoint(event.pos):
                    self.handicap = (self.handicap + 1) % len(self.language['Handicaps'])
                elif self.time_input_rect.collidepoint(event.pos):
                    self.time = (self.time + 1) % len(self.language['Times'])
                elif self.board_size_input_rect.collidepoint(event.pos):
                    self.board_size = (self.board_size + 1) % len(self.language['BoardSizes'])
                elif self.is_start_hovered:
                    self.running = False
                    self.game.opponent_difficulty = self.difficulty
                    self.game.player_color = self.player_color
                    self.game.handicap = self.handicap
                    self.game.time = self.time
                    self.game.board_size = self.board_size
                    self.game_settings_changed = True
                elif self.is_cancel_hovered:
                    self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
