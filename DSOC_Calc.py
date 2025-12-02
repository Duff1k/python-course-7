import tkinter as tk
from datetime import datetime

HISTORY_FILE = "calculations_history.txt"


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор — ДЗ №7")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # === ДИСПЛЕЙ ===
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.RIDGE
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # === КНОПКИ ===
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (text, row, col) in buttons:
            tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                command=lambda v=text: self.on_button_click(v)
            ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Расширение сетки
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    # === ОБРАБОТЧИКИ КНОПОК ===
    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display()
            return

        if value == "=":
            self.calculate()
            return

        # добавление символа
        self.expression += value
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    # === ВЫЧИСЛЕНИЕ ===
    def calculate(self):
        try:
            result = str(eval(self.expression))
        except Exception:
            result = "Ошибка"

        # Запись в файл И ВСЕГДА
        self.log_to_file(self.expression, result)

        # обновление
        self.expression = result
        self.update_display()

    # === ЛОГИРОВАНИЕ ===
    def log_to_file(self, expr, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {expr} = {result}\n"

        try:
            with open(HISTORY_FILE, "a", encoding="utf-8") as f:
                f.write(line)
        except Exception as e:
            print(f"Ошибка записи в файл: {e}")


# === ЗАПУСК ПРИЛОЖЕНИЯ ===
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
