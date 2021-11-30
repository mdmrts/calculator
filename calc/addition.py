"""This is the addition calculation. Values A and B come from the Calculation class"""
# noinspection PyUnresolvedReferences,PyPackageRequirements
from calc.calculation import Calculation

class Addition(Calculation):
    """The Addition class has one method, to get the result of the calculation.
    A and B come from the Calculation parent Class"""
    def get_result(self):
        """Gets the result of the addition object"""
        return self.value_a + self.value_b
