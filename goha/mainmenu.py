import pygame
import sys
import random
import os
from .settings import Settings
from .background import Background
from .gamemenu import Gamemenu
from .newgamemenu import Newgamemenu
from .settingsmenu import Settingsmenu
from .infomenu import Infomenu
from .game import Game
from .constants import WIDTH, FPS

class Mainmenu:
    def __init__(self, win):
        self.win = win
        self.settings = Settings()
        self.load_settings()
        self.game = Game(self.win)
        self.background = Background(self.win)
        self.currentmenu = "mainmenu"
        self._init()

    def _init(self):
        self.button_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 36)
        self.title_font = pygame.font.Font("goha/assets/Shojumaru-Regular.ttf", 100)

        self.button_width = 400
        self.button_height = 70
        self.button_spacing = 45
        self.button_start_y = 300

        self.button_continue_rect = pygame.Rect((WIDTH - self.button_width) // 2, self.button_start_y,                                                  self.button_width, self.button_height)
        self.button_new_game_rect = pygame.Rect((WIDTH - self.button_width) // 2, self.button_start_y +      self.button_height + self.button_spacing,  self.button_width, self.button_height)
        self.button_settings_rect = pygame.Rect((WIDTH - self.button_width) // 2, self.button_start_y + 2 * (self.button_height + self.button_spacing), self.button_width, self.button_height)
        self.button_info_rect =     pygame.Rect((WIDTH - self.button_width) // 2, self.button_start_y + 3 * (self.button_height + self.button_spacing), self.button_width, self.button_height)
        self.button_exit_rect =     pygame.Rect((WIDTH - self.button_width) // 2, self.button_start_y + 4 * (self.button_height + self.button_spacing), self.button_width, self.button_height)

        self.run_menu()

    def load_settings(self):
        self.settings.load_settings()
        self.theme = self.settings.get_theme()
        self.language = self.settings.get_language()

    def play_music(self):
        self.current_music_index = 0
        self.music_files = [file for file in os.listdir('goha/music') if file.endswith((".mp3", ".wav"))]
        random.shuffle(self.music_files)
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        pygame.mixer.music.load(os.path.join('goha/music', self.music_files[self.current_music_index]))
        pygame.mixer.music.set_volume(self.settings.get_volume()/100)
        pygame.mixer.music.play()

    def start_next_music(self):
        for event in self.events:
            if event.type == pygame.USEREVENT + 1:
                    self.current_music_index = (self.current_music_index + 1) % len(self.music_files)
                    pygame.mixer.music.load(os.path.join('goha/music', self.music_files[self.current_music_index]))
                    pygame.mixer.music.play()

    def draw_button(self, screen, text, x, y, width, height, base_color, hover_color, text_color, is_hovered):
        color = hover_color if is_hovered else base_color
        pygame.draw.rect(screen, text_color, (x - 5, y - 5, width + 10, height + 10))
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    def draw_title(self):
        text_surface = self.title_font.render("GOHA", True, self.theme['maincolor1'])
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 150))
        self.win.blit(text_surface, text_rect) 

    def draw_main_menu(self):   
        self.load_settings()
        self.draw_title()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_continue_hovered = self.button_continue_rect.collidepoint(mouse_x, mouse_y)
        self.is_new_game_hovered = self.button_new_game_rect.collidepoint(mouse_x, mouse_y)
        self.is_settings_hovered = self.button_settings_rect.collidepoint(mouse_x, mouse_y)
        self.is_info_hovered = self.button_info_rect.collidepoint(mouse_x, mouse_y)
        self.is_exit_hovered = self.button_exit_rect.collidepoint(mouse_x, mouse_y)
        self.draw_button(self.win, self.language['Continue'],   (WIDTH - self.button_width) // 2, self.button_start_y,                                                  self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['maincolor2'],     self.theme['maincolor1'], self.is_continue_hovered)
        self.draw_button(self.win, self.language['New Game'],   (WIDTH - self.button_width) // 2, self.button_start_y +      self.button_height + self.button_spacing,  self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['maincolor2'],     self.theme['maincolor1'], self.is_new_game_hovered)
        self.draw_button(self.win, self.language['Settings'],   (WIDTH - self.button_width) // 2, self.button_start_y + 2 * (self.button_height + self.button_spacing), self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['maincolor2'],     self.theme['maincolor1'], self.is_settings_hovered)
        self.draw_button(self.win, self.language['Info'],       (WIDTH - self.button_width) // 2, self.button_start_y + 3 * (self.button_height + self.button_spacing), self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['maincolor2'],     self.theme['maincolor1'], self.is_info_hovered)
        self.draw_button(self.win, self.language['Exit'],       (WIDTH - self.button_width) // 2, self.button_start_y + 4 * (self.button_height + self.button_spacing), self.button_width, self.button_height, self.theme['backgroundcolor'], self.theme['cancelcolor'],    self.theme['maincolor1'], self.is_exit_hovered)

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_continue_hovered:
                    self.gamemenu = Gamemenu(self.win, self.game)
                    self.currentmenu = 'gamemenu'
                    self.gamemenu.load_settings()
                    self.gamemenu.running = True
                elif self.is_new_game_hovered:
                    self.newgamemenu = Newgamemenu(self.win, self.game)
                    self.currentmenu = 'newgamemenu'
                    self.newgamemenu.load_settings()
                    self.newgamemenu.running = True
                elif self.is_settings_hovered:
                    self.settingsmenu = Settingsmenu(self.win)
                    self.currentmenu = 'settingsmenu'
                    self.settingsmenu.load_settings()
                    self.settingsmenu.running = True
                elif self.is_info_hovered:
                    self.infomenu = Infomenu(self.win)
                    self.currentmenu = 'infomenu'
                    self.infomenu.load_settings()
                    self.infomenu.running = True
                elif self.is_exit_hovered:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def run_menu(self):
        self.play_music()
        while True:
            self.events = pygame.event.get()
            self.background.draw_background()
            self.start_next_music()

            ### GAME MENU EVENTS ###
            if self.currentmenu == 'gamemenu' and self.gamemenu.running == True:
                self.gamemenu.draw_game_menu()
                self.gamemenu.event_handler(self.events)

            elif self.currentmenu == 'newgamemenu' and self.newgamemenu.game_settings_changed == True:
                self.game = Game(self.win, self.newgamemenu.game.opponent_difficulty, self.newgamemenu.game.player_color, self.newgamemenu.game.handicap, self.newgamemenu.game.time, board_size=self.newgamemenu.game.board_size)
                self.newgamemenu.game_settings_changed = False
                self.currentmenu = 'gamemenu'
                self.gamemenu = Gamemenu(self.win, self.game)
                self.gamemenu.load_settings()
                self.gamemenu.running = True
                self.gamemenu.draw_game_menu()
                self.gamemenu.event_handler(self.events)

            ### NEW GAME MENU EVENTS ###
            elif self.currentmenu == 'newgamemenu' and self.newgamemenu.running == True:
                self.newgamemenu.draw_new_game_menu()
                self.newgamemenu.event_handler(self.events)

            ### SETTINGS MENU EVENTS ###
            elif self.currentmenu == 'settingsmenu' and self.settingsmenu.running == True:
                self.settingsmenu.draw_settings_menu()
                self.settingsmenu.event_handler(self.events)
                
            ### INFO MENU EVENTS ###
            elif self.currentmenu == 'infomenu' and self.infomenu.running == True:
                self.infomenu.draw_info_menu()
                self.infomenu.event_handler(self.events)

            ### MAIN MENU EVENTS ###
            else:
                self.currentmenu = 'mainmenu'
                self.draw_main_menu()
                self.event_handler(self.events)
            
            # Refresh window
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)