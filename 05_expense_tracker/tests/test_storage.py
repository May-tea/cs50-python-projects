import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from storage import save_expense, load_expenses


class TestStorage(unittest.TestCase):
    def test_save_and_load_single_expense(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_file = Path(temp_dir) / "expenses.csv"

            with patch("storage.CSV_FILE", str(csv_file)):
                # Arrange
                expense = {
                    "title": "Food",
                    "amount": 100.0,
                    "date": "2026-07-30",
                }

                # Act
                save_expense(expense)
                expenses = load_expenses()

                # Assert
                self.assertEqual([expense], expenses)


def test_load_expenses_with_empty_file(self):
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file = Path(temp_dir) / "expenses.csv"

        csv_file.touch()

        with patch("storage.CSV_FILE", str(csv_file)):
            # Act
            expenses = load_expenses()

            # Assert
            self.assertEqual([], expenses)


if __name__ == "__main__":
    unittest.main()
