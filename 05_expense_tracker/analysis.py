import statistics
from expense import Expense
from storage import load_expenses


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


def find_expenses_by_date(expense_date: str) -> list[Expense]:
    expenses: list[Expense] = load_expenses()

    date_expenses: list[Expense] = []

    for expense in expenses:
        if expense_date == expense["date"]:
            date_expenses.append(expense)

    return date_expenses


def calculate_average_expense() -> float | None:
    expenses: list[Expense] = load_expenses()

    if not expenses:
        return None

    amounts: list[float] = []

    for expense in expenses:
        amounts.append(expense["amount"])

    return statistics.mean(amounts)
