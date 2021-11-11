"""This tests the Calculator class"""
import pytest

from calculator.main import Calculator

@pytest.fixture
def clear_history():
    """Clears the history so that each test starts with a blank history"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the add method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(4, 5) == 9
    assert calc.add_numbers(3, 8) == 11
    assert calc.add_numbers(2, 7) == 9
    assert calc.add_numbers(11, 7) == 18
    assert calc.history_count() == 4
    assert calc.get_result_of_last_calculation_added_to_history() == 18


def test_clear_history(clear_history):
    """Tests that the clear history function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(4, 5) == 9
    assert calc.subtract_numbers(8, 5) == 3
    assert calc.multiply_numbers(10, 4) == 40
    assert calc.divide_numbers(6, 3) == 2
    assert calc.clear_history() is True
    assert calc.history_count() == 0

def test_count_history(clear_history):
    """Tests that the count history function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.history_count() == 0
    assert calc.add_numbers(4, 5) == 9
    assert calc.subtract_numbers(8, 5) == 3
    assert calc.history_count() == 2

def test_get_last_calculation_result(clear_history):
    """Tests that the get last result function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(4, 5) == 9
    assert calc.multiply_numbers(10, 4) == 40
    assert calc.get_result_of_last_calculation_added_to_history() == 40

def test_get_first_calculation_result(clear_history):
    """Tests that the get first result function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(4, 5) == 9
    assert calc.multiply_numbers(10, 4) == 40
    assert calc.get_result_of_first_calculation_added_to_history() == 9

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.subtract_numbers(8, 5) == 3

def test_calculator_multiply(clear_history):
    """Testing the multiply method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.multiply_numbers(10, 4) == 40

def test_calculator_divide(clear_history):
    """Testing the divide method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.divide_numbers(6, 3) == 2

def test_calculator_divide_by_zero(clear_history):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.divide_numbers(6, 0) == "Error, cannot divide by zero."

    def test_last_object(clear_history):
        """Tests the last object function for the calculator class"""
        # pylint: disable=redefined-outer-name, unused-argument
        Calculator.divide_numbers(8, 8)
        Calculator.multiply_numbers(2, 3)
        Calculator.add_numbers(2, 3)
        assert isinstance(Calculator.get_last_object(), Addition) is True
