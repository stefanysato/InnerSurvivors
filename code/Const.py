from pygame.constants import USEREVENT

# C
C_WHITE = (255, 255, 255)
C_PLAYER = (0, 0, 0)
C_BREATH = (150, 200, 255)
C_COGNIT = (255, 175, 200)

# E
EVENT_ENEMY = USEREVENT + 1
EVENT_TIMEOUT = USEREVENT + 2

ENTITY_SPEED = {
    'player': 1.5,
    'anxiety': 1.2,
    'procrastination': 0.8,
    'thought': 0
}

# S
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100 # 100ms
TIMEOUT_LEVEL = 60000 # 1min

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

WIN_CENTER = WIN_WIDTH / 2, WIN_HEIGHT / 2
