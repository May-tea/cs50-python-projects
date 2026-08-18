import csv

from book import Book

CSV_FILE: str = "data/books.csv"
FIELD_NAMES: list[str] = ["title", "author", "year", "is_borrowed"]


def save_books(books: list[Book]) -> None:
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(books)


def load_books() -> list[Book]:
    books: list[Book] = []

    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books.append(
                    {
                        "title": row["title"],
                        "author": row["author"],
                        "year": int(row["year"]),
                        "is_borrowed": row["is_borrowed"] == "True",
                    }
                )

    except FileNotFoundError:
        return []

    return books
