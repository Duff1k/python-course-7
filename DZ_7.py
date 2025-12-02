import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""
        self.history_file = "calculations_history.txt"

        self._create_history_file()
        self._setup_ui()

    def _create_history_file(self):
        if not os.path.exists(self.history_file):
            with open(self.history_file, 'w', encoding='utf-8') as f:
                f.write("")

    def _setup_ui(self):

        # ДИСПЛЕЙ
        self.display = tk.Entry(
            self.root,
            font=("Arial", 20),
            justify=tk.RIGHT,
            bd=2
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)
        self.display.insert(0, "0")

        # КНОПКИ
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Расположение кнопок: цифры и операции
        buttons_layout = [
            [("7", "#34495e"), ("8", "#34495e"), ("9", "#34495e"), ("/", "#3498db")],
            [("4", "#34495e"), ("5", "#34495e"), ("6", "#34495e"), ("*", "#3498db")],
            [("1", "#34495e"), ("2", "#34495e"), ("3", "#34495e"), ("-", "#3498db")],
            [("0", "#34495e"), (".", "#34495e"), ("=", "#27ae60"), ("+", "#3498db")],
            [("C", "#e74c3c")],
        ]

        for row_idx, row in enumerate(buttons_layout):
            for col_idx, (text, color) in enumerate(row):
                self._create_button(buttons_frame, text, color, row_idx, col_idx)

    def _create_button(self, parent, text, color, row, col):
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white",
            command=lambda: self._on_button_click(text)
        )
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5, ipady=20)
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)

    def _on_button_click(self, char):
        try:
            if char == "C":
                self.expression = ""
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")

            elif char == "=":
                self._calculate()

            else:
                self._add_character(char)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def _add_character(self, char):
        current = self.display.get()

        if current == "0" and char not in [".", "0"]:
            self.expression = ""
            self.display.delete(0, tk.END)
        elif current == "0" and char == "0":
            return

        # Проверка на две точки подряд
        if char == ".":
            last_number = self.expression.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
            if "." in last_number:
                return

        self.expression += char
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def _calculate(self):
        try:
            expression = self.display.get()

            if not expression or expression == "0":
                messagebox.showwarning("Внимание", "Введите выражение")
                return

            if expression[-1] in ["+", "-", "*", "/"]:
                messagebox.showerror("Ошибка", "Неверное выражение")
                return

            # Вычисляем
            result = eval(expression)

            if isinstance(result, float) and result == int(result):
                result = int(result)

            # СОХРАНЯЕМ В ИСТОРИЮ
            self._save_to_history(expression, result)

            # Выводим результат
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)

        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            self._reset()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка вычисления: {str(e)}")
            self._reset()

    def _reset(self):
        self.expression = ""
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

    def _save_to_history(self, expression, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"[{timestamp}] {expression} = {result}\n"

        try:
            with open(self.history_file, 'a', encoding='utf-8') as f:
                f.write(record)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить: {str(e)}")


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()