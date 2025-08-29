
# Removed __main__ import to avoid circular dependency
from . import graphics
from . import game
from . import gameloop
from .config import keys


def update():
    key = graphics.screen.getch()

    if key > 0:
        if key == keys['DOWN']:
            if game.direction[1] == -1:
                return

            game.direction = (0, 1)

        elif key == keys['LEFT']:
            if game.direction[0] == 1:
                return

            game.direction = (-1, 0)

        elif key == keys['RIGHT']:
            if game.direction[0] == -1:
                return

            game.direction = (1, 0)

        elif key == keys['UP']:
            if game.direction[1] == 1:
                return

            game.direction = (0, -1)

        elif key == keys['Q']:
            # Exit the game loop instead of calling __main__.exit() directly
            import sys
            gameloop.stop()
            sys.exit(0)

        elif gameloop.state == 1 and key == keys['ENTER']:
            gameloop.init()
