import pygame
from goha.constants import RED, WIDTH, HEIGHT, SQUARE_SIZE, BOARD_WIDTH_OFFSET, BOARD_HEIGHT_OFFSET, ROWS, COLS
from goha.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('goha')
# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y - BOARD_HEIGHT_OFFSET) // SQUARE_SIZE
    col = (x - BOARD_WIDTH_OFFSET) // SQUARE_SIZE
    if (row<0 or col<0 or row>=ROWS or col>=COLS):
        return False
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (get_row_col_from_mouse(pos) != False):
                    row, col = get_row_col_from_mouse(pos)
                    game.place(row, col)
        game.update()
    
    pygame.quit()

main()