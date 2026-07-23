import re


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


def main() -> None:
    username: str = get_username()
    password: str = get_password()


if __name__ == "__main__":
    main()
