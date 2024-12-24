#5. Create Simple Interest Calculator GUI application with Python.

import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        
        interest = (principal * rate * time) / 100
        
        messagebox.showinfo("Simple Interest", f"The calculated simple interest is: ₹{interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for all fields.")

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x250")

tk.Label(root, text="Principal Amount (₹):").grid(row=0, column=0, padx=10, pady=10, sticky='w')
entry_principal = tk.Entry(root)
entry_principal.grid(row=1, column=0, padx=10, pady=10)

tk.Label(root, text="Interest Rate (%):").grid(row=2, column=0, padx=10, pady=10, sticky='w')
entry_rate = tk.Entry(root)
entry_rate.grid(row=3, column=0, padx=10, pady=10)

tk.Label(root, text="Time (Years):").grid(row=4, column=0, padx=10, pady=10, sticky='w')
entry_time = tk.Entry(root)
entry_time.grid(row=5, column=0, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)

root.mainloop()
