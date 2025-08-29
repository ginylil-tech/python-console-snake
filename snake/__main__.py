
import graphics
import theme
import gameloop
import game
import parser
import stage
import signal
import sys
import os


def reset_terminal_fallback():
    """Fallback terminal reset using system commands"""
    try:
        # os.system('stty sane 2>/dev/null')
        # os.system('tput reset 2>/dev/null')
        # os.system('tput cnorm 2>/dev/null')
        # os.system('stty echo 2>/dev/null')
    except:
        pass


def exit():
    try:
        graphics.exit()
    except:
        reset_terminal_fallback()


def signal_handler(signum, frame):
    """Handle signals to ensure terminal is restored"""
    print("\nReceived signal %d, cleaning up..." % signum)
    exit()
    sys.exit(0)


def run():
    # Set up signal handlers to ensure terminal restoration
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
        print("\nGame interrupted by user")
        exit()
    except Exception as e:
        # Show the actual error but still restore terminal
        print("\nGame error: %s" % e)
        print("Error type: %s" % type(e).__name__)
        import traceback
        print("\nFull traceback:")
        traceback.print_exc()
        exit()
        sys.exit(1)
    finally:
        # Always ensure terminal is restored
        try:
            exit()
        except:
            reset_terminal_fallback()


if __name__ == "__main__":
    run()
