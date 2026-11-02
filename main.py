
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# CREATE CSV FILE
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# ADD EXPENSE
def add_expense():
    print("\n--- ADD EXPENSE ---")

    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter expense category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# VIEW ALL EXPENSES
def view_expenses():
    print("\n--- ALL EXPENSES ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses recorded yet.")
        return

    for row in rows:
        print(" | ".join(row))


# TOTAL EXPENSE
def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print("\nTotal Expenses: Rs.", round(total, 2))


# MAIN MENU
def main():
    create_file()

    while True:
        print("\n================================")
        print(" PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
