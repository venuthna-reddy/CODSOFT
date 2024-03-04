import tkinter as tk

def calculate():
    try:
        
        result.set(eval(entry.get()))
    except:
        
        result.set("Error")

def key_pressed(event):
    if event.char.isdigit() or event.char in ['+', '-', '*', '/', '.']:
        
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        
        calculate()
    elif event.keysym == "BackSpace":
        
        entry.delete(len(entry.get()) - 1, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=('Arial', 14))
entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  

entry.bind('<Key>', key_pressed)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

for i in range(3):
    for j in range(3):
        
        digit = i * 3 + j + 1  
        btn = tk.Button(buttons_frame, text=str(digit), padx=20, pady=10,
                        font=('Arial', 12), command=lambda digit=digit: entry.insert(tk.END, str(digit)))
        btn.grid(row=i, column=j, padx=5, pady=5)  


zero_btn = tk.Button(buttons_frame, text="0", padx=20, pady=10,
                     font=('Arial', 12), command=lambda: entry.insert(tk.END, "0"))
zero_btn.grid(row=3, column=0, padx=5, pady=5)

decimal_btn = tk.Button(buttons_frame, text=".", padx=22, pady=10,
                        font=('Arial', 12), command=lambda: entry.insert(tk.END, "."))
decimal_btn.grid(row=3, column=1, padx=5, pady=5)

equals_btn = tk.Button(buttons_frame, text="=", padx=20, pady=10,
                       font=('Arial', 12), command=calculate)
equals_btn.grid(row=3, column=2, padx=5, pady=5)


operators = ['+', '-', '*', '/']
operators_frame = tk.Frame(root)
operators_frame.pack()

for i, operator in enumerate(operators):
    btn = tk.Button(operators_frame, text=operator, padx=20, pady=10,
                    font=('Arial', 12), command=lambda operator=operator: entry.insert(tk.END, operator))
    btn.grid(row=i, column=0, padx=5, pady=5)

clear_btn = tk.Button(operators_frame, text="Clear", padx=10, pady=10,
                      font=('Arial', 12), command=lambda: entry.delete(0, tk.END))
clear_btn.grid(row=len(operators), column=0, padx=5, pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Arial', 14))
result_label.pack(pady=10)

root.mainloop()