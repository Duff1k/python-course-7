import tkinter as tk
from datetime import datetime

def button_click(number):
    current = display.get()
    if current == "Ошибка":
        display.delete(0, tk.END)
        current = ""
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)

        with open("calculations_history.txt", "a", encoding="utf-8") as file:
            file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {expression} = {result}\n")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Ошибка")

# Создание главного окна
window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x400")
window.configure(bg="#ddeeff")

display = tk.Entry(window, font=("Arial", 20), justify="right", bg="white")
display.pack(pady=10, padx=10, fill="x")

button_frame = tk.Frame(window, bg="#d8c2ff")
button_frame.pack(padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 0
col = 0
for button in buttons:
    if button == "=":
        tk.Button(button_frame, text=button, command=button_equal, font=("Arial", 15),
                  width=5, height=2, bg="#ffcbbb").grid(row=row, column=col, padx=2, pady=2)
    elif button == "C":
        tk.Button(button_frame, text=button, command=button_clear, font=("Arial", 15),
                  width=5, height=2, bg="#ffcbbb").grid(row=row, column=col, padx=2, pady=2)
    else:
        tk.Button(button_frame, text=button, command=lambda b=button: button_click(b), font=("Arial", 15),
                  width=5, height=2, bg="#ffcbbb").grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
