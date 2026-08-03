import unittest
from unittest.mock import patch

from analysis import calculate_total_expenses


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


if __name__ == "__main__":
    unittest.main()
