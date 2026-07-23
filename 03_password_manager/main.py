import re
import csv

FIELDNAMES = ["username", "password"]
CSV_FILE = "data/users.csv"


def save_user(username: str, password: str) -> None:
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({"username": username, "password": password})


def get_password() -> str:
    pattern: str = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

    while True:
        password: str = input("Enter your password: ").strip()

        if re.fullmatch(pattern, password):
            return password

        print(
            "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."
        )


def get_username() -> str:
    return input("Enter your username: ").strip()


def main() -> None:
    username: str = get_username()
    password: str = get_password()

    save_user(username, password)


if __name__ == "__main__":
    main()
