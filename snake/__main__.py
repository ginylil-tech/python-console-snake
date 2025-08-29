
from . import graphics
from . import theme
from . import gameloop
from . import game
from . import parser
from . import stage
import signal
import sys


def exit():
    graphics.exit()

def signal_handler(sig, frame):
    """Handle signals like Ctrl+C gracefully"""
    exit()
    sys.exit(0)


def run():
    # Set up signal handlers for clean exit
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        parser.init()
        stage.init()
        graphics.init()
        theme.init()
        game.reset()
        gameloop.start()

    except KeyboardInterrupt:
        # User pressed Ctrl+C - normal exit, no need to show error
        pass
    except Exception as e:
        # Any other error occurred - ensure terminal cleanup first, then re-raise
        exit()
        raise  # Re-raise the original exception so user can see it
    else:
        # Normal completion - clean exit
        exit()

if __name__ == '__main__':
    run()
