import pygame
from goha.constants import WIDTH, HEIGHT, SQUARE_SIZE, BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET, ROWS, COLS
from goha.mainmenu import Mainmenu

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.display.set_caption('GOHA')
pygame_icon = pygame.image.load('goha/assets/gohaicon.png')
pygame.display.set_icon(pygame_icon)
# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def main():
    mainmenu = Mainmenu(WIN)

main()