from library import Library
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
    library: Library = Library()

    library.books = load_books()

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
                library.add_book()
            case 2:
                library.delete_book()
            case 3:
                library.search_book()
            case 4:
                library.borrow_book()
            case 5:
                library.return_book()
            case 6:
                print("\nGoodbye!")
                break


main()
