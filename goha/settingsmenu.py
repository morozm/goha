import pygame
import sys
from .settings import Settings, THEMES_LIST, LANGUAGES_LIST
from .constants import BLACKCOLOR, WHITECOLOR, LIGHTGREYCOLOR, WIDTH, THEMES

class Settingsmenu:
    def __init__(self, win):
        self.win = win
        self.settings = Settings()
        self.load_settings()
        self.running = False
        self._init()

    def _init(self):
        self.button_font_size = 36
        self.title_font_size = 100
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", self.button_font_size)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", self.title_font_size)

        self.options = ["Username", "Theme", "Language", "Stone Centering", "Volume"]
        self.options_start_y = 300
        self.options_height = 60
        self.options_spacing = 20
        self.options_spacing_horizontal = 80
        self.options_input_length = 400

        self.title_text = self.title_font.render("GOHA", True, self.theme['maincolor1'])
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, 150))
        
        self.username_input_border = 5
        self.username_input_active = False
        self.cursor_toggle_time = 0
        self.cursor_visible = False
        
        self.theme_triangle_spacing = 30
        
        self.stone_centering_growing = False
        self.stone_centering_border = 8
        self.growing_square_size = 0 if not self.stone_centering else self.options_height - 2 * self.stone_centering_border
        self.growing_speed = 5
        
        self.slider_height = 6
        self.knob_dragging = False
        self.knob_radius = 10

    def load_settings(self):
        self.username_input_text = self.settings.get_username()
        self.theme_select_text = self.settings.get_selected_theme()
        self.theme = self.settings.get_theme()
        self.language_select_text = self.settings.get_selected_language()
        self.language = self.settings.get_language()
        self.stone_centering = self.settings.get_stone_centering()
        self.volume = self.settings.get_volume()

    def draw_button(self, screen, text, x, y, width, height, base_color, hover_color, text_color, is_hovered):
        color = hover_color if is_hovered else base_color
        pygame.draw.rect(screen, BLACKCOLOR, (x - 5, y - 5, width + 10, height + 10))
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_username_field(self, screen, text, x, y, width, height, base_color, pressed_color, text_color, is_active):
        self.username_input_rect = pygame.Rect(x, y - height // 2, width, height)
        if is_active:
            pygame.draw.rect(screen, pressed_color, (x, y - height // 2, width, height))
            pygame.draw.rect(screen, base_color, (x + self.username_input_border, y - height // 2 + self.username_input_border, width - self.username_input_border * 2, height - self.username_input_border * 2))
        else:
            pygame.draw.rect(screen, base_color, (x, y - height // 2, width, height))
        text_surface = self.button_font.render(text + '|', True, text_color) if (self.cursor_visible and is_active) else self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y))
        screen.blit(text_surface, text_rect)
        current_time = pygame.time.get_ticks()
        if is_active and (current_time > self.cursor_toggle_time):
            self.cursor_visible = not self.cursor_visible
            self.cursor_toggle_time = current_time + 500

    def draw_theme_field(self, screen, text, x, y, width, height, base_color, text_color):
        self.theme_input_rect = pygame.Rect(x, y - height // 2, width, height)
        pygame.draw.rect(screen, base_color, (x, y - height // 2, width, height))
        triangle_mid_point_x = x + width - self.theme_triangle_spacing
        triangle_mid_point_y = y
        triangle_vertices = [(triangle_mid_point_x + self.theme_triangle_spacing // 2, triangle_mid_point_y), (triangle_mid_point_x - self.theme_triangle_spacing // 2, triangle_mid_point_y + self.theme_triangle_spacing // 2), (triangle_mid_point_x - self.theme_triangle_spacing // 2, triangle_mid_point_y - self.theme_triangle_spacing // 2)]
        pygame.draw.polygon(screen, text_color, triangle_vertices, 0)
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y))
        screen.blit(text_surface, text_rect)

    def draw_language_field(self, screen, text, x, y, width, height, base_color, text_color):
        self.language_input_rect = pygame.Rect(x, y - height // 2, width, height)
        pygame.draw.rect(screen, base_color, (x, y - height // 2, width, height))
        triangle_mid_point_x = x + width - self.theme_triangle_spacing
        triangle_mid_point_y = y
        triangle_vertices = [(triangle_mid_point_x + self.theme_triangle_spacing // 2, triangle_mid_point_y), (triangle_mid_point_x - self.theme_triangle_spacing // 2, triangle_mid_point_y + self.theme_triangle_spacing // 2), (triangle_mid_point_x - self.theme_triangle_spacing // 2, triangle_mid_point_y - self.theme_triangle_spacing // 2)]
        pygame.draw.polygon(screen, text_color, triangle_vertices, 0)
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midleft=(x + self.options_spacing, y))
        screen.blit(text_surface, text_rect)

    def draw_stone_centering_checkbox(self, screen, x, y, squaresize, base_color, pressed_color):
        self.stone_centering_checkbox_rect = pygame.Rect(x, y - squaresize // 2, squaresize, squaresize)
        pygame.draw.rect(screen, base_color, (x, y - squaresize // 2, squaresize, squaresize))
        if self.stone_centering_growing:
            if self.stone_centering:
                self.growing_square_size += self.growing_speed
                if self.growing_square_size >= squaresize - 2 * self.stone_centering_border:
                    self.growing_square_size = squaresize - 2 * self.stone_centering_border
                    self.stone_centering_growing = False
            else:
                self.growing_square_size -= self.growing_speed
                if self.growing_square_size <= 0:
                    self.growing_square_size = 0
                    self.stone_centering_growing = False

        stone_centering_checkbox2_rect = pygame.Rect(0, 0, self.growing_square_size, self.growing_square_size)
        stone_centering_checkbox2_rect.center = self.stone_centering_checkbox_rect.center
        pygame.draw.rect(screen, pressed_color, stone_centering_checkbox2_rect)

    def draw_slider(self, screen, x, y, width, height, base_color, pressed_color, text_color, knob_dragging):
        self.slider_rect = pygame.Rect(x, y - self.options_height // 2, width, height)
        color = pressed_color if knob_dragging else base_color
        pygame.draw.rect(screen, base_color, self.slider_rect)
        self.knob_x = x + self.volume * self.options_input_length // 100
        self.knob_y = y - self.options_height // 2 + height // 2
        pygame.draw.circle(screen, color, (self.knob_x, self.knob_y), self.knob_radius)
        text_surface = self.button_font.render(f"{self.volume}%", True, text_color)
        text_rect = text_surface.get_rect(midright=(self.slider_rect.right + 120, self.slider_rect.centery))
        screen.blit(text_surface, text_rect)

    def draw_settings_menu(self):
        self.win.blit(self.title_text, self.title_rect)

        for i, option in enumerate(self.options):
            text_surface = self.button_font.render(option, True, BLACKCOLOR)
            text_rect = text_surface.get_rect(midright=(WIDTH // 2 - self.options_spacing_horizontal // 2, self.options_start_y + i * (self.options_height + self.options_spacing)))
            self.win.blit(text_surface, text_rect)

        self.draw_username_field(self.win, self.username_input_text, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y, self.options_input_length, self.options_height, LIGHTGREYCOLOR, BLACKCOLOR, BLACKCOLOR, self.username_input_active)
        self.draw_theme_field(self.win, self.theme_select_text, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 1 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, LIGHTGREYCOLOR, BLACKCOLOR)
        self.draw_language_field(self.win, self.language_select_text, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 2 * (self.options_height + self.options_spacing), self.options_input_length, self.options_height, LIGHTGREYCOLOR, BLACKCOLOR)
        self.draw_stone_centering_checkbox(self.win, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 3 * (self.options_height + self.options_spacing), self.options_height, LIGHTGREYCOLOR, BLACKCOLOR)            
        self.draw_slider(self.win, WIDTH // 2 + self.options_spacing_horizontal // 2, self.options_start_y + 4.5 * (self.options_height + self.options_spacing) - self.slider_height // 2 - self.knob_radius, self.options_input_length, self.slider_height, LIGHTGREYCOLOR, BLACKCOLOR, BLACKCOLOR, self.knob_dragging)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_width, button_height = 400, 70
        button_spacing = 45
        button_start_y = 300 + 460

        button_save_rect = pygame.Rect((WIDTH - button_width) // 2 - button_width // 2 - button_spacing, button_start_y, button_width, button_height)
        button_cancel_rect = pygame.Rect((WIDTH - button_width) // 2 + button_width // 2 + button_spacing, button_start_y, button_width, button_height)

        self.is_save_hovered = button_save_rect.collidepoint(mouse_x, mouse_y)
        self.is_cancel_hovered = button_cancel_rect.collidepoint(mouse_x, mouse_y)

        self.draw_button(self.win, "Save", (WIDTH - button_width) // 2 - button_width // 2 - button_spacing, button_start_y, button_width, button_height, WHITECOLOR, LIGHTGREYCOLOR, BLACKCOLOR, self.is_save_hovered)
        self.draw_button(self.win, "Cancel", (WIDTH - button_width) // 2 + button_width // 2 + button_spacing, button_start_y, button_width, button_height, WHITECOLOR, (255, 69, 0), BLACKCOLOR, self.is_cancel_hovered)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.username_input_rect.collidepoint(event.pos):
                    self.username_input_active = True
                    self.cursor_visible = True
                    self.cursor_toggle_time = pygame.time.get_ticks() + 300
                else:
                    self.username_input_active = False
                if self.theme_input_rect.collidepoint(event.pos):
                    try:
                        index = THEMES_LIST.index(self.theme_select_text)
                        next_index = (index + 1) % len(THEMES_LIST)
                        self.theme_select_text = THEMES_LIST[next_index]
                        self.theme = THEMES[self.theme_select_text]
                        self._init()
                    except ValueError:
                        self.theme_select_text = THEMES_LIST[0]
                if self.language_input_rect.collidepoint(event.pos):
                    try:
                        index = LANGUAGES_LIST.index(self.language_select_text)
                        next_index = (index + 1) % len(LANGUAGES_LIST)
                        self.language_select_text = LANGUAGES_LIST[next_index]
                    except ValueError:
                        self.language_select_text = LANGUAGES_LIST[0]
                if self.stone_centering_checkbox_rect.collidepoint(event.pos):
                    self.stone_centering = not self.stone_centering
                    self.stone_centering_growing = True
                    print(self.stone_centering)
                if self.is_save_hovered:
                    self.settings.save_settings(self.username_input_text, self.theme_select_text, self.language_select_text, self.stone_centering, self.volume)
                    self.running = False
                elif self.is_cancel_hovered:
                    self.load_settings()
                    self._init()
                    pygame.mixer.music.set_volume(self.volume/100)
                    self.running = False
                if event.button == 1:
                    knob_rect = pygame.Rect(self.knob_x - self.knob_radius, self.knob_y - self.knob_radius, self.knob_radius * 2, self.knob_radius * 2)
                    if knob_rect.collidepoint(event.pos):
                        self.knob_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.knob_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.knob_dragging:
                    self.knob_x = event.pos[0]
                    self.volume = max(0, min((self.knob_x - (WIDTH // 2 + self.options_spacing_horizontal // 2)) // (self.options_input_length // 100), 100))
                    pygame.mixer.music.set_volume(self.volume/100)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if self.username_input_active:
                    if event.key == pygame.K_RETURN:
                        print("Username entered:", self.username_input_text)
                        self.username_input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.username_input_text = self.username_input_text[:-1]
                    else:
                        self.username_input_text += event.unicode