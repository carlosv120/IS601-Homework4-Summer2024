from decimal import Decimal
from typing import Callable


class Calculation:
    def __init__(self, num1: Decimal, num2:Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    @staticmethod    
    def create(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(num1, num2, operation)

    def perform(self) -> Decimal:
        return self.operation(self.num1,self.num2)
    
    def __repr__(self):
        return f"Calculation({self.num1}, {self.num2}, {self.operation.__name__})"