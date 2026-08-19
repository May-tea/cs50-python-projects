import re


def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.]+\.\w+$"

    return re.match(pattern, email) is not None


def validate_name(name: str) -> bool:
    return name.replace(" ", "").isalpha() and len(name) >= 3


def validate_age(age: int) -> bool:
    return 1 <= age <= 119


def validate_score(score: float) -> bool:
    return 0 <= score <= 20
