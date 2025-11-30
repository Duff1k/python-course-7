import tkinter as tk
from tkinter import messagebox
from datetime import datetime

current_expression = ""
history_file = "calculations_history.txt"


def button_click(value):
    global current_expression
    current_expression += str(value)
    display_var.set(current_expression)


def clear_display():
    global current_expression
    current_expression = ""
    display_var.set(current_expression)


def calculate():
    global current_expression
    try:
        result = eval(current_expression)
        save_calculation(current_expression, result)
        current_expression = str(result)
        display_var.set(current_expression)

    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
        display_var.set(current_expression)
    except Exception as e:
        messagebox.showerror("Ошибка", "Некорректное выражение!")
        clear_display()


def save_calculation(expression, result):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(history_file, "a") as f:
            f.write(f"[{current_time}] {expression} = {result}\n")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить в файл: {e}")


window = tk.Tk()
window.title("Калькулятор")
window.geometry("500x500")
window.configure(background="#3136d4")

display_var = tk.StringVar()
display = tk.Entry(
    window,
    textvariable=display_var,
    font=("Arial", 15),
    justify="right",
    state="readonly",
    width=18,
    bg="white"
)
display.pack(pady=20)

frame_buttons = tk.Frame(window, bg="#3136d4")
frame_buttons.pack(pady=10)

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
    ('C', 3, 4)]

button_colors = {
    'numbers': 'lightblue1',
    'operators': 'sky blue',
    'clear': 'red',
    'equals': 'green yellow'
}

for text, row, col in buttons:
    if text in '0123456789':
        bg_color = button_colors['numbers']
        command = lambda x=text: button_click(x)
    elif text in '+-*/.':
        bg_color = button_colors['operators']
        command = lambda x=text: button_click(x)
    elif text == '=':
        bg_color = button_colors['equals']
        command = calculate
    elif text == 'C':
        bg_color = button_colors['clear']
        command = clear_display

    tk.Button(
        frame_buttons,
        text=text,
        font=("Arial", 15),
        command=command,
        bg=bg_color,
        width=5,
        height=2
    ).grid(row=row, column=col, padx=2, pady=2)

window.mainloop()
