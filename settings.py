import os
from enum import Enum

GAME_TITLE = 'Frogger PyGame'
VERSION = '1.0.0'

# Screen dimensions and grid
WIDTH = 600
HEIGHT = 800
WINDOW_SIZE = (WIDTH, HEIGHT)
CELL_SIZE = 50
GRID_COLS = WIDTH // CELL_SIZE
GRID_ROWS = HEIGHT // CELL_SIZE
FPS = 30

# Media directory and colors
MEDIA_DIR = os.path.join(os.path.dirname(__file__), 'media')
COLORS = {
    'pastel-green': 0x77dd77,
    'grey-green': 0x81d381,
    'malachite': 0x0bda51,
}


# Entity / object categories
class EntityType(Enum):
    PLAYER = 'player'
    CAR = 'car'
    LOG = 'log'
    TURTLE = 'turtle'
    WATER = 'water'
    SAFE = 'safe'
    HOME = 'home'
    OTHER = 'other'


# Game states
class GameState(Enum):
    MENU = 'menu'
    PLAYING = 'playing'
    GAME_OVER = 'game_over'
    PAUSED = 'paused'
    WIN = 'win'
