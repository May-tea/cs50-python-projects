from src.school import School
from src.student import Student


def test_add_student() -> None:
    school: School = School()
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    school.add_student(student)

    assert student in school.students


def test_remove_student() -> None:
    school: School = School()
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    school.add_student(student)
    school.remove_student(student)

    assert student not in school.students


def test_search_student() -> None:
    school: School = School()
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    school.add_student(student)

    result = school.search_student("mahdiyar")

    assert result == [student]


def test_search_student_not_found() -> None:
    school: School = School()
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    school.add_student(student)

    result: list[Student] = school.search_student("ali")

    assert result == []


def test_edit_student() -> None:
    school: School = School()
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    school.add_student(student)

    school.edit_student(student, "Ali", 21, "ali@gmail.com", 19.5)

    assert student.name == "Ali"
    assert student.age == 21
    assert student.email == "ali@gmail.com"
    assert student.score == 19.5


def test_sort_students_by_score() -> None:
    school: School = School()

    alice: Student = Student("Alice", 20, "alice@example.com", 15.0)
    bob: Student = Student("Bob", 21, "bob@example.com", 19.0)
    charlie: Student = Student("Charlie", 22, "charlie@example.com", 17.0)

    school.add_student(alice)
    school.add_student(bob)
    school.add_student(charlie)

    result: list[Student] = school.sort_students_by_score()

    assert result == [bob, charlie, alice]


def test_sort_students_by_score_does_not_modify_original_list() -> None:
    school: School = School()

    alice: Student = Student("Alice", 20, "alice@example.com", 15.0)
    bob: Student = Student("Bob", 21, "bob@example.com", 19.0)
    charlie: Student = Student("Charlie", 22, "charlie@example.com", 17.0)

    school.add_student(alice)
    school.add_student(bob)
    school.add_student(charlie)

    school.sort_students_by_score()

    assert school.students == [alice, bob, charlie]


def test_get_average_score() -> None:
    school: School = School()

    alice: Student = Student("Alice", 20, "alice@example.com", 15.0)
    bob: Student = Student("Bob", 21, "bob@example.com", 19.0)
    charlie: Student = Student("Charlie", 22, "charlie@example.com", 17.0)

    school.add_student(alice)
    school.add_student(bob)
    school.add_student(charlie)

    result: float = school.get_average_score()

    assert result == 17.0


def test_get_average_score_with_empty_school() -> None:
    school: School = School()

    result: float = school.get_average_score()

    assert result == 0.0


def test_get_students() -> None:
    school: School = School()

    alice: Student = Student("Alice", 20, "alice@example.com", 15.0)
    bob: Student = Student("Bob", 21, "bob@example.com", 19.0)

    school.add_student(alice)
    school.add_student(bob)

    result: list[Student] = school.get_students()

    assert result == [alice, bob]


def test_get_student() -> None:
    school: School = School()

    alice: Student = Student("Alice", 20, "alice@example.com", 15.0)
    bob: Student = Student("Bob", 21, "bob@example.com", 19.0)

    school.add_student(alice)
    school.add_student(bob)

    result: Student = school.get_student(1)

    assert result == bob
