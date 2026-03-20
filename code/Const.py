from pygame.constants import USEREVENT

# C
C_WHITE = (255, 255, 255)
C_PLAYER = (0, 0, 0)
C_BREATH = (150, 200, 255)
C_COGNIT = (235, 135, 245)
C_BG = (54,28,119)

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
SPAWN_INTERVAL = 60000 # 1min

# T
TIME_STEP = 100 # 100ms
TIME_VICTORY = 300000 # 5min

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

WIN_CENTER = WIN_WIDTH / 2, WIN_HEIGHT / 2
