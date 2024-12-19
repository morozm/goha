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

# board_9x9 = [
#     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
#     7, 2, 0, 2, 1, 0, 0, 1, 2, 0, 7,
#     7, 0, 2, 1, 0, 1, 0, 1, 2, 0, 7,
#     7, 2, 0, 2, 1, 0, 1, 1, 1, 2, 7,
#     7, 0, 2, 2, 1, 1, 1, 0, 1, 0, 7,
#     7, 0, 2, 0, 2, 2, 1, 1, 2, 0, 7,
#     7, 0, 2, 0, 2, 2, 1, 1, 2, 0, 7,
#     7, 0, 2, 2, 2, 1, 1, 1, 1, 0, 7,
#     7, 0, 0, 2, 1, 0, 1, 1, 2, 1, 7,
#     7, 0, 0, 2, 1, 1, 0, 1, 0, 1, 7,
#     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
# ]

# board_9x9 = [
#     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
#     7, 0, 0, 2, 0, 0, 0, 0, 0, 0, 7,
#     7, 0, 2, 1, 2, 2, 0, 0, 0, 0, 7,
#     7, 0, 1, 1, 1, 2, 2, 0, 0, 0, 7,
#     7, 0, 1, 1, 1, 1, 2, 0, 0, 0, 7,
#     7, 2, 2, 2, 2, 1, 1, 2, 2, 0, 7,
#     7, 0, 0, 2, 1, 1, 1, 1, 2, 0, 7,
#     7, 0, 1, 1, 0, 1, 2, 2, 2, 0, 7,
#     7, 0, 0, 0, 1, 2, 0, 2, 2, 0, 7,
#     7, 0, 0, 0, 0, 1, 2, 0, 0, 2, 7,
#     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
# ]

# puzzles
# board_9x9 = [
#     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
#     7, 0, 1, 0, 0, 2, 0, 0, 0, 0, 7,
#     7, 2, 2, 2, 2, 2, 1, 0, 1, 0, 7,
#     7, 1, 0, 0, 0, 1, 1, 0, 0, 0, 7,
#     7, 0, 1, 0, 1, 0, 0, 0, 0, 0, 7,
#     7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
#     7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
#     7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
#     7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
#     7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
#     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
# ]

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

#theme 4
T4_BLACK1 = (32, 42, 37)
T4_BLUE1 = (95, 75, 182)
T4_BLUE2 = (134, 165, 217)
T4_BLUE3 = (38, 240, 241)

#theme 5
T5_PINK1 = (134, 22, 87)
T5_PINK2 = (213, 106, 160)
T5_GREEN1 = (187, 219, 180)
T5_YELLOW1 = (252, 240, 204)

#theme 6
T6_BLACK1 = (26, 29, 26)
T6_GREEN1 = (187, 219, 180)
T6_BLUE1 = (123, 178, 217)
T6_GREEN2 = (38, 65, 60)

# stone colors
STONECOLORS = {
    1: BLACKCOLOR,
    2: WHITECOLOR,
    5: REDCOLOR,
    6: BLACKCOLOR,
    8: BLUECOLOR
}

THEMES_LIST = [
    'Theme1', 'Theme2', 'Theme3', 'Theme4', 'Theme5', 'Theme6'
]

LANGUAGES_LIST = [
    'English', 'Polski', 'Español', 'Français', 'Deutsch',
]

THEMES = {
    'Theme1': {'backgroundcolor': WHITECOLOR,       'maincolor1': BLACKCOLOR,       'maincolor2': LIGHTGREYCOLOR,   'cancelcolor': REDCOLOR2},
    'Theme2': {'backgroundcolor': T2_ORANGECOLOR2,  'maincolor1': T2_ORANGECOLOR1,  'maincolor2': T2_BROWNCOLOR3,   'cancelcolor': REDCOLOR2},
    'Theme3': {'backgroundcolor': T3_GREEN1,        'maincolor1': T3_GREEN2,        'maincolor2': T3_GREEN3,        'cancelcolor': T3_GREEN4},
    'Theme4': {'backgroundcolor': T4_BLUE1,         'maincolor1': T4_BLACK1,        'maincolor2': T4_BLUE2,         'cancelcolor': T4_BLUE2},
    'Theme5': {'backgroundcolor': T5_PINK2,         'maincolor1': T5_PINK1,         'maincolor2': T5_YELLOW1,       'cancelcolor': T5_GREEN1},
    'Theme6': {'backgroundcolor': T6_GREEN1,        'maincolor1': T6_BLACK1,        'maincolor2': T6_BLUE1,         'cancelcolor': T6_GREEN2},
}

LANGUAGES = {
    'English':  {'Continue': 'Continue' , 'New Game': 'New Game', 'Settings': 'Settings',   'Info': 'Info', 'Exit': 'Exit',
                 'Nick': 'Nick',     'Theme': 'Theme',   'Language': 'Language', 'Stone Centering': 'Stone Centering',       'Volume': 'Volume',
                 'Bot Difficulty': 'Bot Difficulty',    'Play As': 'Play As',   'Handicap': 'Handicap', 'Time': 'Time', 'Board Size': 'Board Size',
                 'Difficulties': ['Easy', 'Medium', 'Hard', 'Random', 'Play Solo'],    'PlayerColors': ['Black', 'White'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],   'Times': ['No', '10+0', '20+5'],    'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Theme 1', 'Theme 2', 'Theme 3', 'Theme 4', 'Theme 5', 'Theme 6'], 'Languages': ['English', 'Polish', 'Spanish', 'French', 'German'],
                 'Info Text': '''Welcome to the game of Go! This ancient Chinese board game\\is a combination of science, art and sport. Try to cover as\\much territory as possible. Capture your opponent's stones,\\but don't let him capture yours!\\\\Hi, my name is Miłosz Moroz and I've created this program\\as a part of my Engineering Thesis. Try different opponents,\\different board sizes and adjust the app settings to your preferences.\\But above all, don't forget the most important thing - to have fun!''',
                 'Save': 'Save',    'Cancel': 'Cancel', 'OK': 'OK', 'Start': 'Start',
                 'Game ends.': 'Game ends.', 'Player resigned.': 'Player resigned.', 'Game ends. White won.': 'Game ends. White won.', '(Black ran out of time.)': '(Black ran out of time.)', 'Game ends. Black won.': 'Game ends. Black won.', '(White ran out of time.)': '(White ran out of time.)'},
    'Polski':   {'Continue': 'Kontynuuj', 'New Game': 'Nowa Gra', 'Settings': 'Opcje',      'Info': 'Info', 'Exit': 'Wyjdź',
                 'Nick': 'Ksywka',  'Theme': 'Motyw',   'Language': 'Język',    'Stone Centering': 'Środkowanie Kamieni',   'Volume': 'Głośność',
                 'Bot Difficulty': 'Trudność Bota',    'Play As': 'Graj Jako',   'Handicap': 'Handicap', 'Time': 'Czas', 'Board Size': 'Wielkość Planszy',
                 'Difficulties': ['Łatwy', 'Średni', 'Trudny', 'Losowy', 'Graj Sam'], 'PlayerColors': ['Czarny', 'Biały'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],  'Times': ['Nie', '10+0', '20+5'],   'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Motyw 1', 'Motyw 2', 'Motyw 3', 'Motyw 4', 'Motyw 5', 'Motyw 6'], 'Languages': ['Angielski', 'Polski', 'Hiszpański', 'Francuski', 'Niemiecki'],
                 'Info Text': '''Witaj w grze w go! Ta starochińska gra planszowa to\\połączenie nauki, sztuki i sportu. Postaraj się otoczyć\\jak największe terytorium. Zbijaj kamienie przeciwnika,\\lecz nie pozwól, by on zbił twoje!\\\\Hej, jestem Miłosz Moroz i to właśnie ja stworzyłem ten\\program w ramach pracy inżynierskiej. Wypróbuj różnych\\przeciwników, różne rozmiary planszy i dostosuj ustawienia\\aplikacji według swoich preferencji. Lecz przede wszystkim\\nie zapomnij o najważniejszym - dobrze się bawić!''',
                 'Save': 'Zapisz',  'Cancel': 'Anuluj', 'OK': 'OK', 'Start': 'Start',
                 'Game ends.': 'Koniec gry.', 'Player resigned.': 'Gracz zrezygnował.', 'Game ends. White won.': 'Koniec gry. Białe wygrały.', '(Black ran out of time.)': '(Koniec czasu czarnych.)', 'Game ends. Black won.': 'Koniec gry. Czarne wygrały.', '(White ran out of time.)': '(Koniec czasu białych.)'},
    'Español':  {'Continue': 'Continuar', 'New Game': 'Nueva Partida', 'Settings': 'Configuración', 'Info': 'Información', 'Exit': 'Salir',
                 'Nick': 'Apodo', 'Theme': 'Tema', 'Language': 'Idioma', 'Stone Centering': 'Centrado de Piedras', 'Volume': 'Volumen',
                 'Bot Difficulty': 'Dificultad del Bot', 'Play As': 'Jugar Como', 'Handicap': 'Desventaja', 'Time': 'Tiempo', 'Board Size': 'Tamaño del Tablero',
                 'Difficulties': ['Fácil', 'Medio', 'Difícil', 'Aleatorio', 'Jugar Solo'], 'PlayerColors': ['Negro', 'Blanco'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Times': ['No', '10+0', '20+5'], 'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Tema 1', 'Tema 2', 'Tema 3', 'Tema 4', 'Tema 5', 'Tema 6'], 'Languages': ['Inglés', 'Polaco', 'Español', 'Francés', 'Alemán'],
                 'Info Text': '''¡Bienvenido al juego de Go! Este antiguo juego de\\mesa chino es una combinación de ciencia, arte y deporte.\\Intenta cubrir la mayor cantidad de territorio posible.\\Captura las piedras de tu oponente, pero no dejes que capture las tuyas.\\\\Hola, mi nombre es Miłosz Moroz y he creado este programa\\como parte de mi Tesis de Ingeniería.\\Prueba diferentes oponentes, tamaños de tablero diferentes\\y ajusta la configuración de la aplicación según tus preferencias.\\Pero, sobre todo, no olvides lo más importante: ¡divertirte!''',
                 'Save': 'Guardar', 'Cancel': 'Cancelar', 'OK': 'Aceptar', 'Start': 'Comenzar',
                 'Game ends.': 'Fin de la partida.', 'Player resigned.': 'Jugador resignado.', 'Game ends. White won.': 'Fin de la partida. Blancas ganaron.', '(Black ran out of time.)': '(Negras se quedaron sin tiempo.)', 'Game ends. Black won.': 'Fin de la partida. Negras ganaron.', '(White ran out of time.)': '(Blancas se quedaron sin tiempo.)'},
    'Français': {'Continue': 'Continuer', 'New Game': 'Nouvelle Partie', 'Settings': 'Paramètres', 'Info': 'Info', 'Exit': 'Quitter',
                 'Nick': 'Pseudo', 'Theme': 'Thème', 'Language': 'Langue', 'Stone Centering': 'Centrage des Pierres', 'Volume': 'Volume',
                 'Bot Difficulty': 'Difficulté du Bot', 'Play As': 'Jouer En Tant Que', 'Handicap': 'Handicap', 'Time': 'Temps', 'Board Size': 'Taille du Plateau',
                 'Difficulties': ['Facile', 'Moyen', 'Difficile', 'Aléatoire', 'Jouer Seul'], 'PlayerColors': ['Noir', 'Blanc'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Times': ['Non', '10+0', '20+5'], 'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Thème 1', 'Thème 2', 'Thème 3', 'Thème 4', 'Thème 5', 'Thème 6'], 'Languages': ['Anglais', 'Polonais', 'Espagnol', 'Français', 'Allemande'],
                 'Info Text': '''Bienvenue dans le jeu de Go ! Ce jeu de plateau\\chinois ancien est une combinaison de science, d'art et de sport.\\Essayez de couvrir autant de territoire que possible.\\Capturez les pierres de votre adversaire, mais ne laissez pas le vôtre être capturé !\\\\Salut, je m'appelle Miłosz Moroz et j'ai créé ce programme\\dans le cadre de ma thèse d'ingénierie. Essayez différents adversaires,\\différentes tailles de plateau et ajustez les paramètres de l'application selon vos préférences.\\Mais surtout, n'oubliez pas la chose la plus importante : vous amuser !''',
                 'Save': 'Enregistrer', 'Cancel': 'Annuler', 'OK': 'OK', 'Start': 'Démarrer', 'Game ends.': 'Fin de la partie.', 'Player resigned.': 'Joueur démissionné.',
                 'Game ends. White won.': 'Fin de la partie. Blanc a gagné.', '(Black ran out of time.)': '(Noir a manqué de temps.)', 'Game ends. Black won.': 'Fin de la partie. Noir a gagné.', '(White ran out of time.)': '(Blanc a manqué de temps.)'},
    'Deutsch':  {'Continue': 'Weiter', 'New Game': 'Neues Spiel', 'Settings': 'Einstellungen','Info': 'Info', 'Exit': 'Beenden',
                 'Nick': 'Spitzname', 'Theme': 'Thema', 'Language': 'Sprache', 'Stone Centering': 'Stein-Zentrierung', 'Volume': 'Lautstärke',
                 'Bot Difficulty': 'Bot-Schwierigkeit', 'Play As': 'Spielen Als', 'Handicap': 'Handicap', 'Time': 'Zeit', 'Board Size': 'Brettgröße',
                 'Difficulties': ['Leicht', 'Mittel', 'Schwer', 'Zufällig', 'Alleine Spielen'], 'PlayerColors': ['Schwarz', 'Weiß'], 'Handicaps': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Times': ['Nein', '10+0', '20+5'], 'BoardSizes': ['9x9', '13x13', '19x19'],
                 'Themes': ['Thema 1', 'Thema 2', 'Thema 3', 'Thema 4', 'Thema 5', 'Thema 6'], 'Languages': ['Englisch', 'Polnisch', 'Spanisch', 'Französisch', 'Deutsch'],
                 'Info Text': 'Willkommen beim Spiel Go! Dieses alte chinesische Brettspiel\\ist eine Kombination aus Wissenschaft, Kunst und Sport.\\Versuchen Sie, so viel Gebiet wie möglich zu bedecken.\\Erfassen Sie die Steine Ihres Gegners, lassen Sie jedoch nicht zu, dass er Ihre erfasst!\\\\Hallo, mein Name ist Miłosz Moroz und ich habe dieses Programm im Rahmen meiner\\Ingenieurarbeit erstellt. Probieren Sie verschiedene Gegner,\\verschiedene Brettgrößen aus und passen\\Sie die App-Einstellungen an Ihre Vorlieben an.\\Aber vor allem, vergessen Sie nicht das Wichtigste: Spaß zu haben!',
                 'Save': 'Speichern', 'Cancel': 'Abbrechen', 'OK': 'OK', 'Start': 'Starten', 'Game ends.': 'Spielende.', 'Player resigned.': 'Spieler hat aufgegeben.',
                 'Game ends. White won.': 'Spielende. Weiß hat gewonnen.', '(Black ran out of time.)': '(Schwarz ist die Zeit ausgegangen.)', 'Game ends. Black won.': 'Spielende. Schwarz hat gewonnen.', '(White ran out of time.)': '(Weiß ist die Zeit ausgegangen.)'},
}