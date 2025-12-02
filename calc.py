import tkinter as tk
from datetime import datetime


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор - Домашнее задание 7")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        self.expression = ""
        self.history_file = "calculations_history.txt"

        self._setup_ui()

    def _setup_ui(self):
        # Дисплей
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 20),
            justify="right",
            bd=5,
            relief=tk.SUNKEN,
            state="readonly"
        )
        display.pack(fill=tk.X, padx=10, pady=(15, 10), ipady=10)

        # Фрейм для кнопок
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

        # Кнопки
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 2)
        ]

        for btn_data in buttons:
            if len(btn_data) == 4:
                text, row, col, colspan = btn_data
            else:
                text, row, col = btn_data
                colspan = 1

            # Определяем цвет кнопки
            if text in '0123456789':
                bg_color = '#f0f0f0'
            elif text in '+-*/.':
                bg_color = '#ff9800'
            elif text == '=':
                bg_color = '#4caf50'
            elif text == 'C':
                bg_color = '#f44336'

            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 14),
                bg=bg_color,
                fg="black",
                command=lambda t=text: self._on_button_click(t)
            )

            if colspan > 1:
                btn.grid(row=row, column=col, columnspan=colspan,
                         sticky="nsew", padx=2, pady=2)
            else:
                btn.grid(row=row, column=col,
                         sticky="nsew", padx=2, pady=2)

        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def _on_button_click(self, value):
        if value == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif value == '=':
            self._calculate()
        else:
            if self.display_var.get() == "0" and value not in '+-*/.':
                self.expression = value
                self.display_var.set(value)
            else:
                self.expression += value
                self.display_var.set(self.expression)

    def _calculate(self):
        if not self.expression:
            return

        try:
            result = eval(self.expression)
            self._save_to_history(self.expression, result)
            if isinstance(result, float):
                result_str = str(result)
            else:
                result_str = str(result)

            self.display_var.set(result_str)
            self.expression = result_str

        except ZeroDivisionError:
            self.display_var.set("Ошибка: деление на 0")
            self.expression = ""
        except Exception:
            self.display_var.set("Ошибка")
            self.expression = ""

    def _save_to_history(self, expression, result):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            record = f"[{timestamp}] {expression} = {result}\n"

            with open(self.history_file, 'a', encoding='utf-8') as f:
                f.write(record)

        except Exception as e:
            print(f"Ошибка при сохранении: {e}")


def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()