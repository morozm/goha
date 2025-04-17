import json
import os
import shutil
from .constants import THEMES, LANGUAGES, THEMES_LIST, LANGUAGES_LIST
from .utils import resource_path

class Settings:
    def __init__(self):
        self.filename = "settings.json"
        self.user_dir = os.path.join(os.getenv("APPDATA") or os.path.expanduser("~"), "Goha")
        os.makedirs(self.user_dir, exist_ok=True)

        self.file_path = os.path.join(self.user_dir, self.filename)

        self.initialize_settings()
        self.load_settings()

    def load_settings(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.username = data.get("username", "")
                self.selected_theme = data.get("theme", THEMES_LIST[0])
                self.theme = THEMES.get(self.selected_theme, THEMES[THEMES_LIST[0]])
                self.selected_language = data.get("language", LANGUAGES_LIST[0])
                self.language = LANGUAGES.get(self.selected_language, LANGUAGES[LANGUAGES_LIST[0]])
                self.stone_centering = data.get("stone_centering", True)
                self.volume = data.get("volume", 50)
        except Exception as e:
            print(f"Błąd ładowania ustawień: {e}")
            self.initialize_settings()

    def save_settings(self, username, selected_theme, selected_language, stone_centering, volume):
        data = {
            "username": username,
            "theme": selected_theme,
            "language": selected_language,
            "stone_centering": stone_centering,
            "volume": volume
        }
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Błąd zapisu ustawień: {e}")

    def initialize_settings(self):
        if not os.path.exists(self.file_path):
            self.save_settings("User", THEMES_LIST[0], LANGUAGES_LIST[0], True, 50)

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