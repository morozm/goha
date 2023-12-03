import pygame
import sys
from .constants import BLACKCOLOR, WHITECOLOR, LIGHTGREYCOLOR, GREYCOLOR, WIDTH

class Settingsmenu:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.running = True
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 36)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 100)

        self.options_start_y = 300
        self.options_height = 60
        self.options_spacing = 20
        self.options_spacing_horizontal = 80
        self.options_input_length = 400

        self.username_input_rect = None
        self.username_input_text = "User"
        self.username_input_active = False
        self.run_menu()

    def draw_button(self, screen, text, x, y, width, height, base_color, hover_color, text_color, is_hovered):
        color = hover_color if is_hovered else base_color
        pygame.draw.rect(screen, BLACKCOLOR, (x - 5, y - 5, width + 10, height + 10))
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_username_field(self, screen, text, x, y, width, height, base_color, pressed_color, text_color, is_active):
        self.username_input_rect = pygame.Rect(x, y, width, height)
        color = pressed_color if is_active else base_color
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_theme_field(self, screen, text, x, y, width, height, base_color, pressed_color, text_color, is_active):
        self.theme_input_rect = pygame.Rect(x, y, width, height)
        color = pressed_color if is_active else base_color
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_language_field(self, screen, text, x, y, width, height, base_color, pressed_color, text_color, is_active):
        self.language_input_rect = pygame.Rect(x, y, width, height)
        color = pressed_color if is_active else base_color
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_stone_centering_checkbox(self, screen, x, y, width, height, base_color, pressed_color, text_color, is_active):
        self.stone_centering_checkbox_rect = pygame.Rect(x, y, width, height)
        color = pressed_color if is_active else base_color
        pygame.draw.rect(screen, color, (x, y, width, height))

    def run_menu(self):
        # Title
        title_text = self.title_font.render("GOHA", True, BLACKCOLOR)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 150))

        # Options
        options = ["Username", "Theme", "Language", "Stone Centering", "Sound"]
        sound_slider = pygame.Rect(WIDTH // 2 + 40, 620 + 20, 200, 40)

        while self.running:
            self.win.fill(WHITECOLOR)
            self.win.blit(title_text, title_rect)

            for i, option in enumerate(options):
                text_surface = self.button_font.render(option, True, BLACKCOLOR)
                text_rect = text_surface.get_rect(topright=(WIDTH // 2 - self.options_spacing_horizontal // 2, self.options_start_y + i * (self.options_height + self.options_spacing)))
                self.win.blit(text_surface, text_rect)

            pygame.draw.rect(self.win, BLACKCOLOR, sound_slider, 2)

            self.draw_username_field(self.win, self.username_input_text, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y, self.options_input_length, self.options_height, LIGHTGREYCOLOR, GREYCOLOR, BLACKCOLOR, False)
            self.draw_theme_field(self.win, self.username_input_text, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 1 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, LIGHTGREYCOLOR, GREYCOLOR, BLACKCOLOR, False)
            self.draw_language_field(self.win, self.username_input_text, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 2 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, LIGHTGREYCOLOR, GREYCOLOR, BLACKCOLOR, False)
            self.draw_stone_centering_checkbox(self.win, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 3 * (self.options_height + self.options_spacing), self.options_height, self.options_height, LIGHTGREYCOLOR, GREYCOLOR, BLACKCOLOR, False)            

            mouse_x, mouse_y = pygame.mouse.get_pos()

            button_width, button_height = 400, 70
            button_spacing = 45
            button_start_y = 300+460

            button_save_rect = pygame.Rect((WIDTH - button_width) // 2 - button_width // 2 - button_spacing, button_start_y, button_width, button_height)
            button_cancel_rect = pygame.Rect((WIDTH - button_width) // 2 + button_width // 2 + button_spacing, button_start_y, button_width, button_height)

            is_save_hovered = button_save_rect.collidepoint(mouse_x, mouse_y)
            is_cancel_hovered = button_cancel_rect.collidepoint(mouse_x, mouse_y)

            # Drawing buttons
            self.draw_button(self.win, "Save", (WIDTH - button_width) // 2 - button_width // 2 - button_spacing, button_start_y, button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, is_save_hovered)
            self.draw_button(self.win, "Cancel", (WIDTH - button_width) // 2 + button_width // 2 + button_spacing, button_start_y, button_width, button_height, WHITECOLOR, (255, 69, 0), BLACKCOLOR, is_cancel_hovered)

            # Events handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.username_input_rect.collidepoint(event.pos):
                        self.username_input_active = not self.username_input_active
                    else:
                        username_input_active = False
                    if is_save_hovered:
                        self.running = False
                    elif is_cancel_hovered:
                        self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.username_input_active:
                        if event.key == pygame.K_RETURN:
                            print("Wprowadzona nazwa użytkownika:", self.username_input_text)
                            self.username_input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.username_input_text = self.username_input_text[:-1]
                        else:
                            self.username_input_text += event.unicode

            # Refresh window
            pygame.display.flip()
