from student import create_student, validate_name, validate_age, validate_score


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


def test_validate_age():
    assert validate_age(20)
    assert validate_age(1)
    assert validate_age(119)

    assert not validate_age(0)
    assert not validate_age(120)
    assert not validate_age(-5)

def test_validate_score():
    assert validate_score(90)
    assert validate_score(0)
    assert validate_score(100)

    assert not validate_score(-1)
    assert not validate_score(101)