"""Testing File for CSV Functionality"""
import pandas as pd

file = pd.read_csv('csv_tests/addition.csv')

for index, row in file.iterrows():
    mynumbers = (row['value_1'], row['value_2'])
    print(mynumbers)
