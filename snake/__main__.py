
import graphics
import theme
import gameloop
import game
import parser
import stage


def exit():
    graphics.exit()


def run():
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

run()
