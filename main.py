import tkinter as tk
from datetime import datetime

HISTORY_FILE = 'calculations_history.txt'

def save_to_history(expression, result):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] {expression} = {result}\n"
    with open (HISTORY_FILE, 'a', encoding="utf-8") as f:
        f.write(line)

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.resizable(False,False)

        self.expression = ''

        self.bg_color = "#1e1e2e"
        self.display_bg = "#2e2e3e"
        self.display_fg = "#ffffff"
        self.btn_bg = "#3b3b4f"
        self.btn_fg = "#ffffff"
        self.btn_op_bg = "#5a5aa8"
        self.btn_eq_bg = "#3ba55d"
        self.btn_c_bg = "#a83b3b"
        self.root.configure(background = self.bg_color)

        self.display_var = tk.StringVar()
        display = tk.Entry(
            root,
            textvariable = self.display_var,
            font = ('Consolas, 20'),
            bd = 0,
            bg = self.display_bg,
            fg = self.display_fg,
            justify = 'right',
            insertbackground = self.display_fg
        )
        display.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5, ipady = 15, sticky = 'nsew')
        for i in range(4):
            root.grid_columnconfigure(i, weight = 1)
        for i in range(4):
            root.grid_rowconfigure(i, weight = 1)

        btn_config = {'font': ('Consolas, 16'), 'bd': 0, 'relief': 'flat', 'width': 4, 'height': 2}
        buttons = [
            ("7", 1, 0, self.btn_bg, self.add_char),
            ("8", 1, 1, self.btn_bg, self.add_char),
            ("9", 1, 2, self.btn_bg, self.add_char),
            ("/", 1, 3, self.btn_op_bg, self.add_char),
            ("4", 2, 0, self.btn_bg, self.add_char),
            ("5", 2, 1, self.btn_bg, self.add_char),
            ("6", 2, 2, self.btn_bg, self.add_char),
            ("*", 2, 3, self.btn_op_bg, self.add_char),
            ("1", 3, 0, self.btn_bg, self.add_char),
            ("2", 3, 1, self.btn_bg, self.add_char),
            ("3", 3, 2, self.btn_bg, self.add_char),
            ("-", 3, 3, self.btn_op_bg, self.add_char),
            ("C", 4, 0, self.btn_c_bg, self.clear),
            ("0", 4, 1, self.btn_bg, self.add_char),
            ("=", 4, 2, self.btn_eq_bg, self.calculate),
            ("+", 4, 3, self.btn_op_bg, self.add_char),
        ]

        for (text, row, col, bg, command) in buttons:
            btn = tk.Button(root, text = text, bg = bg, fg = self.btn_fg, command = lambda t = text, cmd = command: cmd(t), **btn_config)
            btn.grid(row = row, column = col, padx = 5, pady = 5, sticky = 'nsew')

    def add_char(self,char):
        self.expression += char
        self.display_var.set(self.expression)

    def clear(self, _=None):
        self.expression = ""
        self.display_var.set("")

    def calculate(self, _=None):
        if not self.expression:
            return
        expr = self.expression
        try:
            result = eval(expr)
            if isinstance(result,float):
                result = int(result)
            self.display_var.set(str(result))
            save_to_history(expr, result)
            self.expression = str(result)
        except Exception as e:
            self.display_var.set("Ошибка")
            save_to_history(expr, f"Ошибка ({e})")
            self.expression = ""

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()


