import pytest
from calculator import sum, subtract, multiply, divide

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-2, -3) == -5
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-2, -3) == 1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, -3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, -3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5
    assert divide(5, 0) =="Error"

#python -m pytest test_calculator.py -v

