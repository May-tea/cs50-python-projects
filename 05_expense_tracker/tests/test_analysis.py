import unittest
from unittest.mock import patch

from analysis import (
    calculate_total_expenses,
    find_largest_expense,
    find_expenses_by_date,
)


class TestAnalysis(unittest.TestCase):
    @patch("analysis.load_expenses")
    def test_calculate_total_expenses_with_multiple_expenses(self, mock_load_expenses):
        # Arrange
        mock_load_expenses.return_value = [
            {
                "title": "Food",
                "amount": 100.0,
                "date": "2026-07-30",
            },
            {
                "title": "Taxi",
                "amount": 50.0,
                "date": "2026-07-30",
            },
            {
                "title": "Book",
                "amount": 250.0,
                "date": "2026-07-31",
            },
        ]

        # Act
        total: float = calculate_total_expenses()

        # Assert
        expected: float = 400.0
        self.assertEqual(expected, total)

    @patch("analysis.load_expenses")
    def test_calculate_total_expenses_with_no_expenses(self, mock_load_expenses):
        # Arrange
        mock_load_expenses.return_value = []

        # Act
        total: float = calculate_total_expenses()

        # Assert
        expected: float = 0.0
        self.assertEqual(expected, total)

    @patch("analysis.load_expenses")
    def test_find_largest_expense(self, mock_load_expenses):
        # Arrange
        mock_load_expenses.return_value = [
            {"title": "Food", "amount": 100.0, "date": "2026-07-30"},
            {"title": "Laptop", "amount": 1500.0, "date": "2026-07-31"},
            {"title": "Taxi", "amount": 50.0, "date": "2026-07-31"},
        ]

        # Act
        largest = find_largest_expense()

        # Assert
        expected = {
            "title": "Laptop",
            "amount": 1500.0,
            "date": "2026-07-31",
        }
        self.assertEqual(expected, largest)

    @patch("analysis.load_expenses")
    def test_find_largest_expense_with_no_expenses(self, mock_load_expenses):
        # Arrange
        mock_load_expenses.return_value = []

        # Act
        largest = find_largest_expense()

        # Assert
        self.assertIsNone(largest)

    @patch("analysis.load_expenses")
    def test_find_expenses_by_date(self, mock_load_expenses):
        # Arrange
        mock_load_expenses.return_value = [
            {
                "title": "Food",
                "amount": 100.0,
                "date": "2026-07-30",
            },
            {
                "title": "Taxi",
                "amount": 50.0,
                "date": "2026-07-30",
            },
            {
                "title": "Book",
                "amount": 250.0,
                "date": "2026-07-31",
            },
        ]

        expense_date = "2026-07-30"

        # Act
        date_expenses = find_expenses_by_date(expense_date)

        # Assert
        expected = [
            {
                "title": "Food",
                "amount": 100.0,
                "date": "2026-07-30",
            },
            {
                "title": "Taxi",
                "amount": 50.0,
                "date": "2026-07-30",
            },
        ]
        self.assertEqual(expected, date_expenses)

    @patch("analysis.load_expenses")
    def test_find_expenses_by_date_with_no_matching_expenses(self, mock_load_expenses):
        # Arrange
        mock_load_expenses.return_value = [
            {
                "title": "Food",
                "amount": 100.0,
                "date": "2026-07-30",
            },
            {
                "title": "Taxi",
                "amount": 50.0,
                "date": "2026-07-30",
            },
            {
                "title": "Book",
                "amount": 250.0,
                "date": "2026-07-31",
            },
        ]

        expense_date = "2026-08-01"

        # Act
        date_expenses = find_expenses_by_date(expense_date)

        # Assert
        self.assertEqual([], date_expenses)


if __name__ == "__main__":
    unittest.main()
