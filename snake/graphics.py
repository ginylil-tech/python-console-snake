
from . import stage
from . import game
from . import theme
import curses

screen = None


def drawTile(x, y, tile='', color=None):
    color = color or theme.get_color('default')

    x = x * 2 + stage.padding[3] * 2 + stage.width // 2
    y += stage.padding[0] + stage.height // 2

    # Get terminal dimensions to prevent drawing outside bounds
    try:
        max_y, max_x = screen.getmaxyx()
        
        # Only draw if coordinates are within terminal bounds
        if 0 <= y < max_y and 0 <= x < max_x - len(tile):
            screen.addstr(y, x, tile, color)
            if (len(tile) < 2) and x + 1 < max_x:
                screen.addstr(y, x + 1, tile, color)
    except curses.error:
        # Silently ignore curses errors (terminal too small, etc.)
        pass


def drawGameOver():
    drawTile(-4, -1, " GAME OVER ", theme.get_color('border'))
    drawTile(-7, 1, " Press ENTER to restart ", theme.get_color('border'))


def drawScore():
    score_formatted = str(game.score).zfill(2)
    drawTile(
        (stage.width // 2) - 1,
        (-stage.height // 2) - 1,
        score_formatted,
        theme.get_color('border')
        )


def drawLives():
    posx = (-stage.width // 2) + 3
    for x in range(1, game.lives + 1):
        posx += 1
        drawTile(
            posx,
            (-stage.height // 2) - 1,
            theme.get_tile('lives'),
            theme.get_color('lives')
            )
        posx += 1
        drawTile(
            posx,
            (-stage.height // 2) - 1,
            theme.get_tile('border-h'),
            theme.get_color('border')
            )


def drawSnake():
    for part in game.snake:
        drawTile(
            part[0],
            part[1],
            theme.get_tile('snake-body'),
            theme.get_color('snake')
            )
    # Clean last tile
    drawTile(
        game.lastPos[0],
        game.lastPos[1],
        theme.get_tile('bg'),
        theme.get_color('bg')
        )


def drawApples():
    for apple in game.apples:
        drawTile(
            apple[0],
            apple[1],
            theme.get_tile('apple'),
            theme.get_color('apple')
            )


def drawGame():
    for y in range(stage.boundaries['top'], stage.boundaries['bottom']):
        for x in range(stage.boundaries['left'], stage.boundaries['right']):
            drawTile(x, y, theme.get_tile('bg'), theme.get_color('bg'))
    drawBorders()
    drawText()


def drawBorders():
    tile_v = theme.get_tile('border-v')
    tile_h = theme.get_tile('border-h')
    tile_c = theme.get_tile('border-c')
    color = theme.get_color('border')

    x_left = stage.boundaries['left']
    x_right = stage.boundaries['right']

    y_top = stage.boundaries['top']
    y_bottom = stage.boundaries['bottom']

    for y in range(y_top, y_bottom):
        drawTile(x_left - 1, y, tile_v, color)
        drawTile(x_right, y, tile_v, color)

    for x in range(x_left, x_right):
        drawTile(x, y_top - 1, tile_h, color)
        drawTile(x, y_bottom, tile_h, color)

    drawTile(x_left - 1, y_top - 1, tile_c, color)
    drawTile(x_left - 1, y_bottom, tile_c, color)
    drawTile(x_right, y_top - 1, tile_c, color)
    drawTile(x_right, y_bottom, tile_c, color)


def drawText():
    color = theme.get_color('border')
    drawTile((stage.width // 2) - 4, (-stage.height // 2) - 1, "score:", color)
    drawTile((-stage.width // 2), (-stage.height // 2) - 1, "lives:", color)
    drawTile(-5, (stage.height // 2), " Press Q to quit ", color)


def update():

    drawSnake()
    drawApples()
    drawScore()
    drawLives()


def init():
    global screen

    screen = curses.initscr()
    
    # Check if terminal is large enough
    max_y, max_x = screen.getmaxyx()
    min_height, min_width = 10, 20  # Minimum terminal size
    
    if max_y < min_height or max_x < min_width:
        curses.endwin()
        print(f"Terminal too small! Current: {max_x}x{max_y}, Minimum required: {min_width}x{min_height}")
        print("Please resize your terminal and try again.")
        import sys
        sys.exit(1)
    
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    
    # Initialize colors if supported
    if curses.has_colors():
        curses.start_color()
    
    screen.nodelay(1)


def exit():
    try:
        if screen:
            # Clear the screen and refresh
            screen.clear()
            screen.refresh()
            screen.keypad(0)
        
        # Reset all curses settings
        curses.echo()
        curses.nocbreak()
        curses.curs_set(1)  # Restore cursor visibility
        
        # Reset colors to default
        if curses.has_colors():
            curses.use_default_colors()
        
        # Properly end curses mode
        curses.endwin()
        
        # Additional terminal reset to ensure clean state
        import os
        os.system('reset 2>/dev/null || true')
        
    except Exception as e:
        # If curses cleanup fails, try comprehensive terminal reset
        import os
        print(f"Curses cleanup failed: {e}")
        os.system('reset 2>/dev/null || true')
        os.system('stty sane 2>/dev/null || true')
        os.system('tput reset 2>/dev/null || true')
        os.system('tput cnorm 2>/dev/null || true')
        os.system('stty echo 2>/dev/null || true')
        os.system('tput sgr0 2>/dev/null || true')  # Reset all attributes
