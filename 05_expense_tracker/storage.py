import csv
from expense import Expense, create_expense

CSV_FILE: str = "data/expenses.csv"
FIELD_NAMES: list[str] = ["title", "amount", "date"]


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
