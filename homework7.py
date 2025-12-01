import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

current_expression = ""
history_file = "calculations_history.txt"

# Создаем файл истории при запуске, если его нет
if not os.path.exists(history_file):
    with open(history_file, "w", encoding="utf-8") as f:
        f.write("История вычислений:\n")


def button_click(value):
    global current_expression
    current_expression += str(value)
    display_var.set(current_expression)


def clear_display():
    global current_expression
    current_expression = ""
    display_var.set(current_expression)


def calculate():
    global current_expression
    if not current_expression:
        return

    try:
        # Проверка на двойные операторы
        if any(op + op in current_expression for op in '+-*/'):
            messagebox.showerror("Ошибка", "Некорректное выражение!")
            return

        result = eval(current_expression)
        save_calculation(current_expression, result)
        current_expression = str(result)
        display_var.set(current_expression)

    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
        clear_display()
    except Exception as e:
        messagebox.showerror("Ошибка", "Некорректное выражение!")
        clear_display()


def save_calculation(expression, result):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(history_file, "a", encoding="utf-8") as f:
            f.write(f"[{current_time}] {expression} = {result}\n")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить в файл: {e}")


def show_history():
    try:
        with open(history_file, "r", encoding="utf-8") as f:
            history_content = f.read()

        history_window = tk.Toplevel(window)
        history_window.title("История вычислений")
        history_window.geometry("500x400")

        # Текстовое поле с полосой прокрутки
        text_frame = tk.Frame(history_window)
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        text_widget = tk.Text(text_frame, font=("Consolas", 10), wrap="word")
        scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)

        text_widget.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        text_widget.config(yscrollcommand=scrollbar.set)
        text_widget.insert("1.0", history_content)
        text_widget.config(state="disabled")  # Только для чтения

        # Кнопка закрытия
        close_btn = tk.Button(history_window, text="Закрыть", font=("Arial", 12),
                              command=history_window.destroy, bg="lightgray")
        close_btn.pack(pady=5)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть историю: {e}")


def on_key_press(event):
    """Обработка нажатий клавиш"""
    key = event.char

    if key in '0123456789':
        button_click(key)
    elif key in '+-*/.':
        button_click(key)
    elif key == '\r' or key == '=':  # Enter или =
        calculate()
    elif key == '\x08' or key == '\x7f':  # Backspace или Delete
        clear_display()
    elif key == 'c' or key == 'C':  # Очистка
        clear_display()


# Создание главного окна
window = tk.Tk()
window.title("Калькулятор с историей")
window.geometry("500x550")
window.configure(background="#3136d4")

# Привязка обработчика клавиш
window.bind('<Key>', on_key_press)

# Дисплей
display_var = tk.StringVar()
display = tk.Entry(
    window,
    textvariable=display_var,
    font=("Arial", 20, "bold"),
    justify="right",
    state="readonly",
    width=20,
    bg="white",
    fg="black",
    bd=5,
    relief="ridge"
)
display.pack(pady=20)

# Фрейм для кнопок
frame_buttons = tk.Frame(window, bg="#3136d4")
frame_buttons.pack(pady=10)

# Определение кнопок с правильной сеткой
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
    ('C', 4, 0, 3)  # Кнопка C занимает 3 колонки в 4-м ряду
]

button_colors = {
    'numbers': '#E6F3FF',  # Светло-голубой для цифр
    'operators': '#87CEEB',  # Небесно-голубой для операторов
    'clear': '#FF6B6B',  # Красный для очистки
    'equals': '#98FB98'  # Светло-зеленый для равно
}

# Создание кнопок
for button in buttons:
    if len(button) == 3:
        text, row, col = button
        colspan = 1
    else:
        text, row, col, colspan = button

    # Определение цвета и команды
    if text in '0123456789':
        bg_color = button_colors['numbers']
        command = lambda x=text: button_click(x)
    elif text in '+-*/.':
        bg_color = button_colors['operators']
        command = lambda x=text: button_click(x)
    elif text == '=':
        bg_color = button_colors['equals']
        command = calculate
    elif text == 'C':
        bg_color = button_colors['clear']
        command = clear_display

    # Создание кнопки
    btn = tk.Button(
        frame_buttons,
        text=text,
        font=("Arial", 14, "bold"),
        command=command,
        bg=bg_color,
        fg="black" if text != 'C' else "white",
        width=8 if colspan == 1 else 24,  # Ширина для кнопки C
        height=2,
        relief="raised",
        bd=3
    )

    if colspan > 1:
        btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="ew")
    else:
        btn.grid(row=row, column=col, padx=2, pady=2)

# Кнопка просмотра истории
history_btn = tk.Button(
    window,
    text="📜 Показать историю",
    font=("Arial", 12, "bold"),
    command=show_history,
    bg="#FFD700",  # Золотой цвет
    fg="black",
    width=20,
    height=2,
    relief="raised",
    bd=3
)
history_btn.pack(pady=10)

# Информационная метка
info_label = tk.Label(
    window,
    text="Можно использовать клавиатуру: цифры, +-*/.=, C - очистка",
    font=("Arial", 9),
    bg="#3136d4",
    fg="white"
)
info_label.pack(pady=5)

window.mainloop()