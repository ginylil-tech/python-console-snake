# Phase 3: Import & Module System Updates ❌

## Objective
Update import statements and module references for Python 3 compatibility.

## Import System Changes

### Relative Imports
- **Current**: Implicit relative imports in Python 2
- **Target**: Explicit relative imports with dot notation
- **Files Affected**: All modules in `snake/` package

### Module Structure
```
snake/
├── __init__.py          # Package initialization
├── __main__.py          # Entry point - imports from . package
├── config.py            # Constants - no imports needed
├── console.py           # Utilities - os, fcntl, termios, struct
├── controls.py          # Input handling - imports from . package
├── game.py              # Core logic - imports from . package  
├── gameloop.py          # Main loop - imports from . package
├── graphics.py          # Rendering - imports curses, from . package
├── parser.py            # CLI parsing - imports argparse
├── run.py               # Alt entry - imports from . package
├── stage.py             # Layout - imports from . package
├── theme.py             # Theme management - imports from . package
└── themes.py            # Theme data - no imports needed
```

## Expected Import Updates

### Internal Package Imports
- **From**: `import config` (implicit relative)
- **To**: `from . import config` (explicit relative)
- **Files**: Most modules in snake/ package

### Entry Point Imports
- **File**: `snake/__main__.py`
- **Ensure**: Proper package-relative imports
- **Pattern**: `from . import module_name`

### External Imports
- **Standard Library**: Should work unchanged
- **Verify**: curses, os, random, math, time, subprocess compatibility

## Files to Update
- [ ] `snake/__main__.py` - main entry point imports
- [ ] `snake/run.py` - alternative entry point imports  
- [ ] `snake/gameloop.py` - core loop dependencies
- [ ] `snake/graphics.py` - rendering dependencies
- [ ] `snake/controls.py` - input handling dependencies
- [ ] `snake/game.py` - game logic dependencies
- [ ] `snake/stage.py` - layout dependencies
- [ ] `snake/theme.py` - theme system dependencies

## Testing Checklist
- [ ] `python3 -m snake` executes without import errors
- [ ] `python3 snake/run.py` executes without import errors
- [ ] All modules can be imported individually
- [ ] No circular import issues
- [ ] Package structure remains clean

## Import Validation
1. Test package import: `python3 -c "import snake"`
2. Test entry points: `python3 -m snake --help`
3. Test individual modules: `python3 -c "from snake import game"`
4. Verify no warnings about deprecated import patterns

## Common Issues to Watch
- Circular imports (especially gameloop ↔ graphics ↔ game)
- Missing `__init__.py` imports
- Incorrect relative import syntax
- Standard library module name changes (rare but possible)
