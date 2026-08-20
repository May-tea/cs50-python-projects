from src.validators import validate_email, validate_name, validate_age, validate_score


def test_validate_email_with_valid_email() -> None:
    assert validate_email("mahdiyar@example.com") is True


def test_validate_email_with_invalid_email() -> None:
    assert validate_email("mahdiyarexample.com") is False


def test_validate_name_with_valid_name() -> None:
    assert validate_name("Mahdiyar") is True


def test_validate_name_with_short_name() -> None:
    assert validate_name("Ab") is False


def test_validate_name_with_invalid_characters() -> None:
    assert validate_name("Mahdiyar123") is False


def test_validate_name_with_spaces() -> None:
    assert validate_name("Mahdiyar Babaghassabha") is True


def test_validate_name_with_special_character() -> None:
    assert validate_name("Mahdiyar!") is False


def test_validate_age_with_valid_age() -> None:
    assert validate_age(23) is True


def test_validate_age_with_invalid_age() -> None:
    assert validate_age(-23) is False


def test_validate_age_with_age_above_limit() -> None:
    assert validate_age(120) is False


def test_validate_score_with_valid_score() -> None:
    assert validate_score(18.5) is True


def test_validate_score_with_below_minimum() -> None:
    assert validate_score(-1) is False


def test_validate_score_with_above_maximum() -> None:
    assert validate_score(21) is False


def test_validate_score_with_zero() -> None:
    assert validate_score(0) is True
