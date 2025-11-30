import tkinter as tk
from datetime import datetime
import os

# Файл истории
HISTORY_FILE = "calculations_history.txt"

def log_calculation(expression, result):
    """Сохраняет вычисление в файл с текущей датой и временем."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {expression} = {result}\n"
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def on_button_click(char):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(char))

def on_clear():
    display.delete(0, tk.END)

def on_equals():
    try:
        expression = display.get()
        # Безопасное вычисление (только арифметика)
        # Убираем всё, кроме цифр, точек и операторов
        allowed = "0123456789+-*/. ()"
        if not all(c in allowed for c in expression):
            raise ValueError("Недопустимые символы")
        result = eval(expression)  # ⚠️ Используем осторожно (только в доверенной среде)
        display.delete(0, tk.END)
        display.insert(0, str(result))
        log_calculation(expression, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Ошибка")
        # Не сохраняем ошибки в историю

# Создаём окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)

# Дисплей
display = tk.Entry(root, font=("Arial", 16), justify="right", bd=10, insertwidth=2)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Кнопки
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, font=("Arial", 14), command=on_clear)
    elif text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 14), command=on_equals)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14),
                        command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Настройка растягивания сетки
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Запуск
root.mainloop()
