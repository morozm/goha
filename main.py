import pygame
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from goha.constants import WIN
from goha.mainmenu import Mainmenu

def main():
    Mainmenu(WIN)
    
def resource_path(relative_path):
    """Zwraca absolutną ścieżkę do zasobów, działa dla skryptu i dla EXE."""
    try:
        if getattr(sys, 'frozen', False):
            # PyInstaller: folder tymczasowy
            base_path = sys._MEIPASS
        else:
            # Normalny Python: folder ze skryptem
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)
    except Exception as e:
        print(f"Błąd ścieżki zasobu: {e}")
        return relative_path  # fallback

pygame.init()
pygame.display.set_caption('GOHA')
pygame_icon = pygame.image.load(resource_path('goha/assets/gohaicon.png'))
pygame.display.set_icon(pygame_icon)

main()