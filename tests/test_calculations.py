'''Testing the operations'''

from calculator.operations import add, subtract,multiply, divide

def test_addition():
    '''Test Add'''
    assert add(2, 2) == 4

def test_subtraction():
    '''Test Substract'''
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test Multiply'''
    assert multiply(2, 2) == 4

def test_division():
    '''Test Divide'''
    assert divide(2, 2) == 1
    