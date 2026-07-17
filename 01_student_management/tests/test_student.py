from student import create_student


def test_create_student():
    student = create_student("Ali", 20, 90)

    assert student["name"] == "Ali"
    assert student["age"] == 20
    assert student["score"] == 90
