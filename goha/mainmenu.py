import pygame
import sys
from .background import Background
from .gamemenu import Gamemenu
from .settingsmenu import Settingsmenu
from .infomenu import Infomenu
from .constants import WHITECOLOR, BLACKCOLOR, LIGHTGREYCOLOR, WIDTH

class Mainmenu:
    def __init__(self, win):
        self.win = win
        self.background = Background(self.win)
        self._init()

    def _init(self):
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 36)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 100)
        self.run_menu()

    def draw_button(self, screen, text, x, y, width, height, base_color, hover_color, text_color, is_hovered):
        color = hover_color if is_hovered else base_color
        pygame.draw.rect(screen, BLACKCOLOR, (x - 5, y - 5, width + 10, height + 10))
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    def run_menu(self):
        title_text = self.title_font.render("GOHA", True, BLACKCOLOR)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 150))

        while True:
            self.win.fill(WHITECOLOR)
            self.background.draw_background()
            self.win.blit(title_text, title_rect)
            mouse_x, mouse_y = pygame.mouse.get_pos()

            button_width, button_height = 400, 70
            button_spacing = 45
            button_start_y = 300

            button_continue_rect = pygame.Rect((WIDTH - button_width) // 2, button_start_y, button_width, button_height)
            button_new_game_rect = pygame.Rect((WIDTH - button_width) // 2, button_start_y + button_height + button_spacing, button_width, button_height)
            button_settings_rect = pygame.Rect((WIDTH - button_width) // 2, button_start_y + 2 * (button_height + button_spacing), button_width, button_height)
            button_info_rect = pygame.Rect((WIDTH - button_width) // 2, button_start_y + 3 * (button_height + button_spacing), button_width, button_height)
            button_exit_rect = pygame.Rect((WIDTH - button_width) // 2, button_start_y + 4 * (button_height + button_spacing), button_width, button_height)

            is_continue_hovered = button_continue_rect.collidepoint(mouse_x, mouse_y)
            is_new_game_hovered = button_new_game_rect.collidepoint(mouse_x, mouse_y)
            is_settings_hovered = button_settings_rect.collidepoint(mouse_x, mouse_y)
            is_info_hovered = button_info_rect.collidepoint(mouse_x, mouse_y)
            is_exit_hovered = button_exit_rect.collidepoint(mouse_x, mouse_y)

            # Drawing buttons
            self.draw_button(self.win, "Continue", (WIDTH - button_width) // 2, button_start_y, button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, is_continue_hovered)
            self.draw_button(self.win, "New Game", (WIDTH - button_width) // 2, button_start_y + button_height + button_spacing, button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, is_new_game_hovered)
            self.draw_button(self.win, "Settings", (WIDTH - button_width) // 2, button_start_y + 2 * (button_height + button_spacing), button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, is_settings_hovered)
            self.draw_button(self.win, "Info", (WIDTH - button_width) // 2, button_start_y + 3 * (button_height + button_spacing), button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, is_info_hovered)
            self.draw_button(self.win, "Exit", (WIDTH - button_width) // 2, button_start_y + 4 * (button_height + button_spacing), button_width, button_height, WHITECOLOR, (255, 69, 0), BLACKCOLOR, is_exit_hovered)

            # Events handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if is_new_game_hovered:
                        Gamemenu(self.win)
                    if is_settings_hovered:
                        Settingsmenu(self.win)
                    if is_info_hovered:
                        Infomenu(self.win)
                    elif is_exit_hovered:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # Refresh window
            pygame.display.flip()
            pygame.time.Clock().tick(60)