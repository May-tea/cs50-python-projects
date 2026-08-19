from src.school import School
from src.student import Student
from src.validators import validate_name, validate_age, validate_email, validate_score

school: School = School()


def display_menu() -> None:
    print("""
===== Student Management System =====

1. Add student
2. Show students
3. Exit          
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


def main() -> None:
    while True:
        display_menu()

        try:
            choice: int = int(input("\nChoose an option: ").strip())

            if not 1 <= choice <= 3:
                print("\nPlease choose a number between 1 and 2.")
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
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
