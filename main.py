import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор с историей")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Инициализация истории
        self.history_file = "calculations_history.txt"
        self.initialize_history_file()

        # Строка ввода
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=('Arial', 24),
            bd=10,
            relief=tk.RIDGE,
            justify=tk.RIGHT,
            state='readonly'
        )
        self.display.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Фрейм для кнопок
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Кнопки
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0, 2), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 4)  # Кнопка очистки занимает 4 колонки
        ]

        # Создание кнопок
        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1

            if text == '=':
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg='#4CAF50',
                    fg='white',
                    command=self.calculate
                )
            elif text == 'C':
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg='#f44336',
                    fg='white',
                    command=self.clear_display
                )
            else:
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=('Arial', 18),
                    bg='#f0f0f0',
                    command=lambda t=text: self.add_to_display(t)
                )

            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky='nsew',
                padx=5,
                pady=5,
                ipadx=10,
                ipady=10
            )

        # Настройка веса строк и столбцов
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def initialize_history_file(self):
        """Инициализация файла истории, если он не существует"""
        if not os.path.exists(self.history_file):
            with open(self.history_file, 'w', encoding='utf-8') as f:
                f.write("История вычислений калькулятора\n")
                f.write("=" * 40 + "\n")

    def add_to_display(self, char):
        """Добавление символа на дисплей"""
        current_text = self.display_var.get()
        new_text = current_text + str(char)
        self.display_var.set(new_text)

    def clear_display(self):
        """Очистка дисплея"""
        self.display_var.set("")

    def calculate(self):
        """Вычисление выражения и сохранение в файл"""
        expression = self.display_var.get()

        if not expression:
            return

        try:
            # Вычисление результата
            result = eval(expression)

            # Получение текущей даты и времени
            now = datetime.now()
            timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")

            # Формирование строки для записи
            history_entry = f"{timestamp} {expression} = {result}\n"

            # Запись в файл
            with open(self.history_file, 'a', encoding='utf-8') as f:
                f.write(history_entry)

            # Вывод результата
            self.display_var.set(str(result))

        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
            self.save_error_to_history(expression, "Ошибка: деление на ноль")
            self.display_var.set("Ошибка")
        except SyntaxError:
            messagebox.showerror("Ошибка", "Некорректное выражение!")
            self.save_error_to_history(expression, "Ошибка: некорректное выражение")
            self.display_var.set("Ошибка")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
            self.save_error_to_history(expression, f"Ошибка: {str(e)}")
            self.display_var.set("Ошибка")

    def save_error_to_history(self, expression, error_msg):
        """Сохранение ошибки в историю"""
        now = datetime.now()
        timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
        history_entry = f"{timestamp} {expression} = {error_msg}\n"

        with open(self.history_file, 'a', encoding='utf-8') as f:
            f.write(history_entry)


def main():
    root = tk.Tk()
    app = Calculator(root)

    # Добавляем горячие клавиши
    root.bind('<Return>', lambda event: app.calculate())
    root.bind('<Escape>', lambda event: app.clear_display())
    root.bind('<BackSpace>', lambda event: app.display_var.set(app.display_var.get()[:-1]))

    # Добавляем цифры с клавиатуры
    for num in range(10):
        root.bind(str(num), lambda event, n=num: app.add_to_display(n))

    root.mainloop()


if __name__ == "__main__":
    main()