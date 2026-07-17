Student = dict[str, str | int | float]


def create_student(name: str, age: int, score: float) -> Student:
    return {"name": name, "age": age, "score": score}


def add_student(students: list[Student]) -> None:
    while True:
        name: str = input("\nEnter the student's name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("\nStudent's name must contain only letters and spaces.")
            continue
        if len(name) < 3:
            print("\nStudent's name must be at least 3 characters long.")
            continue

        try:
            age: int = int(input("Enter the student's age: "))
            if not 1 <= age < 120:
                print("\nAge must be between 1 and 119.")
                continue
        except ValueError:
            print("\nAge must be a number.")
            continue

        try:
            score: float = float(input("Enter the student's score: "))
            if not 0 <= score <= 100:
                print("\nScore must be a number between 0 and 100.")
                continue
        except ValueError:
            print("\nScore must be a number.")
            continue

        break

    students.append({"name": name, "age": age, "score": score})


def show_students(students: list[Student]) -> None:
    if not students:
        print("\nNo students have been added yet.")
        return

    for student in students:
        display_student(student)


def search_student(students: list[Student]) -> None:
    if not students:
        print("\nStudents list is empty.")
        return

    while True:
        search_query: str = input("\nEnter the student's name to search: ").strip()
        if not search_query.replace(" ", "").isalpha():
            print("\nSearch query must contain only letters and spaces.")
            continue
        if len(search_query) < 3:
            print("\nSearch query must be at least 3 characters long.")
            continue

        break

    for student in students:
        if search_query.lower() in student["name"].lower():
            display_student(student)
            return

    print("\nStudent not found.")


def delete_student(students: list[Student]) -> None:
    if not students:
        print("\nStudents list is empty.")
        return

    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']}")

    while True:
        try:
            choice: int = int(input("\nEnter the number of the student to delete: "))
            if not 1 <= choice <= len(students):
                print(
                    f"\nInvalid selection. Please choose a number between 1 and {len(students)}."
                )
                continue
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            continue

        break

    deleted_student: Student = students.pop(choice - 1)

    print(f"\nStudent \"{deleted_student['name']}\" has been deleted.")


def display_student(student: Student) -> None:
    print(
        "\n---------------------\n"
        f"Name: {student['name']} \n"
        f"Age: {student['age']} \n"
        f"Score: {student['score']}\n"
        "---------------------"
    )
