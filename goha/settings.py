import json
import os
from .constants import THEMES, LANGUAGES    

THEMES_LIST = [
    'Theme1', 'Theme2', 'Theme3'
]

LANGUAGES_LIST = [
    'English', 'Polski'
]

class Settings:
    def __init__(self):
        self.file_path = "settings.json"
        self.username = None
        self.selected_theme = None
        self.theme = None
        self.selected_language = None
        self.stone_centering = None
        self.volume = None
        self.initialize_settings()
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.username = data.get("username", "")
                self.selected_theme = data.get("theme", "")
                self.theme = THEMES[self.selected_theme]
                self.selected_language = data.get("language", "")
                self.language = LANGUAGES[self.selected_language]
                self.stone_centering = data.get("stone_centering", "")
                self.volume = data.get("volume", "")

    def save_settings(self, username, selected_theme, selected_language, stone_centering, volume):
        data = {
            "username": username,
            "theme": selected_theme,
            "language": selected_language,
            "stone_centering": stone_centering,
            "volume": volume
        }
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def initialize_settings(self):
        if not os.path.exists(self.file_path):
            initial_username = "User"
            initial_theme = THEMES_LIST[0]
            initial_language = LANGUAGES_LIST[0]
            initial_stone_centering = True
            initial_volume = 50
            self.save_settings(initial_username, initial_theme, initial_language, initial_stone_centering, initial_volume)

    def get_username(self):
        return self.username
    
    def get_selected_theme(self):
        return self.selected_theme
    
    def get_theme(self):
        return self.theme
    
    def get_selected_language(self):
        return self.selected_language
    
    def get_language(self):
        return self.language
    
    def get_stone_centering(self):
        return self.stone_centering
    
    def get_volume(self):
        return self.volume