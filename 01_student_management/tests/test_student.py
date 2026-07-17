from student import create_student, validate_name


def test_create_student():
    student = create_student("Ali", 20, 90)

    assert student["name"] == "Ali"
    assert student["age"] == 20
    assert student["score"] == 90

def test_validate_name():
    assert validate_name("Ali")
    assert validate_name("Ali Rezaei")
    
    assert not validate_name("A")
    assert not validate_name("Ali123")
    assert not validate_name("")
    assert not validate_name(" ")