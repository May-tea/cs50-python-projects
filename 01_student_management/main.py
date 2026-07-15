from student import add_student, show_students, search_student, delete_student


def main() -> None:
    students: list[dict[str, str | int | float]] = []

    while True:
        choice: int = int(
            input(
                "\n1. Add Student\n"
                "2. Show Students\n"
                "3. Search Student\n"
                "4. Delete Student\n"
                "5. Exit\n\n"
                "Select an option: "
            )
        )

        match choice:
            case 1:
                add_student(students)
            case 2:
                show_students(students)
            case 3:
                search_student(students)
            case 4:
                delete_student(students)
            case 5:
                print("\nGoodbye!")
                break
            case _:
                print("\nInvalid option. Please select a number between 1 and 5.")


main()
