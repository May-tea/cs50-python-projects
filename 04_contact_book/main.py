import csv

Contact = dict[str, str]

CSV_FILE: str = "data/contacts.csv"
FIELD_NAMES: list[str] = ["name", "phone", "email"]


def load_contacts() -> list[Contact]:
    contacts: list[Contact] = []

    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                contacts.append(dict(row))
    except FileNotFoundError:
        pass

    return contacts


def save_contacts(contacts: list[Contact]) -> None:
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)

        writer.writeheader()
        writer.writerows(contacts)


def create_contact(name: str, phone: str, email: str) -> Contact:
    return {"name": name, "phone": phone, "email": email}


def add_contact(contacts: list[Contact]) -> None:
    name: str = input("\nName: ")
    phone: str = input("Phone: ")
    email: str = input("Email: ")

    contact = create_contact(name, phone, email)

    contacts.append(contact)
    save_contacts(contacts)

    print("\nContact added successfully.")


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
                print("Edit")
            case "3":
                print("Delete")
            case "4":
                print("Search")
            case "5":
                print("Show All")
            case "6":
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
