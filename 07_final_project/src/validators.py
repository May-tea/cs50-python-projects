import re


def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.]+\.\w+$"

    return re.match(pattern, email) is not None
