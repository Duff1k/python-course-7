import tkinter as tk
from tkinter import messagebox
from datetime import datetime

result_shown = False

# Запись в файл
def save_to_file(expression, result):
    with open("calculations_history.txt", "a") as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"[{timestamp}] {expression} = {result}\n")

#Калькулятор
def evaluate_expression(event=None):
    global result_shown
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        save_to_file(expression, result)
        result_shown = True
    except:
        messagebox.showerror("Ошибка", "Невозможное арифметическое действие")

# Очистка
def clear(event=None):
    global result_shown
    entry.delete(0, tk.END)
    result_shown = False

#Ввод символов
def button_click(symbol):
    global result_shown

    if result_shown:
        if symbol.isdigit():
            entry.delete(0, tk.END)
        result_shown = False

    entry.insert(tk.END, symbol)

#Обработка клавиатуры
def keypress(event):
    key = event.keysym

    if key in "0123456789":
        button_click(key)

    elif key in ("plus", "KP_Add"):
        button_click("+")
    elif key in ("minus", "KP_Subtract"):
        button_click("-")
    elif key in ("asterisk", "KP_Multiply"):
        button_click("*")
    elif key in ("slash", "KP_Divide"):
        button_click("/")

    elif key in ("Return", "KP_Enter"):
        evaluate_expression()

    elif key == "BackSpace":
        entry.delete(len(entry.get())-1, tk.END)

    elif key == "Escape":
        clear()

#Эффекты нажатия кнопок
def on_enter(event):
    event.widget["bg"] = "#F58888"   # подсветка при наведении на кнопку

def on_leave(event):
    event.widget["bg"] = "black"     # восстановление цвета кнопки

def on_press(event):
    event.widget["bg"] = "#1E1E1E"    # эффект нажатия кнопки

def on_release(event):
    event.widget["bg"] = "#444444"   # возврат после клика


# Окно
root = tk.Tk()
root.title("Калькулятор для домашней работы")
root.configure(bg="white")

root.bind("<Key>", keypress)

# Поле ввода
entry = tk.Entry(root, width=20, font=('Arial', 44), borderwidth=3,
                 relief="solid", justify="right", fg="silver", bg="#238")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 4, 0)
]

# Создание кнопок
for (text, row, col) in buttons:
    if text == '=':
        command = evaluate_expression
    elif text == 'C':
        command = clear
    else:
        command = lambda t=text: button_click(t)

    btn = tk.Button(root, text=text, width=5, height=2,
                    font=('Arial', 32), fg="silver", bg="black",
                    relief="raised", bd=8, command=command)

    # Hover + нажатие
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<ButtonPress-1>", on_press)
    btn.bind("<ButtonRelease-1>", on_release)

    btn.grid(row=row, column=col, padx=3, pady=3)

root.mainloop()