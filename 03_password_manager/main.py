def get_username() -> str:
    return input("Enter your username: ").strip()


def main() -> None:
    username: str = get_username()


if __name__ == "__main__":
    main()
