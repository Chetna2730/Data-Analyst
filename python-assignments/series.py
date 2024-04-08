import pandas as pd

dataset1 = [2, 4, 6, 8, 10]
dataset2= [1, 3, 5, 7, 9]

series1 =pd.Series(dataset1)
series2 =pd.Series(dataset2)

# Addition
addition_result = series1 + series2
print("Addition:")
print(addition_result)

# Subtraction
subtraction_result = series1 - series2
print("\nSubtraction:")
print(subtraction_result)

# Multiplication
multiplication_result = series1 * series2
print("\nMultiplication:")
print(multiplication_result)

# Division
division_result = series1 / series2
print("\nDivision:")
print(division_result)
