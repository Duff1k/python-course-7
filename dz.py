import tkinter as tk
from tkinter import messagebox
from datetime import datetime

HISTORY_FILE = "calculations_history.txt"

def log_calculation(expr, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {expr} = {result}\n"
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception as e:
        print(f"Ошибка записи: {e}")

# === ОСНОВНОЕ ОКНО ===
window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x500")
window.configure(background="#3136d4")

# === ДИСПЛЕЙ ===
tk.Label(window, text="Калькулятор:", font=("Arial", 20), bg="#3136d4", fg="#FFFFFF").pack(pady=5)
entry_display = tk.Entry(window, font=("Arial", 30), width=20, justify="right")
entry_display.pack(pady=5)

# === ИСТОРИЯ ОПЕРАЦИЙ ===
tk.Label(window, text="История:", font=("Arial", 15), bg="#3136d4", fg="#FFFFFF").pack()
listbox_history = tk.Listbox(window, width=45, height=5, font=("Arial", 12))
listbox_history.pack(pady=5)

# === КНОПКИ ===
frame_buttons = tk.Frame(window, bg="#3136d4")
frame_buttons.pack(pady=10)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

def on_button_click(value):
    current = entry_display.get()
    if value == "C":
        entry_display.delete(0, tk.END)
        return
    if value == "=":
        expr = current
        try:
            result = str(eval(expr))
            entry_display.delete(0, tk.END)
            entry_display.insert(0, result)

            log_calculation(expr, result)
            listbox_history.insert(0, f"{expr} = {result}")
        except:
            entry_display.delete(0, tk.END)
            entry_display.insert(0, "Ошибка")
        return
    entry_display.insert(tk.END, value)

for (text, row, col) in buttons:
    tk.Button(frame_buttons, text=text, font=("Arial", 14), bg="lightblue",
              width=5, height=2, command=lambda v=text: on_button_click(v)).grid(row=row, column=col, padx=2, pady=2)

tk.Button(frame_buttons, text="C", font=("Arial", 14), bg="tomato", width=35, height=2,
          command=lambda: on_button_click("C")).grid(row=4, column=0, columnspan=4, pady=10)

window.mainloop()
