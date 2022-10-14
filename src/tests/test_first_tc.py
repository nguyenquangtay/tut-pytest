
def test_add():
    assert 1 + 1 == 2


def test_multiply():
    assert 1 * 1 == 2


def test_true_is_true():
    assert True is True

# For exception case

def test_divide_zero():
    try:
        1/0
    except ZeroDivisionError as e:
        assert 'division by zero' == str(e)