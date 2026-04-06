# import tkinter as tk
# from tkinter import messagebox
# import json
# from datetime import datetime
# import matplotlib.pyplot as plt

# FILE = "expenses.json"

# # -------- ADD EXPENSE --------
# def add_expense():
#     amount = amount_entry.get()
#     category = category_entry.get()
#     description = description_entry.get()

#     if not amount or not category:
#         messagebox.showerror("Error", "Fill all fields")
#         return

#     expense = {
#         "amount": float(amount),
#         "category": category,
#         "description": description,
#         "date": datetime.now().strftime("%Y-%m-%d")
#     }

#     try:
#         with open(FILE, "r") as f:
#             data = json.load(f)
#     except:
#         data = []

#     data.append(expense)

#     with open(FILE, "w") as f:
#         json.dump(data, f, indent=4)

#     messagebox.showinfo("Success", "Expense Added!")

# # -------- VIEW EXPENSE --------
# def view_expenses():
#     try:
#         with open(FILE, "r") as f:
#             data = json.load(f)

#         output = ""
#         for exp in data:
#             output += f"{exp['date']} | ₹{exp['amount']} | {exp['category']} | {exp['description']}\n"

#         result_box.delete(1.0, tk.END)
#         result_box.insert(tk.END, output)

#     except:
#         messagebox.showerror("Error", "No data found")

# # -------- MONTHLY SUMMARY --------
# def monthly_summary():
#     month = month_entry.get()

#     try:
#         with open(FILE, "r") as f:
#             data = json.load(f)

#         total = 0
#         for item in data:
#             if item["date"].startswith(month):
#                 total += item["amount"]

#         messagebox.showinfo("Summary", f"Total for {month}: ₹{total}")

#     except:
#         messagebox.showerror("Error", "No data")

# # -------- CATEGORY BREAKDOWN --------
# def category_breakdown():
#     try:
#         with open(FILE, "r") as f:
#             data = json.load(f)

#         category_totals = {}

#         for item in data:
#             cat = item["category"]
#             category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

#         output = ""
#         for cat, amt in category_totals.items():
#             output += f"{cat}: ₹{amt}\n"

#         result_box.delete(1.0, tk.END)
#         result_box.insert(tk.END, output)

#     except:
#         messagebox.showerror("Error", "No data")

# # -------- HIGHEST CATEGORY --------
# def highest_category():
#     try:
#         with open(FILE, "r") as f:
#             data = json.load(f)

#         category_totals = {}

#         for item in data:
#             cat = item["category"]
#             category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

#         max_cat = max(category_totals, key=category_totals.get)

#         messagebox.showinfo("Highest", f"Highest spending: {max_cat}")

#     except:
#         messagebox.showerror("Error", "No data")

# # -------- PIE CHART --------
# def show_pie_chart():
#     try:
#         with open(FILE, "r") as f:
#             data = json.load(f)

#         category_totals = {}

#         for item in data:
#             cat = item["category"]
#             category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

#         plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%')
#         plt.title("Expense Distribution")
#         plt.show()

#     except:
#         messagebox.showerror("Error", "No data")

# # -------- WINDOW --------
# root = tk.Tk()
# root.title("Smart Expense Tracker")
# root.geometry("500x600")

# # INPUTS
# tk.Label(root, text="Amount").pack()
# amount_entry = tk.Entry(root)
# amount_entry.pack()

# tk.Label(root, text="Category").pack()
# category_entry = tk.Entry(root)
# category_entry.pack()

# tk.Label(root, text="Description").pack()
# description_entry = tk.Entry(root)
# description_entry.pack()

# tk.Label(root, text="Month (YYYY-MM)").pack()
# month_entry = tk.Entry(root)
# month_entry.pack()

# # BUTTONS
# tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
# tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=5)
# tk.Button(root, text="Monthly Summary", command=monthly_summary).pack(pady=5)
# tk.Button(root, text="Category Breakdown", command=category_breakdown).pack(pady=5)
# tk.Button(root, text="Highest Category", command=highest_category).pack(pady=5)
# tk.Button(root, text="Show Pie Chart", command=show_pie_chart).pack(pady=5)

# # OUTPUT BOX
# result_box = tk.Text(root, height=10)
# result_box.pack()

# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import matplotlib.pyplot as plt

FILE = "expenses.json"

# -------- FUNCTIONS --------
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()

        if not category:
            messagebox.showerror("Error", "Category required")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        try:
            with open(FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(expense)

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Success", "Expense Added!")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid amount")

def view_expenses():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        result_box.delete(1.0, tk.END)

        for exp in data:
            result_box.insert(tk.END, f"{exp['date']} | ₹{exp['amount']} | {exp['category']} | {exp['description']}\n")

    except:
        messagebox.showerror("Error", "No data")

def monthly_summary():
    month = month_entry.get()
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        total = sum(item["amount"] for item in data if item["date"].startswith(month))
        messagebox.showinfo("Summary", f"Total: ₹{total}")

    except:
        messagebox.showerror("Error", "No data")

def category_breakdown():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        result_box.delete(1.0, tk.END)

        category_totals = {}
        for item in data:
            category_totals[item["category"]] = category_totals.get(item["category"], 0) + item["amount"]

        for cat, amt in category_totals.items():
            result_box.insert(tk.END, f"{cat}: ₹{amt}\n")

    except:
        messagebox.showerror("Error", "No data")

def highest_category():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        category_totals = {}
        for item in data:
            category_totals[item["category"]] = category_totals.get(item["category"], 0) + item["amount"]

        max_cat = max(category_totals, key=category_totals.get)
        messagebox.showinfo("Highest Category", max_cat)

    except:
        messagebox.showerror("Error", "No data")

def show_pie_chart():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        category_totals = {}
        for item in data:
            category_totals[item["category"]] = category_totals.get(item["category"], 0) + item["amount"]

        plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()

    except:
        messagebox.showerror("Error", "No data")

# -------- WINDOW --------
root = tk.Tk()
root.title("💰 Smart Expense Tracker")
root.geometry("600x600")
root.configure(bg="#1e1e2f")

# -------- TITLE --------
title = tk.Label(root, text="Smart Expense Tracker", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# -------- INPUT FRAME --------
frame = tk.Frame(root, bg="#2c2c3c", padx=10, pady=10)
frame.pack(pady=10)

tk.Label(frame, text="Amount", bg="#2c2c3c", fg="white").grid(row=0, column=0)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1)

tk.Label(frame, text="Category", bg="#2c2c3c", fg="white").grid(row=1, column=0)
category_entry = tk.Entry(frame)
category_entry.grid(row=1, column=1)

tk.Label(frame, text="Description", bg="#2c2c3c", fg="white").grid(row=2, column=0)
description_entry = tk.Entry(frame)
description_entry.grid(row=2, column=1)

tk.Label(frame, text="Month (YYYY-MM)", bg="#2c2c3c", fg="white").grid(row=3, column=0)
month_entry = tk.Entry(frame)
month_entry.grid(row=3, column=1)

# -------- BUTTON FRAME --------
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

buttons = [
    ("Add Expense", add_expense),
    ("View Expenses", view_expenses),
    ("Monthly Summary", monthly_summary),
    ("Category Breakdown", category_breakdown),
    ("Highest Category", highest_category),
    ("Show Pie Chart", show_pie_chart),
]

for text, cmd in buttons:
    tk.Button(btn_frame, text=text, width=20, bg="#4CAF50", fg="white", command=cmd).pack(pady=5)

# -------- OUTPUT --------
result_box = tk.Text(root, height=10, width=70)
result_box.pack(pady=10)

root.mainloop()