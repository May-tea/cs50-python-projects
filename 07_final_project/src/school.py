import statistics
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

    def edit_student(
        self, student: Student, name: str, age: int, email: str, score: float
    ) -> None:
        student.name = name
        student.age = age
        student.email = email
        student.score = score

    def sort_students_by_score(self) -> list[Student]:
        return sorted(self.students, key=lambda student: student.score, reverse=True)

    def get_average_score(self) -> float:
        if not self.students:
            return 0.0

        scores: list[float] = [student.score for student in self.students]

        return statistics.mean(scores)

    def get_students(self) -> list[Student]:
        return self.students
