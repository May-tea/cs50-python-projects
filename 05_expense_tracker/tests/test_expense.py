import unittest

from expense import Expense, create_expense


class TestCreateExpense(unittest.TestCase):
    def test_create_expense(self):
        # Arrange
        title: str = "Food"
        amount: float = 150.0
        expense_date: str = "2026-07-30"

        # Act
        expense: Expense = create_expense(title, amount, expense_date)

        expected: Expense = {"title": "Food", "amount": 150.0, "date": "2026-07-30"}

        # Assert
        self.assertEqual(expected, expense)

    def test_create_expense_with_empty_title(self):
        # Arrange
        title: str = ""
        amount: float = 200.0
        expense_date: str = "2026-08-01"

        # Act
        expense: Expense = create_expense(title, amount, expense_date)

        expected: Expense = {"title": "", "amount": 200.0, "date": "2026-08-01"}

        # Assert
        self.assertEqual(expected, expense)

    def test_create_expense_with_negative_amount(self):
        # Arrange
        title: str = "Leisure"
        amount: float = -50.0
        expense_date: str = "2026-08-01"

        # Act
        expense: Expense = create_expense(title, amount, expense_date)

        expected: Expense = {"title": "Leisure", "amount": -50.0, "date": "2026-08-01"}

        # Assert
        self.assertEqual(expected, expense)

    def test_create_expense_with_invalid_date(self):
        # Arrange
        title: str = "Shopping"
        amount: float = 250.0
        expense_date: str = "abc"

        # Act
        expense: Expense = create_expense(title, amount, expense_date)

        expected: Expense = {"title": "Shopping", "amount": 250.0, "date": "abc"}

        # Assert
        self.assertEqual(expected, expense)


if __name__ == "__main__":
    unittest.main()
