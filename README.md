# Tiny Desktop Automation

Python desktop automation tool for Windows that captures screen coordinates, stores local configurations and replays configurable mouse actions.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![AI-Assisted Development](https://img.shields.io/badge/AI--Assisted%20Development-8B5CF6?style=flat-square)](#ai-assisted-development)
[![Status](https://img.shields.io/badge/Status-Functional-22C55E?style=flat-square)](#features)

## About

Tiny Desktop Automation is a small Windows desktop application developed to automate repetitive click sequences. It provides a graphical interface for configuring two mouse positions for each available automation mode, capturing coordinates from the screen, saving the configuration locally, and repeatedly clicking the configured positions.

The project demonstrates Python desktop development, GUI development with Tkinter, mouse automation, keyboard hotkeys, local configuration persistence, and iterative AI-assisted development.

## Features

The current implementation includes:

- graphical interface built with Tkinter;
- capture of mouse coordinates after a countdown;
- configurable Position 1 and Position 2 for each mode;
- separate automation modes;
- persistent coordinate configuration through a local JSON file;
- automatic clicking on configured positions;
- Start and Stop controls;
- `/` keyboard shortcut to toggle the automation;
- `ESC` to stop the automation;
- a delay between automation cycles, defined by the `DELAY` constant in the source;
- background execution using threads.

This version does not record complete mouse movements, keyboard sequences, or arbitrary action sequences. It works with the two configured positions in the selected mode.

## Current Modes

The application currently provides two modes:

```text
Stationary Troops
Moving Troops
```

Each mode has its own pair of configurable positions:

```text
Position 1
Position 2
```

## How It Works

```text
Choose mode
   ↓
Capture Position 1
   ↓
Capture Position 2
   ↓
Coordinates are saved locally
   ↓
Start automation
   ↓
Application repeatedly clicks both positions
```

When a position is captured, the application waits for the countdown and then reads the current mouse coordinates. The coordinates are stored in the local configuration file for the selected mode and position.

## Installation / How to Run on Windows

### 1. Install Python

Install Python 3 for Windows and make sure the Python launcher `py` is available in PowerShell.

### 2. Open PowerShell in the project folder

Open PowerShell in the folder where `tiny.py` is located.

### 3. Install dependencies

Install the dependencies once with:

```powershell
py -m pip install -r requirements.txt
```

Alternatively, install them directly:

```powershell
py -m pip install pyautogui keyboard
```

### 4. Run the program

From the project folder, run:

```powershell
py "tiny.py"
```

If the file is in the Downloads folder, use the corresponding Windows path:

```powershell
py "C:\Users\USER_NAME\Downloads\tiny.py"
```

Replace `USER_NAME` with the Windows account folder name on the computer where the program is being run.

## Controls

| Control | Action |
| --- | --- |
| Start | Starts the automation |
| Stop | Stops the automation |
| `/` | Toggles between running and stopped |
| `ESC` | Stops the automation |
| Capture Position | Captures mouse coordinates after the countdown |

## Local Configuration

The program creates a local file named:

```text
tiny_config.json
```

This file stores the configured coordinates for the available modes and positions. It is generated locally by the program, is ignored by Git, and should not be committed to the repository. No personal or real user coordinates are included in this documentation.

## AI-Assisted Development

This project was developed and refined with AI assistance using Codex Sol.

AI was used as a development tool while the project remained guided by explicit behavioral requirements and human validation. The workflow included definition of the desired behavior, prompt-driven implementation, testing on Windows, coordinate calibration, delay adjustments, debugging, iterative refinement, and validation of the final behavior.

The project is presented as **AI-Assisted Development**, not as a product created autonomously by AI.

## Tech Stack

| Area | Technology or tool |
| --- | --- |
| Programming language | Python |
| GUI | Tkinter |
| Mouse automation | PyAutoGUI |
| Keyboard hotkeys | keyboard |
| Local persistence | JSON |
| Concurrency | Threading |
| Development assistance | Codex Sol |

Codex Sol is included as an AI-assisted development tool. It is not a Python runtime dependency.

## Screenshots

Screenshots will be added later. No images are included in this initial publication.

```text
assets/
├── application.png
└── capture-position.png
```

## Planned / Future Ideas

The following items are future ideas and are not current features of this version:

- recording arbitrary action sequences;
- replaying recorded actions;
- configurable delays per action;
- additional automation profiles;
- import/export of profiles.
