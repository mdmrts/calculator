"""This is the division calculation. Values A and B come from the Calculation class"""
from calc.calculation import Calculation

class Division(Calculation):
    """The Division class has one method, to get the result of the calculation.
    A and B come from the Calculation parent Class"""
    def get_result(self):
        """Gets the result of the division object"""
        if self.value_b == 0:
            return "Error, cannot divide by zero."
        return self.value_a / self.value_b
