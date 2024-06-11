
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(num1, num2, operation_name):
    operation_mappings = {
        'addition': Calculator.addition,
        'subtraction': Calculator.subtraction,
        'multiplication': Calculator.multiplication,
        'division': Calculator.division
    }

    try:
        num1_decimal, num2_decimal = map(Decimal, [num1, num2])

        operation_func = operation_mappings.get(operation_name)

        if operation_func:
            result = operation_func(num1_decimal, num2_decimal)
            print(f"The result of {num1} {operation_name} {num2} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")

    except InvalidOperation:
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")

    except ZeroDivisionError:
        print("Error: Division by zero.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, num1, num2, operation = sys.argv
    calculate_and_print(num1, num2, operation)

if __name__ == '__main__':
    main()
