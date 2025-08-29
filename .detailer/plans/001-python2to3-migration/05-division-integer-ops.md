# Phase 5: Division & Integer Operations ❌

## Objective
Ensure mathematical operations work correctly with Python 3's division behavior changes.

## Division Behavior Changes

### Python 2 vs 3 Division
- **Python 2**: `/` = integer division for integers, float division for floats
- **Python 3**: `/` = always float division, `//` = floor division
- **Impact**: Layout calculations, positioning, timing

## Critical Areas in Snake Game

### Stage Layout Calculations
- **File**: `snake/stage.py`
- **Operations**: Terminal size calculations, padding, boundaries
- **Risk**: Game area size, positioning accuracy

### Graphics Positioning  
- **File**: `snake/graphics.py`
- **Operations**: Coordinate calculations, tile positioning
- **Risk**: Snake/apple positioning, visual alignment

### Game Logic Calculations
- **File**: `snake/game.py`
- **Operations**: Snake movement, collision detection
- **Risk**: Game mechanics accuracy

### Timing Calculations
- **File**: `snake/gameloop.py`, `snake/config.py`
- **Operations**: Frame timing, game speed
- **Risk**: Game performance, timing accuracy

## Files to Review & Update

### Priority 1: Layout & Positioning
- [ ] `snake/stage.py` - Terminal/game area calculations
- [ ] `snake/graphics.py` - Coordinate and positioning math
- [ ] `snake/console.py` - Terminal size calculations

### Priority 2: Game Logic
- [ ] `snake/game.py` - Movement and collision math
- [ ] `snake/gameloop.py` - Timing calculations

### Priority 3: Configuration
- [ ] `snake/config.py` - Numeric constants and calculations

## Specific Changes Needed

### Ensure Integer Results Where Required
```python
# Example layout calculation
# Python 2: width / 2 (integer result for integers)
# Python 3: width // 2 (explicit floor division)

# For centering calculations
center_x = width // 2
center_y = height // 2

# For grid positioning  
grid_x = pixel_x // tile_size
grid_y = pixel_y // tile_size
```

### Preserve Float Division Where Needed
```python
# For proportional calculations
aspect_ratio = width / height  # Keep as float division
scale_factor = target_size / current_size  # Keep as float
```

## Testing Checklist

### Visual Layout Testing
- [ ] Game area centers correctly in terminal
- [ ] Snake segments align properly
- [ ] Apples appear at correct grid positions
- [ ] Game boundaries are accurate
- [ ] Padding/margins are correct

### Game Mechanics Testing  
- [ ] Snake movement is pixel-perfect
- [ ] Collision detection is accurate
- [ ] Apple spawning positions are valid
- [ ] Game timing feels correct

### Cross-Platform Testing
- [ ] Different terminal sizes work correctly
- [ ] Various screen resolutions supported
- [ ] Consistent behavior across platforms

## Validation Steps
1. **Visual Inspection**: Compare game layout before/after migration
2. **Coordinate Testing**: Log positions to verify accuracy
3. **Boundary Testing**: Test edge cases and collision boundaries
4. **Performance Testing**: Ensure timing calculations are correct

## Mathematical Operations Audit
- Division operations: `/` vs `//`
- Modulo operations: `%` (should work unchanged)
- Rounding operations: `round()`, `int()`, `math.floor()`
- Coordinate transformations: screen ↔ game coordinates

## Risk Assessment
- **High Impact**: Layout miscalculations could break game visuals
- **Medium Impact**: Timing changes could affect game feel
- **Low Impact**: Most operations likely already integer-based
- **Mitigation**: Thorough testing with various terminal sizes
