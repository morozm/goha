import pygame
from goha.constants import WIDTH, HEIGHT
from goha.mainmenu import Mainmenu
from goha.settings import Settings

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.display.set_caption('GOHA')
pygame_icon = pygame.image.load('goha/assets/gohaicon.png')
pygame.display.set_icon(pygame_icon)
# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def main():
    Settings().initialize_settings()
    Mainmenu(WIN)

main()