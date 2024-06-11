# conftest.py
import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Generate test data
    for _ in range(num_records):
        num1 = Decimal(fake.random_number(digits=2))
        num2 = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        

        if operation_func == divide:
            num2 = Decimal('1') if num2 == Decimal('0') else num2
        
        try:
            if operation_func == divide and num2 == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(num1, num2)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield num1, num2, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):


    if {"num1", "num2", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")

        parameters = list(generate_test_data(num_records))

        modified_parameters = [(num1, num2, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for num1, num2, op_name, op_func, expected in parameters]
        metafunc.parametrize("num1, num2, operation,expected", modified_parameters)