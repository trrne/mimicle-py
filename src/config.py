from pygame.locals import *

from trrne.v2 import V2


# def get_refresh_rate():
#     from screeninfo import get_monitors
#     monitors = get_monitors()
#     return {m.refresh_rate for m in monitors}


GAME_TITLE = 'MIMICLE WITH PYTHON'
GAME_FPS = 165

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = V2(1280, 720)

PLAYER_PATH_PREFIX = 'assets\\player'
PLAYER_NAME = 'player.png'
PLAYER_BULLET_NAME = 'bullet1.png'
PLAYER_ROCKET_LAUNCHER_NAME = 'rocketlauncher.png'

BACKGROUND_PATH_PREFIX = 'assets\\background'
BACKGROUND_NAME = 'background.png'

KEY_MOVE_UP = K_w
KEY_MOVE_LEFT = K_a
KEY_MOVE_DOWN = K_s
KEY_MOVE_RIGHT = K_d
KEY_SHOT = K_SPACE
KEY_RELOAD = K_SPACE
