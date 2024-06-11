'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_operation(num1,num2,operation, expected):
    '''Testing the addition operation'''
    calculation = Calculation.create(num1, num2, operation)
    assert calculation.perform() == expected,f"{operation.__name__} Addition failed"

def test_divide_by_zero():
    '''Testing the divide by zero'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
        