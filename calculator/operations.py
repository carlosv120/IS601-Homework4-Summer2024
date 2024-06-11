from decimal import Decimal

def add(num1:Decimal, num2:Decimal)-> Decimal:
    return num1 + num2

def subtract(num1:Decimal, num2:Decimal)-> Decimal:
    return num1 - num2

def multiply(num1:Decimal, num2:Decimal)-> Decimal:
    return num1 * num2

def divide(num1: Decimal, num2: Decimal) -> Decimal:
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2