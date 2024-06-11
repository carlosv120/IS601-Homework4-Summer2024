import pytest
from main import calculate_and_print 


# pylint: skip-file


@pytest.mark.parametrize("num1_string, num2_string, operation_string, expected_string", [
    ("5", "3", 'addition', "The result of 5 addition 3 is equal to 8"),
    ("10", "2", 'subtraction', "The result of 10 subtraction 2 is equal to 8"),
    ("4", "5", 'multiplication', "The result of 4 multiplication 5 is equal to 20"),
    ("20", "4", 'division', "The result of 20 division 4 is equal to 5"),
    ("1", "0", 'division', "An error occurred: Cannot divide by zero"),  
    ("9", "3", 'unknown', "Unknown operation: unknown"),  
    ("a", "3", 'addition', "Invalid number input: a or 3 is not a valid number."),  
    ("5", "b", 'subtraction', "Invalid number input: 5 or b is not a valid number.") 
])
def test_calculate_and_print(num1_string, num2_string, operation_string,expected_string, capsys):
    calculate_and_print(num1_string, num2_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
