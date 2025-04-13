import pygame as pg

# Init pygame
pg.init()

# Color constant
BLACK: pg.Color = pg.Color(0, 0, 0)
RED: pg.Color = pg.Color(255, 0, 0)
GREEN: pg.Color = pg.Color(0, 255, 0)
BLUE: pg.Color = pg.Color(0, 0, 255)

# Window constant
WINDOW_SIZE: tuple[int, int] = (1080, 720)

FRAMERATE: int = 60
BACKGROUND_COLOR: pg.Color = BLACK
