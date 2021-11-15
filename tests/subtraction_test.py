"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    mynumbers = (10.0,4.0,3.0)
    subtraction = Subtraction(mynumbers)
    #Act
    #Assert
    assert subtraction.get_result() == -17.0
