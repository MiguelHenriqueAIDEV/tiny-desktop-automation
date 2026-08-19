import tkinter as tk
import pyautogui
import keyboard
import threading
import time
import json
import os


DELAY = 0.33
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tiny_config.json")
MODE_ALIASES = {
    "Stationary Troops": "\u0054\u0072\u006f\u0070\u0061\u0073 \u0050\u0061\u0072\u0061\u0064\u0061\u0073",
    "Moving Troops": "\u0054\u0072\u006f\u0070\u0061\u0073 \u0041\u006e\u0064\u0061\u006e\u0064\u006f",
}


def default_config():
    return {
        "Stationary Troops": {
            "pos1": {"x": 1103, "y": 853},
            "pos2": {"x": 863, "y": 775},
        },
        "Moving Troops": {
            "pos1": {"x": 1103, "y": 853},
            "pos2": {"x": 863, "y": 775},
        },
    }


def load_config():
    config = default_config()

    if not os.path.exists(CONFIG_FILE):
        return config

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            saved = json.load(file)

        for mode in config:
            saved_mode = saved.get(mode)
            old_mode = MODE_ALIASES.get(mode)
            if saved_mode is None and old_mode:
                saved_mode = saved.get(old_mode)

            if saved_mode is None:
                continue

            for pos in config[mode]:
                if pos in saved_mode:
                    config[mode][pos]["x"] = int(saved_mode[pos].get("x", config[mode][pos]["x"]))
                    config[mode][pos]["y"] = int(saved_mode[pos].get("y", config[mode][pos]["y"]))
    except Exception:
        pass

    return config


def save_config():
    with lock:
        data = {
            mode: {
                pos: {
                    "x": coords["x"],
                    "y": coords["y"],
                }
                for pos, coords in positions.items()
            }
            for mode, positions in config.items()
        }

    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def safe_after(delay, callback):
    try:
        root.after(delay, callback)
    except Exception:
        pass


def update_status():
    with lock:
        is_running = running
        mode = active_mode

    status_var.set("Running" if is_running else "Stopped")
    active_mode_var.set("Active mode: " + mode)


def update_coordinate_labels():
    with lock:
        for mode in config:
            for pos in config[mode]:
                x = config[mode][pos]["x"]
                y = config[mode][pos]["y"]
                coordinate_vars[mode][pos].set("X=" + str(x) + ", Y=" + str(y))


def set_running(value):
    global running

    with lock:
        running = value

    safe_after(0, update_status)


def toggle_running():
    global running

    with lock:
        running = not running

    safe_after(0, update_status)


def use_mode(mode):
    global active_mode

    with lock:
        active_mode = mode

    message_var.set("")
    update_status()


def capture_position(mode, pos):
    message_var.set("Place the mouse on the desired position. Capturing in 5 seconds...")

    def worker():
        time.sleep(5)
        x, y = pyautogui.position()

        with lock:
            config[mode][pos]["x"] = x
            config[mode][pos]["y"] = y

        save_config()

        def finish():
            update_coordinate_labels()
            message_var.set("Position captured: X=" + str(x) + ", Y=" + str(y))

        safe_after(0, finish)

    threading.Thread(target=worker, daemon=True).start()


def click_loop():
    while True:
        with lock:
            if closing:
                break

        if keyboard.is_pressed("esc"):
            set_running(False)
            time.sleep(0.3)

        if keyboard.is_pressed("/"):
            toggle_running()
            time.sleep(0.3)

        with lock:
            is_running = running
            mode = active_mode
            pos1_x = config[mode]["pos1"]["x"]
            pos1_y = config[mode]["pos1"]["y"]
            pos2_x = config[mode]["pos2"]["x"]
            pos2_y = config[mode]["pos2"]["y"]

        if is_running:
            pyautogui.click(pos1_x, pos1_y)
            pyautogui.click(pos2_x, pos2_y)
            time.sleep(DELAY)
        else:
            time.sleep(0.01)


def close_program():
    global closing, running

    with lock:
        closing = True
        running = False

    root.destroy()


def create_mode_frame(parent, mode):
    frame = tk.LabelFrame(parent, text=mode, padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=8)

    tk.Label(frame, text="Position 1").grid(row=0, column=0, sticky="w", padx=4, pady=4)
    tk.Label(frame, textvariable=coordinate_vars[mode]["pos1"]).grid(row=0, column=1, sticky="w", padx=4, pady=4)
    tk.Button(frame, text="Capture position 1", command=lambda: capture_position(mode, "pos1")).grid(row=0, column=2, padx=4, pady=4)

    tk.Label(frame, text="Position 2").grid(row=1, column=0, sticky="w", padx=4, pady=4)
    tk.Label(frame, textvariable=coordinate_vars[mode]["pos2"]).grid(row=1, column=1, sticky="w", padx=4, pady=4)
    tk.Button(frame, text="Capture position 2", command=lambda: capture_position(mode, "pos2")).grid(row=1, column=2, padx=4, pady=4)

    tk.Button(frame, text="Use this mode", command=lambda: use_mode(mode)).grid(row=2, column=0, columnspan=3, sticky="ew", padx=4, pady=8)

    frame.columnconfigure(1, weight=1)


lock = threading.Lock()
config = load_config()
running = False
closing = False
active_mode = "Stationary Troops"

root = tk.Tk()
root.title("Tiny Autoclicker")
root.resizable(False, False)

status_var = tk.StringVar(value="Stopped")
active_mode_var = tk.StringVar(value="Active mode: Stationary Troops")
message_var = tk.StringVar(value="")
coordinate_vars = {}

for mode_name in config:
    coordinate_vars[mode_name] = {
        "pos1": tk.StringVar(),
        "pos2": tk.StringVar(),
    }

update_coordinate_labels()

top_frame = tk.Frame(root, padx=10, pady=10)
top_frame.pack(fill="x")

tk.Button(top_frame, text="Start", width=12, command=lambda: set_running(True)).grid(row=0, column=0, padx=4, pady=4)
tk.Button(top_frame, text="Stop", width=12, command=lambda: set_running(False)).grid(row=0, column=1, padx=4, pady=4)

tk.Label(top_frame, text="Status:").grid(row=1, column=0, sticky="e", padx=4, pady=4)
tk.Label(top_frame, textvariable=status_var).grid(row=1, column=1, sticky="w", padx=4, pady=4)
tk.Label(top_frame, textvariable=active_mode_var).grid(row=2, column=0, columnspan=2, padx=4, pady=4)

create_mode_frame(root, "Stationary Troops")
create_mode_frame(root, "Moving Troops")

tk.Label(root, textvariable=message_var, wraplength=420).pack(fill="x", padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", close_program)

threading.Thread(target=click_loop, daemon=True).start()

root.mainloop()