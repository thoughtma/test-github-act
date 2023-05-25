from calc import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_subtract_numbers():
    assert subtract_numbers(5, 2) == 3


def test_multiply_numbers():
    assert multiply_numbers(4, 5) == 20


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(10, 0) == ZeroDivisionError