import re
import csv

FIELDNAMES = ["username", "password"]
CSV_FILE = "data/users.csv"
PASSWORD_ERROR = (
    "Password must be at least 8 characters long "
    "and contain at least one uppercase letter, "
    "one lowercase letter, and one digit."
)
PASSWORD_PATTERN: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"


def get_username() -> str:
    return input("Enter your username: ").strip()


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
