'''Testing the actual calculator'''

from calculator import Calculator

def test_addition():
    '''Test Addition'''
    assert Calculator.addition(2, 2) == 4

def test_substraction():
    '''Test Substraction'''
    assert Calculator.subtraction(2, 2) == 0

def test_multiplication():
    '''Test Multiplication'''
    assert Calculator.multiplication(2, 2) == 4

def test_division():
    '''Test Division'''
    assert Calculator.division(2, 2) == 1
    