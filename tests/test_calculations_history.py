'''Testing the List of Calculations'''

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations_history import Calculations_History

from calculator.operations import add, subtract

# pylint: disable=redefined-outer-name,unused-argument

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""

    Calculations_History.clear_history()
    Calculations_History.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations_History.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))



def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""

    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations_History.add_calculation(calc)
    assert Calculations_History.get_latest() == calc, "Failed to add the calculation to the history"



def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""

    history = Calculations_History.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"



def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""

    Calculations_History.clear_history()
    assert len(Calculations_History.get_history()) == 0, "History was not cleared"



def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""

    latest = Calculations_History.get_latest()
    assert latest.num1 == Decimal('20') and latest.num2 == Decimal('3'), "Incorrect latest"



def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""

    add_operations = Calculations_History.find_by_operation("add")

    assert len(add_operations) == 1, "Incorrect number of calculations with add operation"
    subtract_operations = Calculations_History.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Incorrect number of calculations with subtract operation"



def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""

    Calculations_History.clear_history()
    assert Calculations_History.get_latest() is None, "Expected None for latest with empty history"
    