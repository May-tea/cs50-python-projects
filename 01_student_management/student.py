def add_student(students: list[dict[str, str | int | float]]) -> None:
    name: str = input("\nEnter the student's name: ")
    age: int = int(input("Enter the student's age: "))
    score: float = float(input("Enter the student's score: "))

    students.append({"name": name, "age": age, "score": score})


def show_students(students: list[dict[str, str | int | float]]) -> None:
    if not students:
        print("\nNo students have been added yet.")
        return

    for student in students:
        display_student(student)


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
