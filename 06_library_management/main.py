from book import Book
from library import (
    add_book,
    delete_book,
    search_book,
    borrow_book,
    return_book,
)
from storage import load_books


def display_menu() -> None:
    print("""
========== Library Management ==========

1. Add book
2. Delete book
3. Search book
4. Borrow book
5. Return book
6. Exit

=========================================
""")


def main() -> None:
    books: list[Book] = load_books()

    while True:
        display_menu()

        try:
            choice: int = int(input("Choose: ").strip())

            if not 1 <= choice <= 6:
                print("\nPlease choose a number between 1 and 6.")
                continue
        except ValueError:
            print("\nInvalid input. Please try again.")
            continue

        match choice:
            case 1:
                add_book(books)
            case 2:
                delete_book(books)
            case 3:
                search_book(books)
            case 4:
                borrow_book(books)
            case 5:
                return_book(books)
            case 6:
                print("\nGoodbye!")
                break


main()
