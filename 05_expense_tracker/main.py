from expense import Expense, add_expense
from storage import save_expense


def main() -> None:
    expenses: list[Expense] = []

    expense = add_expense()

    expenses.append(expense)

    save_expense(expense)


main()
