# Phase 6: Exception Handling Modernization ❌

## Objective
Modernize exception handling syntax and improve error robustness for Python 3.

## Exception Syntax Changes

### Python 2 vs 3 Syntax
- **Python 2**: `except Exception, e:`
- **Python 3**: `except Exception as e:`
- **Impact**: All try/except blocks need updating

## Exception Handling Areas in Snake Game

### Input/Output Operations
- **Files**: `snake/console.py`, `snake/graphics.py`
- **Scenarios**: Terminal operations, curses initialization
- **Exceptions**: `curses.error`, `OSError`, `IOError`

### Game Initialization
- **Files**: `snake/__main__.py`, `snake/run.py`, `snake/graphics.py`
- **Scenarios**: Curses setup, terminal configuration
- **Exceptions**: Import errors, initialization failures

### User Input Handling
- **Files**: `snake/controls.py`, `snake/gameloop.py`
- **Scenarios**: Keyboard input, signal handling
- **Exceptions**: `KeyboardInterrupt`, input errors

### Configuration & Parsing
- **Files**: `snake/parser.py`, `snake/config.py`
- **Scenarios**: CLI argument parsing, configuration loading
- **Exceptions**: `ValueError`, `AttributeError`

## Files to Update

### Core Exception Handling
- [ ] `snake/graphics.py` - curses initialization and rendering
- [ ] `snake/console.py` - terminal operations
- [ ] `snake/controls.py` - input handling
- [ ] `snake/gameloop.py` - main game loop
- [ ] `snake/__main__.py` - application entry point
- [ ] `snake/run.py` - alternative entry point
- [ ] `snake/parser.py` - CLI parsing

### Enhanced Error Handling Opportunities
- [ ] Add graceful degradation for unsupported terminals
- [ ] Improve error messages for user guidance
- [ ] Add proper cleanup in exception paths

## Modernization Improvements

### Current Exception Patterns (to find and update)
```python
# Python 2 style
try:
    curses.initscr()
except curses.error, e:
    print "Curses error:", e

# Python 3 style  
try:
    curses.initscr()
except curses.error as e:
    print("Curses error:", e)
```

### Enhanced Exception Handling
```python
# More specific exception handling
try:
    curses.initscr()
    curses.start_color()
except curses.error as e:
    print(f"Terminal does not support required features: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error initializing display: {e}")
    sys.exit(1)
```

## Testing Checklist

### Exception Path Testing
- [ ] Game exits gracefully on Ctrl+C
- [ ] Proper cleanup when terminal is resized
- [ ] Correct error messages for invalid arguments
- [ ] Graceful handling of unsupported terminals
- [ ] Recovery from temporary input issues

### Error Message Quality
- [ ] User-friendly error descriptions
- [ ] Helpful guidance for common issues
- [ ] No stack traces for expected errors
- [ ] Clear indication of terminal requirements

### Terminal Compatibility
- [ ] Graceful degradation on limited terminals
- [ ] Proper error handling for missing curses support
- [ ] Clean exit when terminal is too small
- [ ] Handling of terminal capability detection

## Specific Exception Scenarios

### Curses Initialization
```python
try:
    stdscr = curses.initscr()
    curses.start_color()
    curses.curs_set(0)
except curses.error as e:
    print(f"Error: Terminal does not support required features ({e})")
    print("Please use a different terminal or check terminal settings.")
    sys.exit(1)
```

### Terminal Size Issues
```python
try:
    height, width = stdscr.getmaxyx()
    if height < MIN_HEIGHT or width < MIN_WIDTH:
        raise ValueError(f"Terminal too small: {width}x{height}")
except Exception as e:
    print(f"Error: {e}")
    print(f"Minimum terminal size required: {MIN_WIDTH}x{MIN_HEIGHT}")
    sys.exit(1)
```

### Keyboard Interrupt Handling
```python
try:
    gameloop.start()
except KeyboardInterrupt:
    print("\nGame interrupted by user")
finally:
    graphics.cleanup()
    curses.endwin()
```

## Validation Steps
1. **Syntax Validation**: Ensure all except statements use `as` syntax
2. **Exception Testing**: Trigger various error conditions deliberately  
3. **Graceful Exit**: Verify clean shutdown in all error cases
4. **User Experience**: Test error messages are helpful and clear
5. **Resource Cleanup**: Ensure proper cleanup in exception paths

## Benefits of Modernization
- Better error messages for users
- More robust terminal compatibility
- Cleaner code with modern Python idioms
- Improved debugging capabilities
- Enhanced user experience with better error handling
