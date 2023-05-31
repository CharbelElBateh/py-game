# Imports
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    def __init__(self):

        # Initialize Pygame modules
        pg.init()

        # Turn off the mouse
        pg.mouse.set_visible(False)

        # Create a screen
        self.screen = pg.display.set_mode(RES)

        # Clock for the frame rate
        self.clock = pg.time.Clock()

        # Time
        self.delta_time = 1

        # Make death animations faster
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    # Initialize the game with all the objects
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    # update the FPS on the screen
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :1f}')

    # Render the enemies and the weapon
    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()

    # Mouse click / Movement / Camera / Quitting mechanisms
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    # Keep running the game through a loop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

# Run the game on running the command
if __name__ == '__main__':
    game = Game()
    game.run()