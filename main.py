import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime

listener = False

def operation_saver(text):
    with open("calculations_history.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def add_value(value):
    current_op = operationLabel.get()
    if "=" in current_op:
        clear_all()

    enterLabel.configure(state="normal")
    current = enterLabel.get()
    if current == "0":
        current = ""
    enterLabel.delete(0, 'end')
    global listener
    if listener:
        enterLabel.insert(0, value)
        listener = False
    else:
        enterLabel.insert(0, current + value)
    enterLabel.configure(state="disabled", disabledbackground="#1c1b1b")

def add_signature(value):
    current = enterLabel.get()
    if current == "":
        return
    operationLabel.configure(state="normal")
    current_op = operationLabel.get()
    global listener
    if "=" in current_op:
        operationLabel.delete(0, 'end')
        operationLabel.insert(0, current + ' ' + value)
        listener = True
    elif current == current_op[:-2] or current_op == "":
        operationLabel.delete(0, 'end')
        operationLabel.insert(0, current +  ' ' + value)
        listener = True

    operationLabel.configure(state="disabled", disabledbackground="#1c1b1b")

def do_operation():
    current = enterLabel.get()
    current_op = operationLabel.get()
    if current_op == "":
        return

    enterLabel.configure(state="normal")
    enterLabel.delete(0, 'end')
    operationLabel.configure(state="normal")
    operationLabel.delete(0, 'end')

    enter_val = ""
    operation_val = ""

    if "=" in current_op:
        sub_vals = current_op.split(" ")
        current_op = current + " " + sub_vals[1]
        current = sub_vals[2]

    if "÷" in current_op and current != "0":
        if "." in current_op:
            enter_val = str(float(current_op[:-2]) / int(current))
        else:
            enter_val = str(int(current_op[:-2]) / int(current))
        if enter_val[-2:] == ".0":
            enter_val = enter_val[:-2]
        operation_val = current_op + " " + current + " ="
    elif "÷" in current_op and current == "0":
        enter_val = "Нельзя делить на 0."
        operation_val = ""
    elif "×" in current_op:
        if "." in current_op:
            enter_val = str(float(current_op[:-2]) * int(current))
        else:
            enter_val = str(int(current_op[:-2]) * int(current))
        if enter_val[-2:] == ".0":
            enter_val = enter_val[:-2]
        operation_val = current_op + " " + current + " ="
    elif "-" in current_op:
        if "." in current_op:
            enter_val = str(float(current_op[:-2]) - int(current))
        else:
            enter_val = str(int(current_op[:-2]) - int(current))
        if enter_val[-2:] == ".0":
            enter_val = enter_val[:-2]
        operation_val = current_op + " " + current + " ="
    elif "+" in current_op:
        if "." in current_op:
            enter_val = str(float(current_op[:-2]) + int(current))
        else:
            enter_val = str(int(current_op[:-2]) + int(current))
        if enter_val[-2:] == ".0":
            enter_val = enter_val[:-2]
        operation_val = current_op + " " + current + " ="

    operation_saver(str(datetime.now()) + " " + operation_val + " " + enter_val)
    operationLabel.insert(0, operation_val)
    enterLabel.insert(0, enter_val)
    enterLabel.configure(state="disabled", disabledbackground="#1c1b1b")
    operationLabel.configure(state="disabled", disabledbackground="#1c1b1b")

def clear():
    enterLabel.configure(state="normal")
    enterLabel.delete(0, 'end')
    enterLabel.insert(0, "0")
    enterLabel.configure(state="disabled", disabledbackground="#1c1b1b")

def clear_all():
    enterLabel.configure(state="normal")
    enterLabel.delete(0, 'end')
    enterLabel.insert(0, "0")
    enterLabel.configure(state="disabled", disabledbackground="#1c1b1b")
    operationLabel.configure(state="normal")
    operationLabel.delete(0, 'end')
    operationLabel.configure(state="disabled", disabledbackground="#1c1b1b")

def delete_last():
    current = enterLabel.get()
    enterLabel.configure(state="normal")
    enterLabel.delete(0, 'end')
    if len(current) > 1:
        enterLabel.insert(0, current[:-1])
    elif len(current) == 1:
        enterLabel.insert(0, "0")
    enterLabel.configure(state="disabled", disabledbackground="#1c1b1b")

#Основная форма
window = tk.Tk()
window.title("Калькулятор")
window.geometry("320x410")
window.configure(background="#1c1b1b")

#Поле операции + поле ввода
operationLabel = tk.Entry(window, font=('Arial', 14), width=300, justify='right', disabledforeground="#ffffff", disabledbackground="#1c1b1b", border="0", background="#1c1b1b", state="disabled")
operationLabel.pack(pady=(10,0), padx=10, anchor="w")
enterLabel = tk.Entry(window, font=('Arial', 24), width=300, justify='right', disabledforeground="#ffffff", disabledbackground="#1c1b1b", border="0", background="#1c1b1b")
enterLabel.insert(0, "0")
enterLabel.configure(state="disabled")
enterLabel.pack(pady=(0,10), padx=10 , anchor="w")



#Поле с кнопками
frame_buttons = tk.Frame(window, background="#1c1b1b")
frame_buttons.pack(pady=5)
tk.Button(frame_buttons, text = "CE", command=clear, font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=0, column=0, padx=1, pady=1)
tk.Button(frame_buttons, text = "C", command=clear_all, font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=0, column=1, padx=1, pady=1)
tk.Button(frame_buttons, text = "<=", command=delete_last, font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=0, column=2, padx=1, pady=1)
tk.Button(frame_buttons, text = "÷", command=lambda v="÷": add_signature(v), font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=0, column=3, padx=1, pady=1)
tk.Button(frame_buttons, text = "7", command=lambda v="7": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=1, column=0, padx=1, pady=1)
tk.Button(frame_buttons, text = "8", command=lambda v="8": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=1, column=1, padx=1, pady=1)
tk.Button(frame_buttons, text = "9", command=lambda v="9": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=1, column=2, padx=1, pady=1)
tk.Button(frame_buttons, text = "×", command=lambda v="×": add_signature(v), font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=1, column=3, padx=1, pady=1)
tk.Button(frame_buttons, text = "4", command=lambda v="4": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=2, column=0, padx=1, pady=1)
tk.Button(frame_buttons, text = "5", command=lambda v="5": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=2, column=1, padx=1, pady=1)
tk.Button(frame_buttons, text = "6", command=lambda v="6": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=2, column=2, padx=1, pady=1)
tk.Button(frame_buttons, text = "-", command=lambda v="-": add_signature(v), font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=2, column=3, padx=1, pady=1)
tk.Button(frame_buttons, text = "1", command=lambda v="1": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=3, column=0, padx=1, pady=1)
tk.Button(frame_buttons, text = "2", command=lambda v="2": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=3, column=1, padx=1, pady=1)
tk.Button(frame_buttons, text = "3", command=lambda v="3": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=3, column=2, padx=1, pady=1)
tk.Button(frame_buttons, text = "+", command=lambda v="+": add_signature(v), font=("Arial", 14),foreground="#ffffff", bg="#343434", width=6, height=2).grid(row=3, column=3, padx=1, pady=1)
tk.Button(frame_buttons, text = "", font=("Arial", 14),disabledforeground="#ffffff", state="disabled", bg="#343434", width=6, height=2).grid(row=4, column=0, padx=1, pady=1)
tk.Button(frame_buttons, text = "0", command=lambda v="0": add_value(v), font=("Arial", 14),foreground="#ffffff", bg="#544e4e", width=6, height=2).grid(row=4, column=1, padx=1, pady=1)
tk.Button(frame_buttons, text = "=", command=do_operation, font=("Arial", 14),foreground="#ffffff", bg="#b53636", width=13, height=2).grid(row=4, column=2, columnspan=2, padx=1, pady=1)

window.mainloop()