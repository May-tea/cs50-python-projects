def get_username() -> str:
    return input("Enter your username: ").strip()


def get_password() -> str:
    return input("Enter your password: ").strip()


def main() -> None:
    username: str = get_username()
    password: str = get_password()


if __name__ == "__main__":
    main()
