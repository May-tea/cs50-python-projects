import csv

from book import Book

CSV_FILE: str = "data/books.csv"
FIELD_NAMES: list[str] = ["title", "author", "year", "is_borrowed"]


def save_books(books: list[Book]) -> None:
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()

        for book in books:
            writer.writerow(
                {
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "is_borrowed": book.is_borrowed,
                }
            )


def load_books() -> list[Book]:
    books: list[Book] = []

    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                book: Book = Book(row["title"], row["author"], int(row["year"]))

                book.is_borrowed = row["is_borrowed"] == "True"

                books.append(book)

    except FileNotFoundError:
        return []

    return books
