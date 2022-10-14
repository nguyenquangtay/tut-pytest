

import pytest
from src.stuff.calculator import Calculator


def test_add_calculator():
    cal = Calculator(2, 3)
    assert cal.add() == 5


def test_divide_calculator():
    cal = Calculator(2, 2)
    assert cal.divide() == 1


class TestCalculator:

    def test_add_calculator(self):
        cal = Calculator(2, 3)
        assert cal.add() == 5

    def test_divide_calculator(self):
        cal = Calculator(2, 2)
        assert cal.divide() == 1
