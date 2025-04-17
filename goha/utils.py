import os
import sys

def resource_path(relative_path):
    """Zwraca absolutną ścieżkę do zasobów, działa dla skryptu i EXE."""
    try:
        if getattr(sys, 'frozen', False):
            # PyInstaller
            base_path = sys._MEIPASS
            return os.path.join(base_path, "goha", relative_path)
        else:
            # Normalne uruchamianie
            base_path = os.path.dirname(__file__)
            return os.path.join(base_path, relative_path)
    except Exception as e:
        print(f"Błąd ścieżki zasobu: {e}")
        return relative_path