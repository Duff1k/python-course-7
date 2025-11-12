import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import threading
import time

tasks = []

def add_task():
    task_text = entry_task.get()
    task_time = time_var.get()
    if not task_text:
        messagebox.showerror("Ошибка", "Введите задачу")
        return

    task = (task_text, task_time)
    tasks.append(task)
    listbox.insert(tk.END, f"{task_text}-{task_time}")
    entry_task.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Информация", "Выберите хотя бы одну задачу для удаления")
        return
    for index in reversed(selected):
        listbox.delete(index)
        del tasks[index]

def save_tasks():
    if not tasks:
        messagebox.showerror("Информация", "Задач для сохранения нет")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        title="Сохранить задачу как...."
    )

    if not file_path:
        return

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for text, t in tasks:
                f.write(f"{text}-{t}\n")
        messagebox.showinfo("Успешно", f"Задачи успешно сохранены в {file_path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл, ошибка: {e}")


def check_tasks():
    while True:
        now = datetime.now().strftime("%H:%M")
        print(now)
        for text, t in tasks[:]:
            if t == now:
                messagebox.showinfo("Напоминание", f"Пора выполнять задачу на время: {t}, Задача: {text}")
            i = tasks.index((text, t))
            listbox.delete(i)
            tasks.remove((text, t))
        time.sleep(5)

window = tk.Tk()
window.title("Планировщик задач")
window.geometry("600x600")
window.configure(background="#3136d4")

tk.Label(window, text="Введите задачу:", font=("Arial", 15), background="#3136d4", fg="#FFFFFF").pack()
entry_task = tk.Entry(window, font=("Arial", 15), width=40)
entry_task.pack(pady=5)

frame_time = tk.Frame(window, background="#3136d4")
frame_time.pack(pady=5)

tk.Label(frame_time, text = "Выберите время: ", font=("Arial", 12), background="#3136d4").grid(row=0, column=0, padx=5)

time_options = [f"{h:02d}:{m:02d}" for h in range(20, 24) for m in(0,47)]
time_var = tk.StringVar(value=time_options[0])

time_menu = tk.OptionMenu(frame_time, time_var, *time_options)
time_menu.config(width=10, font = ("Arial", 12))
time_menu.grid(row=0, column=1)


listbox = tk.Listbox(window, width=60, height=10, font=("Arial", 12), selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

frame_buttons = tk.Frame(window, bg="#3136d4")
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text = "Добавить", command=add_task, font=("Arial", 12), bg="lightgreen", width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text = "Удалить", command=delete_task, font=("Arial", 12), bg="tomato", width=10).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text = "Сохранить", command=save_tasks,font=("Arial", 12), bg="lightblue", width=10).grid(row=0, column=2, padx=5)

thread = threading.Thread(target=check_tasks, daemon=True)
thread.start()

window.mainloop()