# Map Camera Fix for Guerre en Amerique Mod

## Problem
Your map is too large and the camera cannot zoom out far enough to see the entire map.

## Current Settings
```ini
map_min_x   = -400
map_max_x   = 400
map_min_y   = -400
map_max_y   = 400
map_max_distance = 175.0
```

## Issue
Your map boundaries are 800x800 units, but `map_max_distance` is only 175.0, which limits how far the camera can zoom out.

## Solution
Increase the `map_max_distance` value in your `module.ini` file. The maximum value is approximately 251.0.

## Recommended Settings

### Option 1: Maximum Zoom (Recommended for Large Maps)
```ini
map_min_x   = -400
map_max_x   = 400
map_min_y   = -400
map_max_y   = 400
map_max_distance = 251.0
```

### Option 2: Moderate Zoom
```ini
map_min_x   = -400
map_max_x   = 400
map_min_y   = -400
map_max_y   = 400
map_max_distance = 220.0
```

## Additional Camera Settings

You can also adjust these settings for better camera control:

```ini
map_min_elevation = 0.2
# Sets the minimum distance the camera can be from the terrain

map_max_elevation = 1.0
# Sets the maximum distance the camera can be from the terrain
```

## How to Apply

1. Open `Guerre en Amerique Assets/module.ini`
2. Find the line `map_max_distance = 175.0`
3. Change it to `map_max_distance = 251.0`
4. Save the file
5. Launch the game and test

## Understanding the Settings

- **map_min_x / map_max_x**: Eastern and western boundaries of the world map
- **map_min_y / map_max_y**: Northern and southern boundaries of the world map
- **map_max_distance**: Maximum zoom out distance (max ~251.0)
- **map_min_elevation**: Minimum camera height above terrain
- **map_max_elevation**: Maximum camera height above terrain

## Testing

After applying the fix:
1. Launch Mount & Blade Warband
2. Load your mod
3. Enter the campaign map
4. Use the mouse wheel to zoom out
5. You should now be able to see the entire map

## Notes

- The maximum value for `map_max_distance` is approximately 251.0
- If you still can't see the entire map, your map might be too large for the engine's limitations
- Consider adjusting your map boundaries if needed