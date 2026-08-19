# Manual Test Plan

This project currently relies on **manual Windows validation** because its main behavior depends on real mouse coordinates, desktop focus and keyboard input.

The following test plan documents the behaviors that should be checked after changes.

## Environment

- Windows
- Python 3
- `pyautogui`
- `keyboard`

## Test cases

| ID | Scenario | Steps | Expected result |
|---|---|---|---|
| T01 | Application starts | Run `py tiny.py` | Tkinter window opens without crashing |
| T02 | Default state | Open application | Status shows stopped and default mode is selected |
| T03 | Capture Position 1 | Click capture, move cursor before countdown ends | Position 1 updates to current cursor coordinates |
| T04 | Capture Position 2 | Click capture, move cursor before countdown ends | Position 2 updates to current cursor coordinates |
| T05 | Persistence | Capture coordinates, close and reopen app | Saved coordinates are loaded from `tiny_config.json` |
| T06 | Mode isolation | Configure different coordinates for each mode | Switching modes preserves separate coordinate pairs |
| T07 | Start button | Click Start | Automation begins clicking configured positions |
| T08 | Stop button | Click Stop | Repeated clicking stops |
| T09 | Slash shortcut | Press `/` | Running state toggles |
| T10 | Escape shortcut | Start automation and press `ESC` | Automation stops |
| T11 | Configuration file missing | Delete local `tiny_config.json`, reopen app | Application loads default coordinates instead of failing |
| T12 | Window close | Close the Tkinter window | Application exits cleanly |

## Safe testing recommendation

Before testing the automation loop, configure both positions over a harmless area such as an empty text editor or desktop region.

Avoid testing over destructive UI controls such as:

- delete buttons;
- purchase / payment buttons;
- account settings;
- system shutdown controls.

## Regression checklist

After modifying the code, verify at minimum:

- [ ] application launches;
- [ ] both modes can be selected;
- [ ] both positions can be captured;
- [ ] coordinates persist after restart;
- [ ] Start begins automation;
- [ ] Stop ends automation;
- [ ] `/` toggles automation;
- [ ] `ESC` stops automation;
- [ ] GUI remains responsive while the click loop is active;
- [ ] closing the window terminates the app.

## Future automated testing opportunities

Some internal behavior could later be separated from GUI / OS input to make unit testing easier, for example:

- configuration loading and saving;
- mode state management;
- validation of coordinate data;
- timing / state-transition logic.

Actual mouse clicks and global keyboard input would still benefit from end-to-end manual validation on Windows.
