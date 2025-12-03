import tkinter as tk
from datetime import datetime

HISTORY_FILE = "calculations_history.txt"

def save_history(expression, result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {expression} = {result}\n")


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("Arial", 20),
            width=25,
            borderwidth=5,
            justify="right"
        )
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                buttons_frame,
                text=text,
                width=10,
                height=3,
                font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "=":
            try:
                result = str(eval(self.expression))
                save_history(self.expression, result)
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Ошибка")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
