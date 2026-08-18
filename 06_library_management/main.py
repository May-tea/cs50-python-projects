Book = dict[str, str | int]


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


def create_book(title: str, author: str, year: int) -> Book:
    return {"title": title, "author": author, "year": year}


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


def main() -> None:
    books: list[Book] = []

    add_book(books)
    print("\nBook added successfully.\n")

    delete_book(books)

    search_book(books)


main()
