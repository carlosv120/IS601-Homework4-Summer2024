'''Testing Calculation'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide


def test_calculation_operations(num1, num2, operation, expected):
    '''Testing failing case'''
    calc = Calculation(num1,num2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation w/ {num1} and {num2}"

def test_calculation_repr():
    '''Testing expected string'''
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ output does not match the expected str."


def test_divide_by_zero():
    '''Testing dividing by zero case'''
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
        