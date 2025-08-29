# Phase 2: Core Syntax Updates ❌

## Objective
Update core Python syntax from Python 2 to Python 3 patterns.

## Primary Changes

### Print Statement → Print Function
- **Files Affected**: Likely `snake/graphics.py`, `snake/game.py`, debug statements
- **Change**: `print "text"` → `print("text")`
- **Impact**: Low - straightforward replacement

### Exception Handling Syntax
- **Files Affected**: All modules with try/except blocks
- **Change**: `except Exception, e:` → `except Exception as e:`
- **Impact**: Low - syntax only

### Integer Division
- **Files Affected**: `snake/stage.py`, `snake/graphics.py` (layout calculations)
- **Change**: Ensure `//` for floor division, `/` for float division
- **Impact**: Medium - may affect game layout calculations

### Dictionary Iteration
- **Files Affected**: `snake/themes.py`, `snake/config.py`
- **Change**: `.iteritems()` → `.items()`, `.iterkeys()` → `.keys()`
- **Impact**: Low - direct replacement

## Files to Update
- [ ] `snake/graphics.py` - rendering and debug output
- [ ] `snake/game.py` - game logic calculations
- [ ] `snake/stage.py` - layout calculations
- [ ] `snake/config.py` - configuration parsing
- [ ] `snake/themes.py` - theme iteration
- [ ] `menu.py` - user interaction output
- [ ] All other modules - error handling

## Testing Checklist
- [ ] Game starts without syntax errors
- [ ] All print outputs work correctly
- [ ] Game layout calculations are accurate
- [ ] Exception handling works properly
- [ ] No runtime errors from syntax changes

## Validation Steps
1. Run `python3 -m py_compile` on each module
2. Execute game with various options
3. Test error conditions and exception paths
4. Verify visual layout matches original

## Backup Strategy
- Commit changes incrementally per module
- Test each module individually before proceeding
- Maintain rollback capability at each step
