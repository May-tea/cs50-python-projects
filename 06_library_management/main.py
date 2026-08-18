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


def main() -> None:
    books: list[Book] = []

    add_book(books)
    print("\nBook added successfully.")


main()
