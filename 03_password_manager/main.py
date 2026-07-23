import re
import csv

CSV_FILE: str = "data/users.csv"
FIELDNAMES: list[str] = ["username", "password"]

USERNAME_PATTERN: str = r"[a-zA-Z0-9_]{3,}"
PASSWORD_PATTERN: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
PASSWORD_ERROR: str = (
    "Password must be at least 8 characters long "
    "and contain at least one uppercase letter, "
    "one lowercase letter, and one digit."
)


def get_username() -> str:
    while True:
        username: str = input("Enter your username: ").strip()

        if not username:
            print("Username cannot be empty.")
            continue

        if re.fullmatch(USERNAME_PATTERN, username):
            return username

        print(
            "Username must be at least 3 characters and contain only letters, numbers, and underscores."
        )


def get_password() -> str:
    while True:
        password: str = input("Enter your password: ").strip()

        if re.fullmatch(PASSWORD_PATTERN, password):
            return password

        print(PASSWORD_ERROR)


def username_exists(username: str) -> bool:
    try:
        with open(CSV_FILE, encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for user in reader:
                if username.lower() == user["username"].lower():
                    return True

        return False
    except FileNotFoundError:
        return False


def save_user(username: str, password: str) -> None:
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({"username": username, "password": password})


def main() -> None:
    username: str = get_username()

    if username_exists(username):
        print("Username already exists.")
        return

    password: str = get_password()

    save_user(username, password)

    print("User registered successfully.")


if __name__ == "__main__":
    main()
