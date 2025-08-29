# Phase 4: String/Unicode Handling ❌

## Objective
Update string and unicode handling for Python 3's unified string model.

## Python 2 vs 3 String Changes

### String Types
- **Python 2**: `str` (bytes), `unicode` (text)
- **Python 3**: `str` (text), `bytes` (bytes)
- **Impact**: All strings are unicode by default in Python 3

### Key Areas in Snake Game

#### Terminal/Curses Output
- **Files**: `snake/graphics.py`, `snake/theme.py`
- **Concern**: Character rendering, tile symbols
- **Change**: Ensure proper string encoding for terminal display

#### Configuration Strings
- **Files**: `snake/config.py`, `snake/themes.py`
- **Concern**: Key mappings, theme symbols
- **Change**: Verify unicode characters work correctly

#### File I/O (if any)
- **Files**: Any modules reading/writing files
- **Change**: Explicit encoding specification

## Specific Updates Needed

### Theme Symbols & Tiles
```python
# Python 2 style (may be present)
tile_chars = {
    'snake': u'█',
    'apple': u'●',
    'empty': u' '
}

# Python 3 (strings are unicode by default)
tile_chars = {
    'snake': '█',
    'apple': '●', 
    'empty': ' '
}
```

### Curses Integration
- **File**: `snake/graphics.py`
- **Concern**: curses.addstr() may need encoding attention
- **Test**: Unicode characters display correctly in terminal

### String Formatting
- **Modern approach**: Use f-strings where beneficial
- **Maintain compatibility**: Keep existing format for stability

## Files to Update
- [ ] `snake/graphics.py` - character rendering and display
- [ ] `snake/theme.py` - theme symbol handling
- [ ] `snake/themes.py` - theme character definitions
- [ ] `snake/config.py` - any string constants
- [ ] `menu.py` - user interface text

## Testing Checklist
- [ ] Game characters display correctly in terminal
- [ ] Theme symbols render properly
- [ ] No string/unicode related errors
- [ ] Terminal output formatting preserved
- [ ] Multi-byte characters work (if used)

## Curses-Specific Testing
- [ ] Snake body renders correctly
- [ ] Apple symbols display properly  
- [ ] Game borders and padding work
- [ ] Score/status text displays correctly
- [ ] All theme variations work

## Character Encoding Validation
1. Test in various terminal emulators
2. Verify UTF-8 compatibility
3. Check ASCII fallback behavior
4. Test with different locale settings

## Risk Mitigation
- **Low Risk**: Game uses simple ASCII/basic unicode
- **Fallback**: Maintain ASCII alternatives for compatibility
- **Testing**: Test on multiple terminal types and encodings
