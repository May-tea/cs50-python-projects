import csv
from datetime import datetime

Expense = dict[str, str | float]

CSV_FILE: str = "data/expenses.csv"
FIELD_NAMES: list[str] = ["title", "amount", "date"]


def create_expense(title: str, amount: float, expense_date: str) -> Expense:
    return {"title": title, "amount": amount, "date": expense_date}


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

    while True:
        try:
            expense_date: str = input("Enter expense date (YYYY-MM-DD): ")

            datetime.strptime(expense_date, "%Y-%m-%d")

            break
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            continue

    print("Expense added successfully.")

    return create_expense(title, amount, expense_date)


def save_expense(expense: Expense) -> None:
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(expense)


def load_expenses() -> list[Expense]:
    expenses: list[Expense] = []

    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(
                    create_expense(row["title"], float(row["amount"]), row["date"])
                )
    except FileNotFoundError:
        return []

    return expenses


def calculate_total_expenses() -> float:
    expenses: list[Expense] = load_expenses()

    total: float = 0.0

    for expense in expenses:
        total += expense["amount"]

    return total


def find_largest_expense() -> Expense | None:
    expenses: list[Expense] = load_expenses()

    if not expenses:
        return None

    largest: Expense = expenses[0]

    for expense in expenses[1:]:
        if largest["amount"] < expense["amount"]:
            largest = expense

    return largest


def main() -> None:
    expenses: list[Expense] = []

    expense = add_expense()

    expenses.append(expense)

    save_expense(expense)


main()
