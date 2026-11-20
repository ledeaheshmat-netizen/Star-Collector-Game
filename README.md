# Star Collector ⭐

A 2D interactive game built using Python and Pygame.

## How to run (Windows)

1. Install Python from https://www.python.org/downloads/
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Run `py -m pip install -r requirements.txt`
5. Run `py main.py`

If `py` is unavailable, replace `py` with `python`.

**Note:** If Pygame does not install with Python 3.15, install Python 3.13 or 3.14 alongside it and run with that version (for example `py -3.13 -m pip install -r requirements.txt` and `py -3.13 main.py`).

## Gameplay
- Press SPACE to start or restart.
- Use arrow keys or WASD to move.
- Collect 15 yellow stars before 60 seconds pass.
- Avoid purple rocks: you have three lives.
- Press ESC to exit.

## Code structure
- `main.py`: game loop, menus, collision outcomes, scoring, timer, and keyboard events.
- `entities.py`: player and falling-object classes, drawing and movement.
- `settings.py`: game configuration constants.
- `requirements.txt`: Python dependencies.

## Implementation summary
The game uses object-oriented classes, lists of falling objects, loops, conditional logic, keyboard events, and Pygame rectangles for collision detection. All visuals are drawn programmatically; no external images are needed.

## Submission
Upload these files to a GitHub repository, and submit the repository URL with the run instructions and a brief description. Test the game on your computer before submitting.
