import tkinter as tk
from datetime import datetime


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Настольный калькулятор")

        self.expression = ""

        self.display = tk.Entry(
            master,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        button_definitions = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in button_definitions:
            button = tk.Button(
                master,
                text=text,
                font=("Arial", 18),
                bd=5,
                relief=tk.RAISED,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(
                row=row,
                column=col,
                padx=5,
                pady=5,
                sticky="nsew"
            )

        for i in range(5):
            master.rowconfigure(i, weight=1)
        for i in range(4):
            master.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.clear()
        elif char == "=":
            self.calculate()
        else:
            self.expression += str(char)
            self.update_display(self.expression)

    def update_display(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, text)

    def calculate(self):
        if not self.expression:
            return
        expr = self.expression
        try:
            result = eval(expr, {"__builtins__": None}, {})
        except ZeroDivisionError:
            result = "Ошибка: деление на 0"
        except Exception:
            result = "Ошибка"
        else:
            self.expression = str(result)
        self.update_display(str(result))
        self.log_calculation(expr, result)

    def clear(self):
        self.expression = ""
        self.update_display("")

    def log_calculation(self, expr, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {expr} = {result}\n"
        with open("calculations_history.txt", "a", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
