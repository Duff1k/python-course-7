import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime


def log_operation(value_on_display, result):
    timestamp = datetime.now().strftime("[%d-%m-%Y %H:%M]")
    entry = f"{timestamp} {value_on_display} = {result}\n"
    with open("calculations_history.txt", "a", encoding="utf-8") as f:
        f.write(entry)


def update_display(value, display):
    global display_value
    display_value = value
    display.config(text=display_value)


def btn_click(btn, display):
    global display_value
    if len(display_value) < MAX_LEN:
        display_value += btn
        update_display(display_value, display)
    else:
        messagebox.showerror("Ошибка", "Превышение максимального количества символов")


def clear_display(display):
    global display_value
    display_value = ""
    update_display(display_value, display)


def calculate(display):
    global display_value
    try:
        value_on_display = display_value
        result = str(eval(value_on_display))
        update_display(result, display)
        log_operation(value_on_display, result)
    except Exception:
        messagebox.showerror("Ошибка", "Что-то пошло не так")
        clear_display(display)


display_value = ""
MAX_LEN = 21

window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x270")
window.resizable(False, False)
window.configure(background="#ffffff")

display = tk.Label(window, text="", font=("Arial", 20), background="#ffffff", fg="#000000")
display.pack(pady=5)

frame_buttons = tk.Frame(window, bg="#E0F0F0")
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="7", command=lambda: btn_click("7", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="8", command=lambda: btn_click("8", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="9", command=lambda: btn_click("9", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_buttons, text="/", command=lambda: btn_click("/", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=0, column=3, padx=5, pady=5)

tk.Button(frame_buttons, text="4", command=lambda: btn_click("4", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="5", command=lambda: btn_click("5", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="6", command=lambda: btn_click("6", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=1, column=2, padx=5, pady=5)
tk.Button(frame_buttons, text="*", command=lambda: btn_click("*", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=1, column=3, padx=5, pady=5)

tk.Button(frame_buttons, text="1", command=lambda: btn_click("1", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="2", command=lambda: btn_click("2", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="3", command=lambda: btn_click("3", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=2, column=2, padx=5, pady=5)
tk.Button(frame_buttons, text="-", command=lambda: btn_click("-", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=2, column=3, padx=5, pady=5)

tk.Button(frame_buttons, text="0", command=lambda: btn_click("0", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="C", command=lambda: clear_display(display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=3, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="=", command=lambda: calculate(display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=3, column=2, padx=5, pady=5)
tk.Button(frame_buttons, text="+", command=lambda: btn_click("+", display), font=("Arial", 16), bg="#FFFFFF", width=5).grid(row=3, column=3, padx=5, pady=5)

window.mainloop()
