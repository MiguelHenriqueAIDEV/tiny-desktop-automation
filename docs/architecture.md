# Architecture Notes

This document explains the current architecture of **Tiny Desktop Automation** as implemented in `tiny.py`.

## Main components

```text
Tkinter UI
   │
   ├── Start / Stop controls
   ├── Mode selection
   └── Coordinate capture
          │
          ↓
Configuration state
   │
   ├── Stationary Troops
   │     ├── Position 1
   │     └── Position 2
   │
   └── Moving Troops
         ├── Position 1
         └── Position 2
          │
          ↓
Local JSON persistence
          │
          ↓
Background click loop
          │
          ├── Read active mode
          ├── Read configured positions
          ├── Click Position 1
          ├── Click Position 2
          └── Wait for cycle delay
```

## Configuration

The application starts with default coordinate values and attempts to load saved values from `tiny_config.json`.

Each mode stores two coordinate pairs:

```text
Mode
├── pos1
│   ├── x
│   └── y
└── pos2
    ├── x
    └── y
```

The JSON file is machine-specific and intentionally excluded from Git.

## Coordinate capture

When the user clicks a **Capture position** button:

1. the interface displays a countdown message;
2. a background worker waits five seconds;
3. `pyautogui.position()` reads the current cursor coordinates;
4. the selected mode / position is updated;
5. the configuration is saved to JSON;
6. the GUI label is refreshed.

The delay gives the user time to move the mouse to the desired target before capture.

## Automation loop

The click loop runs in a daemon thread so the Tkinter main loop remains responsive.

During each iteration it:

1. checks whether the program is closing;
2. checks keyboard shortcuts;
3. reads the current running state and active mode;
4. reads Position 1 and Position 2;
5. clicks both positions when automation is enabled;
6. waits for the configured cycle delay.

When automation is stopped, the loop sleeps briefly instead of executing clicks.

## Keyboard controls

The current implementation polls keyboard state inside the automation thread:

```text
/   → toggle running / stopped
ESC → stop automation
```

A short debounce delay is applied after a shortcut is detected to reduce repeated toggles while a key remains pressed.

## Thread safety

Shared application state is protected with a `threading.Lock` when reading or writing values such as:

- `running`;
- `closing`;
- `active_mode`;
- stored coordinates.

Tkinter UI changes that originate from worker threads are scheduled through `root.after(...)` rather than directly manipulating widgets from the worker.

## Persistence behavior

The application writes configuration using JSON with indentation for readability.

If the configuration file does not exist, default coordinates are used.

If loading the saved configuration fails, the current implementation falls back to defaults rather than terminating the application.

## Current limitations

The architecture is intentionally small and has several known limits:

- only two click positions exist per mode;
- the cycle delay is defined in source code;
- there is no arbitrary macro recorder;
- mouse movement is not recorded;
- keyboard sequences are not replayed;
- there is no profile import / export UI.

These limitations are documented as current behavior rather than hidden behind future-feature claims.
