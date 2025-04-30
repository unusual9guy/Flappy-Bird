"""
This is the config file for the my version of Flappy Bird game which loads all the 
nessecary assets to run the game. 
"""

import pygame

# initialsing the pygame mixer for loading the audio files 
pygame.mixer.init()

# Loading sound effects
AUDIO_PATH = 'assets/audio'
try:
    WING_SOUND = pygame.mixer.Sound(f'{AUDIO_PATH}/wing.ogg')
    POINT_SOUND = pygame.mixer.Sound(f'{AUDIO_PATH}/point.ogg')
    HIT_SOUND = pygame.mixer.Sound(f'{AUDIO_PATH}/hit.ogg')
    DIE_SOUND = pygame.mixer.Sound(f'{AUDIO_PATH}/die.ogg')
    SWOOSH_SOUND = pygame.mixer.Sound(f'{AUDIO_PATH}/swoosh.ogg')
except:
    print("Warning: Could not load some sound files")
    WING_SOUND = POINT_SOUND = HIT_SOUND = DIE_SOUND = SWOOSH_SOUND = None

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30

# Colors
WHITE = (255, 255, 255)

# Bird dimensions
BIRD_WIDTH = 34
BIRD_HEIGHT = 24

# Loading the images
BIRD_MID = pygame.image.load('assets/sprites/yellowbird-midflap.png')
BIRD_UP = pygame.image.load('assets/sprites/yellowbird-upflap.png')
BIRD_DOWN = pygame.image.load('assets/sprites/yellowbird-downflap.png')

# Scaling all the bird images
BIRD_MID = pygame.transform.scale(BIRD_MID, (BIRD_WIDTH, BIRD_HEIGHT))
BIRD_UP = pygame.transform.scale(BIRD_UP, (BIRD_WIDTH, BIRD_HEIGHT))
BIRD_DOWN = pygame.transform.scale(BIRD_DOWN, (BIRD_WIDTH, BIRD_HEIGHT))

# Loading and scaling the background and base
BACKGROUND_IMAGE = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

BASE_IMAGE = pygame.image.load('assets/sprites/base.png')
BASE_HEIGHT = 100  
BASE_IMAGE = pygame.transform.scale(BASE_IMAGE, (SCREEN_WIDTH, BASE_HEIGHT))

# Loadong the pipe image
PIPE_IMAGE = pygame.image.load('assets/sprites/pipe-green.png')

# Updating the PIPE_MAX_HEIGHT to account for the base height
PIPE_MAX_HEIGHT = SCREEN_HEIGHT - BASE_HEIGHT - 150  

# Constants for pipe spacing
PIPE_GAP_MIN = 110  # Minimum vertical gap between pipes 
PIPE_GAP_MAX = 160  # Maximum vertical gap between pipes 
PIPE_SPACING_MIN = 180  # Minimum horizontal distance between pipes 
PIPE_SPACING_MAX = 300  # Maximum horizontal distance between pipes 

PIPE_MIN_HEIGHT = 150  # Minimum height for lower pipe

# Loading the sprites for the numbers
NUMBERS = []
for i in range(10):
    number = pygame.image.load(f'assets/sprites/{i}.png')
    NUMBERS.append(number)

# Small number sprites
SMALL_NUMBERS = []
for i in range(10):
    number = pygame.image.load(f'assets/sprites/{i}_small.png')
    SMALL_NUMBERS.append(number)

GAME_OVER_IMAGE = pygame.image.load('assets/sprites/gameover.png')
MESSAGE_IMAGE = pygame.image.load('assets/sprites/message.png')

# Scaling the message images to fit the screen better
MESSAGE_IMAGE = pygame.transform.scale(MESSAGE_IMAGE, (SCREEN_WIDTH - 100, int((SCREEN_WIDTH - 100) * MESSAGE_IMAGE.get_height() / MESSAGE_IMAGE.get_width())))

# Yellow bird sprites
YELLOW_BIRD_MID = BIRD_MID  # Rename existing bird images
YELLOW_BIRD_UP = BIRD_UP
YELLOW_BIRD_DOWN = BIRD_DOWN

# Red bird sprites
RED_BIRD_MID = pygame.image.load('assets/sprites/redbird-midflap.png')
RED_BIRD_UP = pygame.image.load('assets/sprites/redbird-upflap.png')
RED_BIRD_DOWN = pygame.image.load('assets/sprites/redbird-downflap.png')

# Blue bird sprites
BLUE_BIRD_MID = pygame.image.load('assets/sprites/bluebird-midflap.png')
BLUE_BIRD_UP = pygame.image.load('assets/sprites/bluebird-upflap.png')
BLUE_BIRD_DOWN = pygame.image.load('assets/sprites/bluebird-downflap.png')

# Scaling all new bird images
RED_BIRD_MID = pygame.transform.scale(RED_BIRD_MID, (BIRD_WIDTH, BIRD_HEIGHT))
RED_BIRD_UP = pygame.transform.scale(RED_BIRD_UP, (BIRD_WIDTH, BIRD_HEIGHT))
RED_BIRD_DOWN = pygame.transform.scale(RED_BIRD_DOWN, (BIRD_WIDTH, BIRD_HEIGHT))

BLUE_BIRD_MID = pygame.transform.scale(BLUE_BIRD_MID, (BIRD_WIDTH, BIRD_HEIGHT))
BLUE_BIRD_UP = pygame.transform.scale(BLUE_BIRD_UP, (BIRD_WIDTH, BIRD_HEIGHT))
BLUE_BIRD_DOWN = pygame.transform.scale(BLUE_BIRD_DOWN, (BIRD_WIDTH, BIRD_HEIGHT))

# Bird configurations
BIRD_TYPES = [
    {'name': 'Yellow', 'sprites': [YELLOW_BIRD_UP, YELLOW_BIRD_MID, YELLOW_BIRD_DOWN, YELLOW_BIRD_MID]},
    {'name': 'Red', 'sprites': [RED_BIRD_UP, RED_BIRD_MID, RED_BIRD_DOWN, RED_BIRD_MID]},
    {'name': 'Blue', 'sprites': [BLUE_BIRD_UP, BLUE_BIRD_MID, BLUE_BIRD_DOWN, BLUE_BIRD_MID]}
]

# Medal assets
SCORE_PANEL = pygame.image.load('assets/sprites/panel.png')
BRONZE_MEDAL = pygame.image.load('assets/sprites/bronze-medal.png')
SILVER_MEDAL = pygame.image.load('assets/sprites/silver-medal.png')
GOLD_MEDAL = pygame.image.load('assets/sprites/gold-medal.png')
PLATINUM_MEDAL = pygame.image.load('assets/sprites/platinum-medal.png')