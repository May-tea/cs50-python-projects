from datetime import datetime

Expense = dict[str, str | float]


def create_expense(title: str, amount: float, expense_date: str) -> Expense:
    return {"title": title, "amount": amount, "date": expense_date}


def input_expense_date() -> str:
    while True:
        try:
            expense_date: str = input("Enter expense date (YYYY-MM-DD): ")

            datetime.strptime(expense_date, "%Y-%m-%d")

            break
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            continue

    return expense_date


def add_expense() -> Expense:
    while True:
        title: str = input("Enter Expense Title: ").strip()

        if not title:
            print("Title cannot be empty.")
            continue

        if len(title) < 3:
            print("Title must be at least 3 characters long.")
            continue

        break

    while True:
        try:
            amount: float = float(input("Enter Expense Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

    expense_date = input_expense_date()

    print("Expense added successfully.")

    return create_expense(title, amount, expense_date)
