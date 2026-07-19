import pytest

from main import calculate, DivisionByZeroError, InvalidOperatorError


def test_addition():
    assert calculate(10, 2, "+") == 12
    
def test_subtraction():
    assert calculate(8, 4, "-") == 4
    
def test_multiplication():
    assert calculate(5, 3, "*") == 15
    
def test_division():
    assert calculate(6, 2, "/") == 3

def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate(5, 0, "/")
        
def test_invalid_operator():
    with pytest.raises(InvalidOperatorError):
        calculate(5, 3, "&")