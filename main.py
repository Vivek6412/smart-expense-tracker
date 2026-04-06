import matplotlib.pyplot as plt
import json
from datetime import datetime

FILE = "expenses.json"

# -------- ADD EXPENSE --------
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(expense)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("Expense added!")

# -------- VIEW EXPENSE --------
def view_expenses():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        for exp in data:
            print(exp)
    except:
        print("No data")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        total = 0
        for item in data:
            if item["date"].startswith(month):
                total += item["amount"]

        print(f"Total expense for {month}: ₹{total}")
    except:
        print("No data found.")

def category_breakdown():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        category_totals = {}

        for item in data:
            cat = item["category"]
            category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

        print("\nCategory-wise spending:")
        for cat, amt in category_totals.items():
            print(f"{cat}: ₹{amt}")

        return category_totals
    except:
        print("No data found.")
        return {}

def highest_category():
    data = category_breakdown()
    if not data:
        return

    max_cat = max(data, key=data.get)
    print(f"Highest spending category: {max_cat}")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        total = 0
        for item in data:
            if item["date"].startswith(month):
                total += item["amount"]

        print(f"Total expense for {month}: ₹{total}")
    except:
        print("No data found.")

def category_breakdown():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        category_totals = {}

        for item in data:
            cat = item["category"]
            category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

        print("\nCategory-wise spending:")
        for cat, amt in category_totals.items():
            print(f"{cat}: ₹{amt}")

        return category_totals
    except:
        print("No data found.")
        return {}

def highest_category():
    data = category_breakdown()
    if not data:
        return

    max_cat = max(data, key=data.get)
    print(f"Highest spending category: {max_cat}")

def show_pie_chart():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        category_totals = {}

        for item in data:
            cat = item["category"]
            category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

        labels = category_totals.keys()
        values = category_totals.values()

        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()

    except:
        print("No data to show")

# -------- MAIN MENU --------
def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Breakdown")
        print("5. Highest Category")
        print("6. Show Pie Chart")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_breakdown()
        elif choice == "5":
            highest_category()
        elif choice == "6":
            show_pie_chart()
        elif choice == "7":
            break


# -------- RUN --------
if __name__ == "__main__":
    main()