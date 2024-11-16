import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

# Create the main window
root = tk.Tk()
root.title("Add Two Numbers")

# Create and place the labels, entries, and buttons
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.grid(row=4, column=1, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, state='readonly')
result_entry.grid(row=2, column=1)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=0, columnspan=2)

# Start the main loop
root.minsize(400, 400)
root.mainloop()
