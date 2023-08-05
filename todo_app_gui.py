import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("todo_list.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("todo_list.txt", "r") as f:
            for line in f:
                listbox_tasks.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create widgets
label_title = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
entry_task = tk.Entry(root, font=("Helvetica", 12))
button_add = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=add_task)
button_delete = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
listbox_tasks = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE)
scrollbar_tasks = tk.Scrollbar(root, command=listbox_tasks.yview)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

# Grid layout
label_title.grid(row=0, column=0, columnspan=2)
entry_task.grid(row=1, column=0, padx=10, pady=5)
button_add.grid(row=1, column=1, padx=10, pady=5)
listbox_tasks.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
scrollbar_tasks.grid(row=2, column=2, sticky=tk.N+tk.S)

button_delete.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Load tasks from the file
load_tasks()

# Start the main event loop
root.mainloop()
