import pygame

###################################
#
# 0000 => 0    empty sqare
# 0001 => 1    black stone
# 0010 => 2    white stone
# 0100 => 4    stone marker
# 0111 => 7    offboard square
# 1000 => 8    liberty marker
#
# 0101 => 5    black stone marked
# 0110 => 6    white stone marked
#
###################################

board_9x9 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

board_13x13 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

board_19x19 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

BOARDS = {
    9:  board_9x9,
    13: board_13x13,
    19: board_19x19
}
SELECTED_BOARD = 9
OFFSETS_ENABLED = 1
ROWS, COLS = SELECTED_BOARD, SELECTED_BOARD

# stones
EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

# pixel sizes
WIDTH, HEIGHT = 1600, 900
SQUARE_SIZE = min(WIDTH//COLS, HEIGHT//ROWS)
BOARD_HEIGHT_OFFSET = max(0, (HEIGHT - SQUARE_SIZE*ROWS)//2)
BOARD_WIDTH_OFFSET = max(0, (WIDTH - SQUARE_SIZE*COLS)//2)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# colors
WHITECOLOR = (255, 255, 255)
BLACKCOLOR = (0, 0, 0)
GREYCOLOR = (128, 128, 128)
LIGHTGREYCOLOR = (200, 200, 200)
REDCOLOR = (255, 0 ,0)
REDCOLOR2 = (255, 69, 0)
DARKREDCOLOR = (173, 17, 17)
BLUECOLOR = (0, 0, 255)
BROWNCOLOR = (205,133,63)

#theme2
T2_ORANGECOLOR = (255,165,0)
T2_BROWNCOLOR1 = (192, 148, 134)
T2_BROWNCOLOR2 =(150, 92, 74)
T2_BROWNCOLOR3 = (74, 56, 50)

#theme3
T3_GREEN1 = (242, 252, 238)
T3_GREEN2 = (46, 238, 44)
T3_GREEN3 = (123, 153, 114)
T3_GREEN4 = (33, 53, 28)

# stone colors
STONECOLORS = {
    1: BLACKCOLOR,
    2: WHITECOLOR,
    5: REDCOLOR,
    6: BLACKCOLOR,
    8: BLUECOLOR
}

THEMES_LIST = [
    'Theme1', 'Theme2', 'Theme3'
]

LANGUAGES_LIST = [
    'English', 'Polski'
]

THEMES = {
    'Theme1': {'backgroundcolor': WHITECOLOR,       'maincolor1': BLACKCOLOR,       'maincolor2': LIGHTGREYCOLOR,   'cancelcolor': REDCOLOR2,   'boardcolor': BROWNCOLOR},
    'Theme2': {'backgroundcolor': T2_BROWNCOLOR3,   'maincolor1': T2_ORANGECOLOR,   'maincolor2': T2_BROWNCOLOR1,   'cancelcolor': REDCOLOR2,   'boardcolor': BROWNCOLOR},
    'Theme3': {'backgroundcolor': T3_GREEN1,        'maincolor1': T3_GREEN2,        'maincolor2': T3_GREEN3,        'cancelcolor': T3_GREEN4,   'boardcolor': BROWNCOLOR}
}

LANGUAGES = {
    'English':  {'Continue': 'Continue' , 'New Game': 'New Game', 'Settings': 'Settings',   'Info': 'Info', 'Exit': 'Exit',
                 'Nick': 'Nick',     'Theme': 'Theme',   'Language': 'Language', 'Stone Centering': 'Stone Centering',       'Volume': 'Volume',
                 'Difficulty': 'Difficulty',    'Play As': 'Play As',   'Handicap': 'Handicap', 'Time': 'Time', 'Board Size': 'Board Size',
                 'Difficulties': ['Easy', 'Medium', 'Hard'],    'PlayerColors': ['Black', 'White'], 'Handicaps': ['1', '2', '3'],   'Times': ['No', '10+0', '20+0'],    'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Theme 1', 'Theme 2', 'Theme 3'], 'Languages': ['English', 'Polish'],
                 'Save': 'Save',    'Cancel': 'Cancel', 'OK': 'OK', 'Start': 'Start'},
    'Polski':   {'Continue': 'Kontynuuj', 'New Game': 'Nowa Gra', 'Settings': 'Opcje',      'Info': 'Info', 'Exit': 'Wyjdź',
                 'Nick': 'Ksywka',  'Theme': 'Motyw',   'Language': 'Język',    'Stone Centering': 'Środkowanie Kamieni',   'Volume': 'Głośność',
                 'Difficulty': 'Trudność',    'Play As': 'Graj Jako',   'Handicap': 'Handicap', 'Time': 'Czas', 'Board Size': 'Wielkość Planszy',
                 'Difficulties': ['Łatwy', 'Średni', 'Trudny'], 'PlayerColors': ['Czarny', 'Biały'], 'Handicaps': ['1', '2', '3'],  'Times': ['Nie', '10+0', '20+0'],   'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Motyw 1', 'Motyw 2', 'Motyw 3'], 'Languages': ['Angielski', 'Polski'],
                 'Save': 'Zapisz',  'Cancel': 'Anuluj', 'OK': 'OK', 'Start': 'Start'},
}