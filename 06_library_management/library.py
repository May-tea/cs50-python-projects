from book import Book, create_book


def add_book(books: list[Book]) -> None:
    while True:
        title: str = input("Enter book title: ").strip().lower()

        if not title:
            print("\nTitle can not be empty.\n")
            continue

        author: str = input("Enter author: ").strip().lower()

        if not author:
            print("\nAuthor can not be empty.\n")
            continue

        try:
            year: int = int(input("Enter publication year: ").strip())
        except ValueError:
            print("\nPlease enter a valid publication year for the book.\n")
            continue

        break

    new_book = create_book(title, author, year)

    books.append(new_book)

    print("\nBook added successfully.\n")


def delete_book(books: list[Book]) -> None:
    if not books:
        print("\nThere are no books in the library.\n")
        return

    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']} - {book['author']} ({book['year']})")

    while True:
        try:
            choice: int = int(input("\nEnter book number to delete: ").strip())

            if not 1 <= choice <= len(books):
                print("\nPlease enter a valid number.")
                continue
        except ValueError:
            print("\nJust integers accepted.")
            continue

        break

    deleted_book: Book = books.pop(choice - 1)

    print(f"\nBook '{deleted_book['title']}' deleted successfully.")


def search_book(books: list[Book]) -> None:
    if not books:
        print("\nThere are no books in the library.\n")
        return

    while True:
        query: str = input("\nEnter search query: ").strip().lower()

        if not query:
            print("\nTry something to search.")
            continue

        break

    found: bool = False

    for book in books:
        if query in book["title"] or query in book["author"]:
            print(f"\n{book['title']} - {book['author']} ({book['year']})")
            found = True

    if not found:
        print("No books found.")
        return


def borrow_book(books: list[Book]) -> None:
    if not books:
        print("\nThere are no books in the library.")
        return

    available_books: list[Book] = []

    for book in books:
        if not book["is_borrowed"]:
            available_books.append(book)

    if not available_books:
        print("\nThere are no available books.")
        return

    print("\nAvailable books:\n")

    for index, book in enumerate(available_books, start=1):
        print(f"{index}. {book['title']} - {book['author']} ({book['year']})")

    while True:
        try:
            choice: int = int(input("Enter book number to borrow: "))

            if not 1 <= choice <= len(available_books):
                print("\nPlease enter a valid number.")
                continue
        except ValueError:
            print("\nJust integers accepted.")
            continue

        break

    borrowed_book: Book = available_books[choice - 1]

    borrowed_book["is_borrowed"] = True

    print(f"\nBook '{borrowed_book['title']}' borrowed successfully.")


def return_book(books: list[Book]) -> None:
    if not books:
        print("\nThere are no books in the library.")
        return

    borrowed_books: list[Book] = []

    for book in books:
        if book["is_borrowed"]:
            borrowed_books.append(book)

    if not borrowed_books:
        print("\nThere are no borrowed books.")
        return

    print("\nBorrowed books:\n")

    for index, book in enumerate(borrowed_books, start=1):
        print(f"{index}. {book['title']} - {book['author']} ({book['year']})")

    while True:
        try:
            choice: int = int(input("Enter book number to return: "))

            if not 1 <= choice <= len(borrowed_books):
                print("\nPlease enter a valid number.")
                continue
        except ValueError:
            print("\nJust integers accepted.")
            continue

        break

    returned_book: Book = borrowed_books[choice - 1]

    returned_book["is_borrowed"] = False

    print(f"\nBook '{returned_book['title']}' returned successfully.")
