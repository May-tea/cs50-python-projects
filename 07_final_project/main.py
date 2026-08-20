from src.school import School
from src.student import Student
from src.validators import validate_name, validate_age, validate_email, validate_score

school: School = School()


def display_menu() -> None:
    print("""
===== Student Management System =====

1. Add student
2. Show students
3. Search student
4. Delete student
5. Edit student
6. Sort students by score
7. Show average score
8. Exit          
""")


def add_student() -> None:
    name: str = input("\nName: ").strip()

    if not validate_name(name):
        print("\nInvalid name.")
        return

    try:
        age: int = int(input("\nAge: ").strip())
    except ValueError:
        print("\nAge must be an integer.")
        return

    if not validate_age(age):
        print("\nInvalid age.")
        return

    email: str = input("\nEmail: ").strip()

    if not validate_email(email):
        print("\nInvalid email.")
        return

    try:
        score: float = float(input("\nScore: ").strip())
    except ValueError:
        print("\nScore must be a number.")
        return

    if not validate_score(score):
        print("\nInvalid score.")
        return

    student: Student = Student(name, age, email, score)

    school.add_student(student)

    print("\nStudent added successfully.")


def show_students() -> None:
    students: list[Student] = school.get_students()

    if not students:
        print("\nStudents list is empty.")
        return

    for student in students:
        print(student)


def search_student() -> None:
    query: str = input("\nSearch by name: ").strip()

    if not validate_name(query):
        print("\nInvalid search query.")
        return

    students: list[Student] = school.search_student(query)

    if not students:
        print("\nNo students found.")
        return

    for student in students:
        print(student)


def delete_student() -> None:
    students: list[Student] = school.get_students()

    if not students:
        print("\nStudents list is empty.")
        return

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")

    try:
        choice: int = int(input("\nChoose a student to delete: ").strip())

        if not 1 <= choice <= len(students):
            print("\nInvalid student number.")
            return
    except ValueError:
        print("\nInvalid input. Please try again.")
        return

    student: Student = school.get_student(choice - 1)

    school.remove_student(student)

    print(f"\nStudent '{student.name}' deleted successfully.")


def edit_student() -> None:
    students: list[Student] = school.get_students()

    if not students:
        print("\nStudents list is empty.")
        return

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")

    try:
        choice: int = int(input("\nChoose a student to edit: ").strip())

        if not 1 <= choice <= len(students):
            print("\nInvalid student number.")
            return
    except ValueError:
        print("\nInvalid input. Please try again.")
        return

    student: Student = school.get_student(choice - 1)

    new_name: str = input("\nNew name: ").strip()

    if not validate_name(new_name):
        print("\nInvalid name.")
        return

    try:
        new_age: int = int(input("\nNew age: ").strip())
    except ValueError:
        print("\nInvalid input. Please try again.")
        return

    if not validate_age(new_age):
        print("\nInvalid age.")
        return

    new_email: str = input("\nNew email: ").strip()

    if not validate_email(new_email):
        print("\nInvalid email.")
        return

    try:
        new_score: float = float(input("\nNew score: ").strip())
    except ValueError:
        print("\nInvalid input. Please try again.")
        return

    if not validate_score(new_score):
        print("\nInvalid score.")
        return

    school.edit_student(student, new_name, new_age, new_email, new_score)

    print(f"\nStudent '{student.name}' updated successfully.")


def sort_students() -> None:
    students: list[Student] = school.sort_students_by_score()

    if not students:
        print("\nStudents list is empty.")
        return

    for student in students:
        print(student)


def show_average_score() -> None:
    if not school.get_students():
        print("\nStudents list is empty.")
        return

    average_score: float = school.get_average_score()

    print(f"\nAverage score: {average_score:.2f}")


def main() -> None:
    while True:
        display_menu()

        try:
            choice: int = int(input("\nChoose an option: ").strip())

            if not 1 <= choice <= 8:
                print("\nPlease choose a number between 1 and 8.")
                continue
        except ValueError:
            print("\nInvalid input. Please try again.")
            continue

        match choice:
            case 1:
                add_student()
            case 2:
                show_students()
            case 3:
                search_student()
            case 4:
                delete_student()
            case 5:
                edit_student()
            case 6:
                sort_students()
            case 7:
                show_average_score()
            case 8:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
