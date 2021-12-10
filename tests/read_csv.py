"""Function to read CSV"""
import pandas as pd
from write_csv import write_csv

class Read():
    def read_csv(filepath):
        file = pd.read_csv(filepath)
        return write_csv(file)