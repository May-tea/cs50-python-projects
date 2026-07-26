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
