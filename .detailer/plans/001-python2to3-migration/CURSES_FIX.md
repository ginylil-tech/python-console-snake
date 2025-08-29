# Curses Compatibility Fix

## Issue
The game was experiencing `_curses.error: addwstr() returned ERR` when trying to draw to the terminal. This typically happens when:
- Terminal window is too small
- Trying to draw outside terminal boundaries
- Terminal doesn't support required features

## Solution Applied

### 1. Bounds Checking in drawTile()
Added proper boundary checking before drawing:
```python
def drawTile(x, y, tile='', color=None):
    # ... coordinate calculations ...
    
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
```

### 2. Terminal Size Validation
Added minimum terminal size checking:
```python
def init():
    # ... screen initialization ...
    
    # Check if terminal is large enough
    max_y, max_x = screen.getmaxyx()
    min_height, min_width = 10, 20  # Minimum terminal size
    
    if max_y < min_height or max_x < min_width:
        curses.endwin()
        print(f"Terminal too small! Current: {max_x}x{max_y}, Minimum required: {min_width}x{min_height}")
        print("Please resize your terminal and try again.")
        sys.exit(1)
```

### 3. Color Support Detection
Added check for color support:
```python
# Initialize colors if supported
if curses.has_colors():
    curses.start_color()
```

## Result
- Game now handles small terminals gracefully
- Drawing operations are protected from boundary errors
- Clear error messages for terminal size issues
- Better compatibility across different terminal types

The game should now run reliably on Python 3 across various terminal environments.
