def delete_student(students: list[dict[str, str | int | float]]) -> None:
    if not students:
        print("\nStudents list is empty.")
        return

    for number, student in enumerate(students, start=1):
        print(f"\n{number}. {student['name']}")

    choice: int = int(input("\nWhich student do you want to delete? "))

    deleted_student: dict[str, str | int | float] = students.pop(choice - 1)

    print(f"\nStudent \"{deleted_student['name']}\" has been deleted.")


def display_student(student: dict[str, str | int | float]) -> None:
    print(
        "\n---------------------\n"
        f"Name: {student['name']} \n"
        f"Age: {student['age']} \n"
        f"Score: {student['score']}\n"
        "---------------------"
    )


def search_student(students: list[dict[str, str | int | float]]) -> None:
    if not students:
        print("\nStudents list is empty.")
        return

    search_query: str = input("\nSearch by name: ")

    for student in students:
        if search_query.lower() in student["name"].lower():
            display_student(student)
            return

    print("\nStudent not found.")


def show_students(students: list[dict[str, str | int | float]]) -> None:
    if not students:
        print("\nNo students have been added yet.")
        return

    for student in students:
        display_student(student)


def add_student(students: list[dict[str, str | int | float]]) -> None:
    name: str = input("\nEnter the student's name: ")
    age: int = int(input("Enter the student's age: "))
    score: float = float(input("Enter the student's score: "))

    students.append({"name": name, "age": age, "score": score})


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
