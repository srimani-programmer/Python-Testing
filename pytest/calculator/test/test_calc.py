from src.calc_operations import add, sub, multiply


def test_add_pytest():
    assert add(5, 2) == 7

def test_sub_pytest():
    assert sub(5, 2) == 3

def test_multiply_pytest():
    assert multiply(5, 2) == 10
