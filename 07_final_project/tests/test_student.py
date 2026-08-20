from src.student import Student


def test_student_creation() -> None:
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    assert student.name == "Mahdiyar"
    assert student.age == 23
    assert student.email == "mahdiyar@example.com"
    assert student.score == 18.5


def test_student_str() -> None:
    student: Student = Student("Mahdiyar", 23, "mahdiyar@example.com", 18.5)

    assert str(student) == (
        "Name: Mahdiyar | Age: 23 | Email: mahdiyar@example.com | Score: 18.5"
    )
