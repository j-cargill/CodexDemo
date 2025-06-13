import pytest
from calculator import add, subtract, multiply, divide, calculate, main


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(4, 0)


def test_calculate():
    assert calculate(3, '+', 2) == 5
    assert calculate(3, '-', 2) == 1
    assert calculate(3, '*', 2) == 6
    assert calculate(3, '/', 2) == 1.5
    with pytest.raises(ValueError):
        calculate(3, '?', 2)


def test_main_success(capsys):
    main(['2', '+', '2'])
    captured = capsys.readouterr()
    assert 'Result: 4.0' in captured.out


def test_main_error(capsys):
    main(['2', '/', '0'])
    captured = capsys.readouterr()
    assert 'Error:' in captured.out
