from pygame.constants import USEREVENT

# C
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_BREATH = (150, 200, 255)
C_COGNIT = (235, 135, 245)
C_BG = (54, 28, 119)
C_BG_WIN = (115, 180, 150)
C_BG_LOSE = (235, 85, 85)
C_LIGHT_GREY = (195, 195, 195)
C_BLUE_GREY = (115, 145, 190)

# E
EVENT_ENEMY = USEREVENT + 1
EVENT_TIME = USEREVENT + 2

ENTITY_SPEED = {
    'player': 2,
    'anxiety': 1.5,
    'procrastination': 1,
    'thought': 0
}

# M
MENU_OPTION = ('JOGAR', 'SCORE', 'SAIR')

# S
SPAWN_TIME = 3000
SPAWN_INTERVAL = 60000  # 1min


# T
TIME_STEP = 100  # 100ms
# TIME_VICTORY = 300000 # 5min
TIME_VICTORY = 60000  # 1min - TESTE

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

WIN_CENTER = WIN_WIDTH / 2, WIN_HEIGHT / 2

SCORE_POS = {
    0: (WIN_WIDTH / 2, 130),
    1: (WIN_WIDTH / 2, 150),
    2: (WIN_WIDTH / 2, 170),
    3: (WIN_WIDTH / 2, 190),
    4: (WIN_WIDTH / 2, 210),
    5: (WIN_WIDTH / 2, 230),
    6: (WIN_WIDTH / 2, 250),
    7: (WIN_WIDTH / 2, 270),
    8: (WIN_WIDTH / 2, 290),
    9: (WIN_WIDTH / 2, 310),
}
