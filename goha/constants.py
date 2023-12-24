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

board_19x19 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 0, 0, 7,
    7, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 0, 0, 7,
    7, 0, 0, 0, 0, 2, 0, 2, 1, 1, 2, 2, 2, 1, 1, 1, 0, 1, 1, 0, 7,
    7, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 0, 1, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 2, 1, 1, 1, 1, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 7,
    7, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 7,
    7, 0, 0, 0, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 0, 2, 0, 0, 0, 7,
    7, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

BOARDS = {
    0: [board_9x9, 9, 9],
    1: [board_13x13, 13, 13],
    2: [board_19x19, 19, 19]
}
SELECTED_BOARD = 0

# stones
EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

# pixel sizes
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# piece to draw
PADDING = 15    #percents
OUTLINE = 2     #pixels

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
T2_ORANGECOLOR1 = (255,165,0)
T2_ORANGECOLOR2 = (255, 238, 204)
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
    'Theme1': {'backgroundcolor': WHITECOLOR,       'maincolor1': BLACKCOLOR,       'maincolor2': LIGHTGREYCOLOR,   'cancelcolor': REDCOLOR2,   'iconbackgroundcolor': BROWNCOLOR},
    'Theme2': {'backgroundcolor': T2_ORANGECOLOR2,  'maincolor1': T2_ORANGECOLOR1,  'maincolor2': T2_BROWNCOLOR3,   'cancelcolor': REDCOLOR2,   'iconbordercolor': BROWNCOLOR},
    'Theme3': {'backgroundcolor': T3_GREEN1,        'maincolor1': T3_GREEN2,        'maincolor2': T3_GREEN3,        'cancelcolor': T3_GREEN4,   'iconbordercolor': BROWNCOLOR}
}

LANGUAGES = {
    'English':  {'Continue': 'Continue' , 'New Game': 'New Game', 'Settings': 'Settings',   'Info': 'Info', 'Exit': 'Exit',
                 'Nick': 'Nick',     'Theme': 'Theme',   'Language': 'Language', 'Stone Centering': 'Stone Centering',       'Volume': 'Volume',
                 'Bot Difficulty': 'Bot Difficulty',    'Play As': 'Play As',   'Handicap': 'Handicap', 'Time': 'Time', 'Board Size': 'Board Size',
                 'Difficulties': ['Easy', 'Medium', 'Hard', 'Random', 'Play Solo'],    'PlayerColors': ['Black', 'White'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],   'Times': ['No', '10+0', '20+5'],    'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Theme 1', 'Theme 2', 'Theme 3'], 'Languages': ['English', 'Polish'],
                 'Info Text': '''Welcome to the game of Go! This ancient Chinese board game\\is a combination of science, art and sport. Try to cover as\\much territory as possible. Capture your opponent's stones,\\but don't let him capture yours!\\\\Hi, my name is Miłosz Moroz and I've created this program\\as a part of my Engineering Thesis. Try different opponents,\\different board sizes and adjust the app settings to your preferences.\\But above all, don't forget the most important thing - to have fun!''',
                 'Save': 'Save',    'Cancel': 'Cancel', 'OK': 'OK', 'Start': 'Start',
                 'Game ends.': 'Game ends.', 'Player resigned.': 'Player resigned.', 'Game ends. White won.': 'Game ends. White won.', '(Black ran out of time.)': '(Black ran out of time.)', 'Game ends. Black won.': 'Game ends. Black won.', '(White ran out of time.)': '(White ran out of time.)'},
    'Polski':   {'Continue': 'Kontynuuj', 'New Game': 'Nowa Gra', 'Settings': 'Opcje',      'Info': 'Info', 'Exit': 'Wyjdź',
                 'Nick': 'Ksywka',  'Theme': 'Motyw',   'Language': 'Język',    'Stone Centering': 'Środkowanie Kamieni',   'Volume': 'Głośność',
                 'Bot Difficulty': 'Trudność Bota',    'Play As': 'Graj Jako',   'Handicap': 'Handicap', 'Time': 'Czas', 'Board Size': 'Wielkość Planszy',
                 'Difficulties': ['Łatwy', 'Średni', 'Trudny', 'Losowy', 'Graj Sam'], 'PlayerColors': ['Czarny', 'Biały'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],  'Times': ['Nie', '10+0', '20+5'],   'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Motyw 1', 'Motyw 2', 'Motyw 3'], 'Languages': ['Angielski', 'Polski'],
                 'Info Text': '''Witaj w grze w go! Ta starochińska gra planszowa to\\połączenie nauki, sztuki i sportu. Postaraj się otoczyć\\jak największe terytorium. Zbijaj kamienie przeciwnika,\\lecz nie pozwól, by on zbił twoje!\\\\Hej, jestem Miłosz Moroz i to właśnie ja stworzyłem ten\\program w ramach pracy inżynierskiej. Wypróbuj różnych\\przeciwników, różne rozmiary planszy i dostosuj ustawienia\\aplikacji według swoich preferencji. Lecz przede wszystkim\\nie zapomnij o najważniejszym - dobrze się bawić!''',
                 'Save': 'Zapisz',  'Cancel': 'Anuluj', 'OK': 'OK', 'Start': 'Start',
                 'Game ends.': 'Koniec gry.', 'Player resigned.': 'Gracz zrezygnował.', 'Game ends. White won.': 'Koniec gry. Białe wygrały.', '(Black ran out of time.)': '(Koniec czasu czarnych.)', 'Game ends. Black won.': 'Koniec gry. Czarne wygrały.', '(White ran out of time.)': '(Koniec czasu białych.)'},
}