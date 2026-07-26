Contact = dict[str, str]


def create_contact(name: str, phone: str, email: str) -> Contact:
    return {"name": name, "phone": phone, "email": email}
