import tkinter as tk
from datetime import datetime
 
# Функция записи в файл
def save_to_file(expression, result):
    with open("calculations_history.txt", "a", encoding="utf-8") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time_now}] {expression} = {result}\n")
 
# Функция нажатия кнопок
def press(value):
    display.insert(tk.END, value)
 
# Функция вычисления
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        save_to_file(expression, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Ошибка")
 
# Очистка дисплея
def clear():
    display.delete(0, tk.END)
 
# Окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)
 
# Дисплей
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)
 
# Кнопки
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]
 
frame = tk.Frame(root)
frame.pack()
 
row = 0
col = 0
 
for btn in buttons:
    if btn == "=":
        action = calculate
    elif btn == "C":
        action = clear
    else:
        action = lambda x=btn: press(x)
 
    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 16),
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)
 
    col += 1
    if col > 3:
        col = 0
        row += 1
 
root.mainloop()