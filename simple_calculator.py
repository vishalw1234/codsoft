import tkinter as tk

def button_click(event):
    current = display_var.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif text == "C":
        display_var.set("")
    else:
        display_var.set(current + text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

display_var = tk.StringVar()
display_var.set("")

# Display
display_frame = tk.Frame(root, bg="white", bd=3, relief=tk.RAISED)
display_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

display_label = tk.Label(display_frame, textvariable=display_var, font=("Arial", 24), bg="white", bd=2, relief=tk.SOLID)
display_label.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

# Calculator Buttons
button_frame = tk.Frame(root, bg="lightgray", bd=3, relief=tk.RAISED)
button_frame.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+')
]

for row_idx, row in enumerate(buttons):
    for col_idx, text in enumerate(row):
        btn = tk.Button(button_frame, text=text, font=("Arial", 20), bd=2, relief=tk.RAISED)
        btn.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky='nsew')
        btn.bind('<Button-1>', button_click)

# Equal button
btn_equal = tk.Button(button_frame, text="=", font=("Arial", 20), bd=2, relief=tk.RAISED)
btn_equal.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
btn_equal.bind('<Button-1>', button_click)

# Configure rows and columns to expand evenly
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for j in range(4):
    button_frame.grid_columnconfigure(j, weight=1)

root.mainloop()
