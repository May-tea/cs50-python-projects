from storage import load_contacts
from contacts import (
    add_contact,
    edit_contact,
    delete_contact,
    search_contact,
    show_contacts,
)

Contact = dict[str, str]


def main() -> None:
    contacts: list[Contact] = load_contacts()

    while True:
        print("""
1. Add
2. Edit
3. Delete
4. Search
5. Show All
6. Exit
""")
        choice: str = input("Choose: ")

        match choice:
            case "1":
                add_contact(contacts)
            case "2":
                edit_contact(contacts)
            case "3":
                delete_contact(contacts)
            case "4":
                search_contact(contacts)
            case "5":
                show_contacts(contacts)
            case "6":
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
