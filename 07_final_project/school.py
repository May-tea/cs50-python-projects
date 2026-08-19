from student import Student


class School:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        self.students.remove(student)
