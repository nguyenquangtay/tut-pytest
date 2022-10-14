import pytest
from src.stuff.calculator import Calculator


# Fixture


@pytest.fixture
def cal():
    return Calculator(3, 5)


# test

def test_add(cal):
    assert cal.add() == 8


def test_divide(cal):
    assert cal.divide() == 0.6


class TestFixture:

    # fixture
    @pytest.fixture
    def cal(self):
        return Calculator(3, 5)

    # test

    def test_add(self, cal):
        assert cal.add() == 8

    def test_divide(self, cal):
        assert cal.divide() == 0.6

