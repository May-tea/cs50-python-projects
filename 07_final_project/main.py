from src.school import School

school: School = School()


def display_menu() -> None:
    print("""
===== Student Management System =====

1. Add student
2. Exit          
""")


def main():
    while True:
        display_menu()

        try:
            choice: int = int(input("\nChoose an option: ").strip())

            if not 1 <= choice <= 2:
                print("\nPlease choose a number between 1 and 2.")
                continue
        except ValueError:
            print("\nInvalid input. Please try again.")
            continue

        match choice:
            case 1:
                pass
            case 2:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
