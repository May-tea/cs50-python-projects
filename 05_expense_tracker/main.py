from analysis import (
    calculate_total_expenses,
    find_largest_expense,
    find_expenses_by_date,
    calculate_average_expense,
)
from expense import Expense, add_expense, input_expense_date
from storage import save_expense


def display_menu() -> None:
    print("""
========== Expense Tracker ==========

1. Add Expense
2. Show Total Expenses
3. Show Largest Expense
4. Search Expenses by Date
5. Show Average Expense
6. Exit

=====================================
""")


def display_expense(expense: Expense) -> None:
    print(f"""
------------------------
Title : {expense['title']}
Amount: {expense['amount']}
Date  : {expense['date']}
------------------------
""")


def main() -> None:
    while True:
        display_menu()

        try:
            choice: int = int(input("Choose: "))

            if not 1 <= choice <= 6:
                print("Please choose a number between 1 to 6.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        match choice:
            case 1:
                expense = add_expense()
                display_expense(expense)
                save_expense(expense)
            case 2:
                print(f"Total Expenses: {calculate_total_expenses():.2f}")
            case 3:
                largest = find_largest_expense()

                if largest is None:
                    print("\nNo expenses found.")
                else:
                    display_expense(largest)
            case 4:
                expense_date = input_expense_date()

                expenses = find_expenses_by_date(expense_date)

                if not expenses:
                    print("\nNo expenses found for this date.")
                else:
                    for expense in expenses:
                        display_expense(expense)
            case 5:
                avg = calculate_average_expense()

                if avg is None:
                    print("\nNo expenses found.")
                else:
                    print(f"Average Expense: {avg:.2f}")
            case 6:
                print("\nGoodbye!")
                break


main()
