TITLE = "Take the L"
# screen dims
WIDTH = 480
HEIGHT = 600
# frames per second
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
REDDISH = (240,55,66)
SKY_BLUE = (143, 185, 252)
FONT_NAME = 'arial'
SPRITESHEET = "spritesheet_jumper.png"
SPRITESHEET2 = "spritesheet.png"
# data files
HS_FILE = "highscore.txt"
# player settings
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 25
# game settings
BOOST_POWER = 60
RIGHT_POWER = 70
POW_SPAWN_PCT = 7
RIGHT_SPAWN_PCT = 7

MOB_FREQ = 500
# layers - uses numerical value in layered sprites
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
RIGHT_POWER_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

PLATFORM_LIST = [(0, HEIGHT-40),
                (50, HEIGHT-40),
                (100, HEIGHT-40),
                (150, HEIGHT-40),
                 (65, HEIGHT - 300),
                 (20, HEIGHT - 350),
                 (200, HEIGHT - 150),
                 (200, HEIGHT - 450)]
