import pygame
from goha.constants import WIN
from goha.mainmenu import Mainmenu

pygame.init()
pygame.display.set_caption('GOHA')
pygame_icon = pygame.image.load('goha/assets/gohaicon.png')
pygame.display.set_icon(pygame_icon)
# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def main():
    Mainmenu(WIN)

main()