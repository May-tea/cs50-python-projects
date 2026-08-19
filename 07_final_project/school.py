from student import Student


class School:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        self.students.remove(student)

    def search_student(self, query: str) -> list[Student]:
        found_students: list[Student] = []

        for student in self.students:
            if query.lower() in student.name.lower():
                found_students.append(student)

        return found_students
