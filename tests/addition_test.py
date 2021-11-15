"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (3.0,4.0,5.0,6.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 18.0
