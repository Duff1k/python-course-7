import tkinter as tk
import datetime

def add_digit(digit):
    global current_input
    current_input += str(digit)
    display_var.set(current_input)

def add_operation(operation):
    global current_input
    current_input += operation
    display_var.set(current_input)

def calculate():
    global current_input
    try:
        result = eval(current_input)
        save_calculation(current_input, result)
        display_var.set(result)
        current_input = str(result)
    except:
        display_var.set("Error")
        current_input = ""

def save_calculation(expression, result):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    operation = f"{timestamp} {expression} = {result}\n"

    with open("calculations_history.txt", "a", encoding="utf-8") as f:
        f.write(operation)


def add_decimal():
    global current_input
    current_input += "."
    display_var.set(current_input)

def change_sign():
    global current_input
    if current_input:
        if current_input.startswith("-"):
            current_input = current_input[1:]
        else:
            current_input = "-" + current_input
        display_var.set(current_input)

def percentage():
    global current_input
    try:
        if current_input:
            result = eval(current_input)
            percent = result / 100
            display_var.set(percent)
            current_input = str(percent)
    except Exception as e:
        display_var.set("Error")
        current_input = ""

def clear_all():
    global current_input
    current_input = ""
    display_var.set("")

def clear_entry():
    global current_input
    if current_input:
        current_input = current_input[:-1]
        display_var.set(current_input)


window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")
window.configure(background="#96e1f2")

current_input = ""
display_var = tk.StringVar()

display = tk.Entry(window, font=("Arial", 15), width=15, justify='right', bd=5, textvariable=display_var, state='readonly')
display.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

tk.Button(button_frame, text="7", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(7)).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="8", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(8)).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="9", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(9)).grid(row=0, column=2, padx=5, pady=5)

tk.Button(button_frame, text="4", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(4)).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="5", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(5)).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="6", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(6)).grid(row=1, column=2, padx=5, pady=5)

tk.Button(button_frame, text="1", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(1)).grid(row=2, column=0, padx=5, pady=5)
tk.Button(button_frame, text="2", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(2)).grid(row=2, column=1, padx=5, pady=5)
tk.Button(button_frame, text="3", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(3)).grid(row=2, column=2, padx=5, pady=5)

tk.Button(button_frame, text="0", font=("Arial", 15), bg="#c0effa", width=5, command=lambda: add_digit(0)).grid(row=3, column=0, padx=5, pady=5)
tk.Button(button_frame, text=".", font=("Arial", 15), bg="#60cce6", width=5, command=add_decimal).grid(row=3, column=1, padx=5, pady=5)
tk.Button(button_frame, text="=", font=("Arial", 15), bg="#60cce6", width=5, command=calculate).grid(row=3, column=2, padx=5, pady=5)

tk.Button(button_frame, text="+", font=("Arial", 15), bg="#60cce6", width=5, command=lambda: add_operation("+")).grid(row=0, column=3, padx=5, pady=5)
tk.Button(button_frame, text="-", font=("Arial", 15), bg="#60cce6", width=5, command=lambda: add_operation("-")).grid(row=1, column=3, padx=5, pady=5)
tk.Button(button_frame, text="*", font=("Arial", 15), bg="#60cce6", width=5, command=lambda: add_operation("*")).grid(row=2, column=3, padx=5, pady=5)
tk.Button(button_frame, text="/", font=("Arial", 15), bg="#60cce6", width=5, command=lambda: add_operation("/")).grid(row=3, column=3, padx=5, pady=5)  # ТОЛЬКО ОДИН РАЗ!

tk.Button(button_frame, text="C", font=("Arial", 15), bg="#60cce6", width=5, command=clear_all).grid(row=4, column=0, padx=5, pady=5)
tk.Button(button_frame, text="⌫", font=("Arial", 15), bg="#60cce6", width=5, command=clear_entry).grid(row=4, column=1, padx=5, pady=5)
tk.Button(button_frame, text="±", font=("Arial", 15), bg="#60cce6", width=5, command=change_sign).grid(row=4, column=2, padx=5, pady=5)
tk.Button(button_frame, text="%", font=("Arial", 15), bg="#60cce6", width=5, command=percentage).grid(row=4, column=3, padx=5, pady=5)


window.mainloop()