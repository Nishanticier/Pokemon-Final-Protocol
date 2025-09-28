## This is my first ever serious project ever created, but I made it just for entertainment and did not take into account code organization or effectiveness at that time, therefore please expect this project to be all around messy but still works!

## How to Play

### On macOS
- Double-click `Play_Pokemon_on_Mac.command`

### On Windows
- Double-click `Play_Pokemon_on_Windows.bat`

## Notes
- Both launchers automatically run the game from the `GameFiles/` folder.
- Make sure Python 3 is installed.
- If dependencies are missing, run:
  ```bash
  pip install -r requirements.txt

## About the Launchers
The `.bat` (Windows) and `.command` (Mac) launchers are simple text scripts.  
- They **only run the main Python file** (`GameFiles/scripts/main.py`).  
- You can open them in Notepad/TextEdit to verify before running.

## Troubleshooting

If double-clicking the launcher does not work:

- On macOS:
  Open a Terminal window, navigate into the project folder, and run:
  python3 GameFiles/scripts/main.py
- On Windows:
  Open cmd, navigate into the project folder, and run:
  python GameFiles\scripts\main.py