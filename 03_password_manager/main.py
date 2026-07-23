import re
import csv

FIELDNAMES = ["username", "password"]
CSV_FILE = "data/users.csv"


def get_username() -> str:
    return input("Enter your username: ").strip()


def get_password() -> str:
    pattern: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

    while True:
        password: str = input("Enter your password: ").strip()

        if re.fullmatch(pattern, password):
            return password

        print(
            "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."
        )


def username_exists(username: str) -> bool:
    try:
        with open(CSV_FILE) as file:
            reader = csv.DictReader(file)

            for user in reader:
                if username.lower() == user["username"].lower():
                    return True

        return False
    except FileNotFoundError:
        return False


def save_user(username: str, password: str) -> None:
    with open(CSV_FILE, "a", newline="") as file:
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


if __name__ == "__main__":
    main()
