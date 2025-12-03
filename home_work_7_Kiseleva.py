import tkinter as tk
from datetime import datetime
import os

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        
        # Файл для сохранения истории
        self.history_file = "calculations_history.txt"
        
        # Переменные
        self.current_input = ""
        self.result_var = tk.StringVar()
        
        # Создание интерфейса
        self.create_widgets()
        
    def create_widgets(self):
        # Дисплей калькулятора
        display_frame = tk.Frame(self.root, height=80)
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
        
        display = tk.Entry(display_frame, textvariable=self.result_var, 
                          font=('Arial', 24), justify='right', bd=10, 
                          relief=tk.SUNKEN, bg='lightgray')
        display.pack(fill=tk.BOTH, expand=True)
        
        # Фрейм для кнопок
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Расположение кнопок
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '(', ')', '⌫']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = tk.Button(buttons_frame, text=text, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
                btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                
                # Настройка размера кнопок
                buttons_frame.grid_columnconfigure(j, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        else:
            self.current_input += str(char)
            self.result_var.set(self.current_input)
    
    def calculate(self):
        try:
            # Вычисление результата
            result = eval(self.current_input)
            
            # Форматирование результата
            if isinstance(result, float):
                result = round(result, 10)  # Ограничение десятичных знаков
            
            # Сохранение в файл
            self.save_to_file(self.current_input, result)
            
            # Обновление дисплея
            self.current_input = str(result)
            self.result_var.set(self.current_input)
            
        except ZeroDivisionError:
            self.result_var.set("Ошибка: деление на 0")
            self.save_to_file(self.current_input, "Ошибка: деление на 0")
            self.current_input = ""
        except Exception as e:
            self.result_var.set("Ошибка вычисления")
            self.save_to_file(self.current_input, f"Ошибка: {str(e)}")
            self.current_input = ""
    
    def save_to_file(self, expression, result):
        """Сохранение операции в файл"""
        try:
            # Получение текущей даты и времени
            now = datetime.now()
            timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
            
            # Форматирование записи
            entry = f"{timestamp} {expression} = {result}\n"
            
            # Запись в файл
            with open(self.history_file, 'a', encoding='utf-8') as f:
                f.write(entry)
                
            # Проверка существования файла (создание, если не существует)
            if not os.path.exists(self.history_file):
                print(f"Файл {self.history_file} создан")
                
        except Exception as e:
            print(f"Ошибка при сохранении в файл: {e}")
    
    def clear(self):
        self.current_input = ""
        self.result_var.set("")
    
    def backspace(self):
        self.current_input = self.current_input[:-1]
        self.result_var.set(self.current_input)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()