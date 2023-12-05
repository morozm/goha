import pygame
import sys
from .constants import BLACKCOLOR, WIDTH, WHITECOLOR, LIGHTGREYCOLOR

class Infomenu:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.running = False
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 36)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 100)
        self.text_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 20)
        self.title_text = self.title_font.render("GOHA", True, BLACKCOLOR)
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, 150))
        self.text_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\\eiusmod tempor incididunt nut labore et dolore magna aliqua.\\Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\\nisi ut aliquip ex ea commodo consequat.\\\\Duis aute irure dolor in reprehenderit in voluptate velit esse\\cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\\cupidatat non proident, sunt in culpa qui officia deserunt mollit\\anim id est laborum."
        self.lines_text = self.text_text.split('\\')

    def draw_button(self, screen, text, x, y, width, height, base_color, hover_color, text_color, is_hovered):
        color = hover_color if is_hovered else base_color
        pygame.draw.rect(screen, BLACKCOLOR, (x - 5, y - 5, width + 10, height + 10))
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_info_menu(self):
        self.win.blit(self.title_text, self.title_rect)
            
        y_position = 350
        for line in self.lines_text:
            text_surface = self.text_font.render(line, True, BLACKCOLOR)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y_position))
            self.win.blit(text_surface, text_rect)
            y_position += self.text_font.get_linesize()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_width, button_height = 400, 70
        button_spacing = 45
        button_start_y = 300+460

        button_ok_rect = pygame.Rect((WIDTH - button_width) // 2, button_start_y, button_width, button_height)

        self.is_ok_hovered = button_ok_rect.collidepoint(mouse_x, mouse_y)

        self.draw_button(self.win, "Ok", (WIDTH - button_width) // 2, button_start_y, button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, self.is_ok_hovered)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_ok_hovered:
                    self.running = False         
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False