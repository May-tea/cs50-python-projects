Book = dict[str, str | int | bool]


def create_book(title: str, author: str, year: int) -> Book:
    return {"title": title, "author": author, "year": year, "is_borrowed": False}
