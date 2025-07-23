import tkinter as tk
from tkinter import messagebox

# Function to handle number and operator button presses
def press(key):
    entry.insert(tk.END, key)

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, width=16, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=22, height=2, font=("Arial", 18), command=clear)
        btn.grid(row=row, column=col, columnspan=4, pady=10)
        continue
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda k=text: press(k))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()