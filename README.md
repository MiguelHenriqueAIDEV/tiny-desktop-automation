<div align="center">

<img src="./assets/banner.svg" alt="Tiny Desktop Automation" width="100%" />

<br>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](#tech-stack)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](#run-on-windows)
[![AI-Assisted Development](https://img.shields.io/badge/AI--Assisted_Development-8B5CF6?style=flat-square)](#ai-assisted-development-workflow)
[![Status](https://img.shields.io/badge/Status-Functional-22C55E?style=flat-square)](#highlights)
[![Python Check](https://github.com/MiguelHenriqueAIDEV/tiny-desktop-automation/actions/workflows/python-check.yml/badge.svg)](https://github.com/MiguelHenriqueAIDEV/tiny-desktop-automation/actions/workflows/python-check.yml)

**A Windows automation application that captures screen coordinates, stores local configuration and repeatedly executes configured mouse actions.**

</div>

## Recruiter quick scan

| | |
|---|---|
| **Problem** | Reduce repetitive desktop clicking with a configurable local tool. |
| **Built with** | Python, Tkinter, PyAutoGUI, keyboard, JSON and threading. |
| **Engineering proof** | Architecture notes, manual regression plan, GitHub Actions validation and Dependabot. |
| **My workflow** | Define behavior → implement with AI assistance → test on Windows → debug → refine → validate. |
| **Current status** | Functional and documented; real screenshots are the next portfolio improvement. |

## Why this project exists

Tiny Desktop Automation was built to reduce repetitive desktop clicking through a simple graphical workflow. The project combines desktop GUI development, input automation, persistent configuration and background execution in a compact Python application.

It is also a practical example of **AI-assisted development**: behavior was defined, implemented, tested on Windows, debugged and iteratively refined with Codex Sol assistance.

## Highlights

- **Tkinter desktop interface** for configuration and control
- **Mouse coordinate capture** after a short countdown
- **Two configurable positions per automation mode**
- **Separate Stationary Troops and Moving Troops profiles**
- **Persistent JSON configuration** stored locally
- **Start / Stop controls** and keyboard hotkeys
- **Background automation loop** using threading
- **Configurable cycle delay** in source code
- **GitHub Actions validation workflow** for repository checks
- **Dependabot configuration** for dependency maintenance

> This version does **not** record arbitrary mouse movement, full keyboard sequences or free-form macros. It replays the two configured click positions for the selected mode.

## How it works

```text
Choose automation mode
        ↓
Capture Position 1
        ↓
Capture Position 2
        ↓
Coordinates saved locally
        ↓
Start automation
        ↓
Click Position 1 → Position 2 → repeat
```

## Controls

| Control | Action |
|---|---|
| **Start** | Starts the automation |
| **Stop** | Stops the automation |
| **/** | Toggles running / stopped |
| **ESC** | Stops the automation |
| **Capture Position** | Saves the current mouse coordinates after the countdown |

## Run on Windows

### 1. Requirements

- Python 3
- Windows

### 2. Install dependencies

```powershell
py -m pip install -r requirements.txt
```

Or directly:

```powershell
py -m pip install pyautogui keyboard
```

### 3. Run

```powershell
py tiny.py
```

## Local configuration

The application creates a local file named:

```text
tiny_config.json
```

It stores the configured coordinates for each mode. The file is intentionally ignored by Git so machine-specific coordinates are not published.

## Tech stack

| Area | Technology |
|---|---|
| Language | Python |
| GUI | Tkinter |
| Mouse automation | PyAutoGUI |
| Keyboard hotkeys | keyboard |
| Persistence | JSON |
| Background execution | Threading |
| Development assistance | Codex Sol |
| Repository validation | GitHub Actions |
| Dependency maintenance | Dependabot |

## Engineering documentation

The repository includes additional documentation for reviewers who want to understand the implementation beyond the main README:

- [**Architecture notes →**](docs/architecture.md) — state, threads, persistence, coordinate capture and automation loop.
- [**Manual test plan →**](docs/testing.md) — Windows validation scenarios and regression checklist.
- [**Development notes →**](docs/development.md) — iterative AI-assisted development workflow.

## AI-assisted development workflow

Codex Sol was used as a development assistant while the behavior and final validation remained human-directed.

```text
Requirement
   ↓
Prompt-driven implementation
   ↓
Windows testing
   ↓
Behavior / timing issues identified
   ↓
Refinement and debugging
   ↓
Re-test
   ↓
Validated working version
```

This repository documents the project as **AI-Assisted Development**, not autonomous AI generation.

## Repository structure

```text
tiny-desktop-automation/
├── tiny.py
├── requirements.txt
├── README.md
├── .gitignore
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       └── python-check.yml
├── assets/
│   └── banner.svg
└── docs/
    ├── architecture.md
    ├── development.md
    └── testing.md
```

## Screenshots

Real application screenshots are the next visual improvement planned for this repository.

Planned paths:

```text
assets/application.png
assets/capture-position.png
```

## Future ideas

These are **planned ideas**, not current functionality:

- arbitrary action recording
- recorded-sequence replay
- per-action timing
- additional automation profiles
- import / export of profiles

---

<div align="center">

**Built with Python · Tested on Windows · Documented for review · Refined with AI assistance**

</div>
