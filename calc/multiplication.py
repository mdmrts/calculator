"""This is the multiplication calculation. Values A and B come from the Calculation class"""
from calc.calculation import Calculation

class Multiplication(Calculation):
    """The Multiplication class has one method, to get the result of the calculation.
    A and B come from the Calculation parent Class"""
    def get_result(self):
        """Gets the result of the multiplication object."""
        return self.value_a * self.value_b
