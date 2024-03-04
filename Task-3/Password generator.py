import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()


    if complexity == "Simple":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(characters) for i in range(length))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

complexity_var = tk.StringVar()
complexity_var.set("Simple")
simple_radio = tk.Radiobutton(root, text="Simple", variable=complexity_var, value="Simple")
simple_radio.grid(row=1, column=0, padx=10, pady=5)
medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium")
medium_radio.grid(row=1, column=1, padx=10, pady=5)
complex_radio = tk.Radiobutton(root, text="Complex", variable=complexity_var, value="Complex")
complex_radio.grid(row=1, column=2, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=3, padx=10, pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=('Arial', 12), wraplength=300)
password_label.grid(row=3, columnspan=3, padx=10, pady=10)

strength_label = tk.Label(root, text="Password Strength:", font=('Arial', 12))
strength_label.grid(row=4, column=0, padx=10, pady=5)
strength_var = tk.StringVar()
strength_var.set("Weak")
strength_indicator = tk.Label(root, textvariable=strength_var, font=('Arial', 12), fg="red")
strength_indicator.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

def check_strength(password):
    if len(password) < 8:
        strength_var.set("Weak")
        strength_indicator.config(fg="red")
    elif len(password) < 12:
        strength_var.set("Moderate")
        strength_indicator.config(fg="orange")
    else:
        strength_var.set("Strong")
        strength_indicator.config(fg="green")

password_var.trace_add("write", lambda name, index, mode: check_strength(password_var.get()))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, columnspan=3, padx=10, pady=10)

root.mainloop()