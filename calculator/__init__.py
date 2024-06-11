from calculator.calculation import Calculation
from calculator.calculations_history import Calculations_History
from calculator.operations import add, subtract, multiply, divide

from decimal import Decimal
from typing import Callable 

class Calculator:

    @staticmethod #Don't work on any data other than whatever is inside the method, sealed bags.
    def _perform_operation(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:

        calculation = Calculation.create(num1, num2, operation)
        Calculations_History.add_calculation(calculation)

        return calculation.perform()


    @staticmethod
    def addition(num1: Decimal,num2: Decimal) -> Decimal:

        return Calculator._perform_operation(num1,num2,add)
    
    @staticmethod
    def subtraction(num1: Decimal,num2: Decimal) -> Decimal:

        return Calculator._perform_operation(num1,num2,subtract)
    
    @staticmethod
    def multiplication(num1: Decimal,num2: Decimal) -> Decimal:

        return Calculator._perform_operation(num1,num2,multiply)

    
    @staticmethod
    def division(num1: Decimal,num2: Decimal) -> Decimal:
        
        return Calculator._perform_operation(num1,num2,divide)