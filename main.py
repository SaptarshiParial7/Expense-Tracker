import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    item = item_entry.get()
    amount = amount_entry.get()

    if item == "" or amount == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    expenses.append({"item": item, "amount": amount})
    update_list()
    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def delete_expense():
    selected = expense_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select an expense to delete")
        return

    expenses.pop(selected[0])
    update_list()

def update_list():
    expense_list.delete(0, tk.END)
    total = 0
    for exp in expenses:
        expense_list.insert(tk.END, f"{exp['item']} - ₹{exp['amount']:.2f}")
        total += exp['amount']

    total_label.config(text=f"Total Expenses: ₹{total:.2f}")

# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Item:").grid(row=0, column=0, padx=5, pady=5)
item_entry = tk.Entry(frame)
item_entry.grid(row=0, column=1)

tk.Label(frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=1, column=1)

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)

expense_list = tk.Listbox(root, width=40)
expense_list.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_expense).pack(pady=5)

total_label = tk.Label(root, text="Total Expenses: ₹0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

root.mainloop()
