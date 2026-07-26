from contact import create_contact
from storage import save_contacts

Contact = dict[str, str]


def add_contact(contacts: list[Contact]) -> None:
    name: str = input("\nName: ")
    phone: str = input("Phone: ")
    email: str = input("Email: ")

    contact = create_contact(name, phone, email)

    contacts.append(contact)
    save_contacts(contacts)

    print("\nContact added successfully.")


def find_contact_index(contacts: list[Contact], name: str) -> int | None:
    for index, contact in enumerate(contacts, start=1):
        if contact["name"].lower() == name.lower():
            return index

    return None


def edit_contact(contacts: list[Contact]) -> None:
    name: str = input("Name: ").strip()

    index = find_contact_index(contacts, name)

    if index is None:
        print("\nContact not found.")
        return

    new_name = input("Name: ")
    new_phone = input("Phone: ")
    new_email = input("Email: ")

    contacts[index] = create_contact(new_name, new_phone, new_email)

    save_contacts(contacts)


def delete_contact(contacts: list[Contact]) -> None:
    name: str = input("Name: ").strip()

    index = find_contact_index(contacts, name)

    if index is None:
        print("\nContact not found.")
        return

    deleted_contact = contacts.pop(index)

    save_contacts(contacts)

    print(f"\n{deleted_contact['name']} deleted successfully.")


def display_contact(contact: Contact) -> None:
    print(f"Name : {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")


def search_contact(contacts: list[Contact]) -> None:
    name: str = input("Name: ").strip().lower()

    index = find_contact_index(contacts, name)

    if index is None:
        print("\nContact not found.")
        return

    print()
    display_contact(contacts[index])


def show_contacts(contacts: list[Contact]) -> None:
    if not contacts:
        print("\nNo contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        display_contact(contact)
