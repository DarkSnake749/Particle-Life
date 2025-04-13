import pygame as pg
from src.config import *

class Window:
    def __init__(self) -> None: 
        # Window
        self.window: pg.Surface = pg.display.set_mode(WINDOW_SIZE)
        pg.display.set_caption("Engine")

        # Window controller
        self.clock: pg.time.Clock = pg.time.Clock()
        """ Control the framerate of the window """

        self.quit: bool = False
        """ Control the main loop via internal function (e.g event_loop)"""
    
    def event_loop(self) -> None:
        for event in pg.event.get():
            self.quit = True if event.type == pg.QUIT else self.quit
    
    def run(self) -> None:
        while not self.quit:
            # Compute events
            self.event_loop()

            # Clear the window
            self.window.fill(BACKGROUND_COLOR)

            # Update the window
            pg.display.flip()
            self.clock.tick(FRAMERATE)
        
        pg.quit()
        exit(0)
