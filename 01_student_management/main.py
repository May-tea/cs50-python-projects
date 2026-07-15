def show_students(students):
    if not students:
        print("\nNo students have been added yet.")
        return

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Score: {student['score']}"
        )


def add_student():
    students = []

    name = input("\nEnter the student's name: ")
    age = int(input("Enter the student's age: "))
    score = float(input("Enter the student's score: "))

    students.append({"name": name, "age": age, "score": score})

    return students


def main():
    choice = int(
        input(
            "1. Add Student\n"
            "2. Show Students\n"
            "3. Search Student\n"
            "4. Delete Student\n"
            "5. Exit\n\n"
            "Select an option: "
        )
    )

    students = []

    match choice:
        case 1:
            students = add_student()
        case 2:
            show_students(students)


main()
