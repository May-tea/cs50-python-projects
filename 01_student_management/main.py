def delete_student(students):
    if not students:
        print("\nStudents list is empty.")
        return
    
    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']}")
        
    choice = int(input("Which student do you want to delete? "))
    
    deleted_student = students.pop(choice - 1)
    
    print(f"{deleted_student['name']} has been deleted.")       


def search_student(students):
    if not students:
        print("\nStudents list is empty.")
        return

    search_query = input("Search by name: ")

    for student in students:
        if search_query.lower() in student["name"].lower():
            print(
                f"Name: {student['name']}, "
                f"Age: {student['age']}, "
                f"Score: {student['score']}"
            )
            return

    print("Student not found.")


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
    students = []
    
    while True:
        choice = int(
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
                students = add_student()
            case 2:
                show_students(students)
            case 3:
                search_student(students)
            case 4:
                delete_student(students)
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Please select a number between 1 and 5.")


main()
