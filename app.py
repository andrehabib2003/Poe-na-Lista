import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage
from time import sleep

# Cores
dark_gray = "#212529"
gray = "#343A40"
light_gray = "#CED4DA"
green = "#53A93E"
red = "#CC4848"
blue = "#54B6E0"

# Janela
window = tk.Tk()
window.title('Põe na Lista!')
window.configure(bg=dark_gray)
window.geometry("500x600")

editing_frame = None


# Função para adicionar tarefa
def add_task():
    global editing_frame

    task = task_input.get().strip()
    if task and task != "Item a ser adicionado":
        if editing_frame is not None:
            update_task(task)
            editing_frame = None
        else:
            add_item_task(task)
            task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Tarefa em branco, por favor, insira uma tarefa")


def add_item_task(task):
    frame_task = tk.Frame(canvas_interior, bg=gray, bd=0, relief=tk.SOLID)

    label_task = tk.Label(frame_task, text=task, font=("Noto Sans Sogdian", 12), bg=gray, fg="white", width=36, height=1, anchor="w")
    label_task.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    edit_button = tk.Button(frame_task, image=edit_icon, command=lambda f=frame_task, l=label_task: prepare_edit(f, l), bg=gray, relief=tk.FLAT)
    edit_button.pack(side=tk.RIGHT, padx=2)

    complete_button = tk.Button(frame_task, image=delete_icon, command=lambda f=frame_task: delete_task(f), bg=gray, relief=tk.FLAT)
    complete_button.pack(side=tk.RIGHT, padx=2)

    frame_task.pack(fill=tk.X, padx=5, pady=5)

    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def prepare_edit(frame_task, label_task):
    global editing_frame
    editing_frame = frame_task
    task_input.delete(0, tk.END)
    task_input.insert(0, label_task.cget("text"))


# noinspection PyUnresolvedReferences
def update_task(new_task):
    global editing_frame
    for widget in editing_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=new_task)


def delete_task(frame_task):
    frame_task.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


edit_icon = PhotoImage(file="edit.png").subsample(3, 3)
delete_icon = PhotoImage(file="delete.png").subsample(3, 3)

# Titulo
title_font = font.Font(family="Patua One", size=20, weight="bold")
# noinspection PyNoneFunctionAssignment
title = tk.Label(window, text="Põe na Lista!", font=title_font, bg=dark_gray, fg=green).pack(pady=10)

frame = tk.Frame(window, bg=dark_gray)
frame.pack(pady=10)

# Entrada de Dados
task_input = tk.Entry(frame, font=("Noto Sans Sogdian", 12), relief=tk.FLAT, bg=gray, fg="white", width=30)
task_input.pack(side=tk.LEFT, padx=10)

addtask_button = tk.Button(frame, command=add_task, text="Adicionar Tarefa", bg=green, fg="white", height=1, width=15, font=("Noto Sans Sogdian", 11), relief=tk.FLAT)
addtask_button.pack(side=tk.LEFT, padx=10)

# Frame para lista de tarefas c/ rolagem
frame_tasklist = tk.Frame(window, bg=dark_gray)
frame_tasklist.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_tasklist, bg=dark_gray, borderwidth=0, highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_tasklist, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set, bg=dark_gray)
canvas_interior = tk.Frame(canvas, bg=dark_gray)
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Programa principal
window.mainloop()
sleep(10)
