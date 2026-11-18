from calculator import add, subtract, multiply, divide
import pytest

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(5, 2) == 3

def test_multiply():
	assert multiply(4, 2) == 8

def test_divide_uneven():
	assert divide(5, 2) == 2.5

def test_divide_by_zero():
	with pytest.raises(ZeroDivisionError):
		divide(5, 0)

def test_circleArea():
        assert circleArea(-4) == "Error"

@pytest.mark.parametrize("a, b, expected", [
	(2, 3, 5), (-2, -3, -5), (0, 0, 0),
])
def test_add_many(a, b, expected):
	assert add(a, b) == expected
