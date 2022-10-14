
import pytest
from src.stuff.calculator import Calculator


@pytest.mark.smoke
def test_add_calculator():
    cal = Calculator(2, 3)
    assert cal.add() == 5

# @pytest.mark.smoke
def test_add_calculator_failed():
    cal = Calculator(2, 3)
    assert cal.add() == 6

@pytest.mark.smoke
def test_divide_calculator():
    cal = Calculator(2, 2)
    assert cal.divide() == 1


@pytest.mark.sanity
def test_add_calculator2():
    cal = Calculator(2, 3)
    assert cal.add() == 5


@pytest.mark.sanity
def test_divide_calculator2():
    cal = Calculator(2, 2)
    assert cal.divide() == 1


class TestCalculator:

    def test_add_calculator(self):
        cal = Calculator(2, 3)
        assert cal.add() == 5

    def test_divide_calculator(self):
        cal = Calculator(2, 2)
        assert cal.divide() == 1
