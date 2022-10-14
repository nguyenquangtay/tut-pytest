import pytest


def test_add():
    assert 1 + 1 == 2


def test_multiply():
    assert 1 * 1 == 2


def test_true_is_true():
    assert True is True


# For exception case

def test_divide_zero():
    try:
        1 / 0
    except ZeroDivisionError as e:
        assert 'division by zero' == str(e)


# parameterize example
data = [
    (1, 1, 2),
    (2, 3, 5),
    (-2, 0, -2),
    (-1.1, 1.1, 0)
]


@pytest.mark.parametrize('num1, num2, result', data)
def test_add_param(num1, num2, result):
    assert num1 + num2 == result
