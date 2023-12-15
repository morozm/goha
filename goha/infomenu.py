import pygame
import sys
from .settings import Settings
from .constants import WIDTH

class Infomenu:
    def __init__(self, win):
        self.win = win
        self.settings = Settings()
        self.load_settings()
        self.running = False
        self._init()

    def _init(self):
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 36)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 100)
        self.text_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 20)

        self.button_width = 400
        self.button_height = 70
        self.button_spacing = 45
        self.button_start_y = 300 + 460
        
        self.button_ok_rect = pygame.Rect((WIDTH - self.button_width) // 2, self.button_start_y, self.button_width, self.button_height)

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

    def draw_title(self, screen):
        text_surface = self.title_font.render("GOHA", True, self.theme['maincolor1'])
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 150))
        screen.blit(text_surface, text_rect)
    
    def draw_text(self, screen):
        y_position = 350
        text_text = self.language['Info Text']
        lines_text = text_text.split('\\')
        for line in lines_text:
            text_surface = self.text_font.render(line, True, self.theme['maincolor1'])
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y_position))
            screen.blit(text_surface, text_rect)
            y_position += self.text_font.get_linesize()

    def draw_info_menu(self):
        self.draw_title(self.win)
        self.draw_text(self.win)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_ok_hovered = self.button_ok_rect.collidepoint(mouse_x, mouse_y)
        self.draw_button(self.win, self.language['OK'], (WIDTH - self.button_width) // 2, self.button_start_y, self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['maincolor2'], self.theme['maincolor1'], self.is_ok_hovered)

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_ok_hovered:
                    self.running = False         
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False