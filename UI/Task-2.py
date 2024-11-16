import tkinter as ttk
def on_select(event):
    selected_value.set(combo.get())
    selected_value1.set(combo1.get())
    selected_value2.set(combo2.get())

def show_selected_option():
    selected_option = selected_value.get()
    selected_option1 = selected_value1.get()
    selected_option2 = selected_value2.get()
    messagebox.showinfo("Selected Option", f"Session: {selected_option} \n Semester: {selected_option1} \n Passing Year: {selected_option2}")
    # messagebox.showinfo("Selected Option", f"You selected: {selected_option1}")

# Create the main window
root = tk.Tk()
root.title("Session Info")

# Create a StringVar to store the selected value
selected_value = tk.StringVar()

# Create a Label to display the selected value
label = tk.Label(root, text="Session:")
label.pack(pady=10)

# Create the dropdown list
options = ["2022-23", "2023-24", "2024-25"]
combo = ttk.Combobox(root, values=options, textvariable=selected_value)
combo.pack()

selected_value1 = tk.StringVar()

label = tk.Label(root, text="Semester:")
label.pack(pady=10)

options1 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
combo1 = ttk.Combobox(root, values=options1, textvariable=selected_value1)
combo1.pack()

selected_value2 = tk.StringVar()

label = tk.Label(root, text="Passing Year:")
label.pack(pady=10)

options2 = ["2024", "2025", "2026", "2027", "2028"]
combo2 = ttk.Combobox(root, values=options2, textvariable=selected_value2)
combo2.pack()

# Bind the on_select function to the <<ComboboxSelected>> event
combo.bind("<<ComboboxSelected>>", on_select)
combo1.bind("<<ComboboxSelected>>", on_select)
combo2.bind("<<ComboboxSelected>>", on_select)

# Create a button to show the selected option
show_button = tk.Button(root, text="Show", command=show_selected_option).grid()
# show_button.grid(pady=10)
show_button = tk.Button(root, text="Cancel", command=quit).grid()
# show_button.grid(pady=10)

# Run the Tkinter event loop
root.mainloop()
