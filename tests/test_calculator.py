'''My Calculator Test'''
from calculator import add, substract

def test_addition():
    '''Test Addition'''
    assert add(2, 2) == 4

def test_substraction():
    '''Test Substraction'''
    assert substract(2, 2) == 0
    