import csv
import pytest

from src.csv_handler import save_to_csv, load_from_csv
from src.student import Student


def test_save_to_csv(tmp_path) -> None:
    filename = tmp_path / "students.csv"

    students: list[Student] = [
        Student("Alice", 20, "alice@example.com", 18.5),
        Student("Bob", 21, "bob@example.com", 19.0),
    ]

    save_to_csv(students, str(filename))

    assert filename.exists()


def test_save_to_csv_writes_header(tmp_path) -> None:
    filename = tmp_path / "students.csv"

    students: list[Student] = [
        Student("Alice", 20, "alice@example.com", 18.5),
    ]

    save_to_csv(students, str(filename))

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

    assert header == ["name", "age", "email", "score"]


def test_save_to_csv_writes_student_data(tmp_path) -> None:
    filename = tmp_path / "students.csv"

    students: list[Student] = [
        Student("Alice", 20, "alice@example.com", 18.5),
        Student("Bob", 21, "bob@example.com", 19.0),
    ]

    save_to_csv(students, str(filename))

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows[1] == ["Alice", "20", "alice@example.com", "18.5"]
    assert rows[2] == ["Bob", "21", "bob@example.com", "19.0"]


def test_load_from_csv(tmp_path) -> None:
    filename = tmp_path / "students.csv"

    students: list[Student] = [
        Student("Alice", 20, "alice@example.com", 18.5),
        Student("Bob", 21, "bob@example.com", 19.0),
    ]

    save_to_csv(students, str(filename))

    result: list[Student] = load_from_csv(str(filename))

    assert result[0].name == "Alice"
    assert result[0].age == 20
    assert result[0].email == "alice@example.com"
    assert result[0].score == 18.5

    assert result[1].name == "Bob"
    assert result[1].age == 21
    assert result[1].email == "bob@example.com"
    assert result[1].score == 19.0


def test_load_from_csv_file_not_found(tmp_path) -> None:
    filename = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_from_csv(str(filename))


def test_load_from_empty_csv(tmp_path) -> None:
    filename = tmp_path / "students.csv"

    save_to_csv([], str(filename))

    result = load_from_csv(str(filename))

    assert result == []
