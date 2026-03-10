from pygame.constants import USEREVENT

# C
C_WHITE = (255, 255, 255)
C_PLAYER = (0, 0, 0)
C_ANXIETY = (255, 0, 0)
C_PROC = (63, 72, 204)

# E
EVENT_ENEMY = USEREVENT + 1
SPAWN_TIME = 5000

ENTITY_SPEED = {
    'player': 1,
    'anxiety': 2,
    'procrastination': 0.8,
    'guilt': 3,
    'thought': 0
}

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

WIN_CENTER = WIN_WIDTH / 2, WIN_HEIGHT / 2
