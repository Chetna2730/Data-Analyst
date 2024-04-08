# Q1. Write a Python program to get the volume of a sphere with radius 6.
import math

def sphere_vol(radius):
    return (4/3) * math.pi * radius**3

# Radius of the sphere
radius = 6

# Calculate the volume of the sphere
volume = sphere_vol(radius)
print("Volume of the sphere with radius {} is {:.2f}".format(radius, volume))

#2. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum hint: write User defined functions
def sum_or_triple(a, b, c):
    if a == b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c

# Test the function with sample values
num1 = 3
num2 = 3
num3 = 3

result = sum_or_triple(num1, num2, num3)
print("Result:", result)

# Q3 Write a Python program to count the number 4 in a given list.

def count(lst):
    count = 0
    for num in lst:
        if num == 4:
            count += 1
    return count

my_list = [1, 4, 6, 8, 4, 9, 4]
result = count(my_list)
print("Number of occurrences of 4 in the list:", result)

# Q4: Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence
#Sample numbers list :

#399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527

def print_even_until_237(numbers):
    for num in numbers:
        if num == 237:
            break
        elif num % 2 == 0:
            print(num)

# Sample numbers list
numbers_list = [399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
                815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
                958, 743, 527]

# Call the function with the sample numbers list
print_even_until_237(numbers_list)

#5. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
def find_numbers():
    # Initialize an empty list to store the numbers that meet the conditions
    result = []

    # Iterate through the range from 1500 to 2700 (both included)
    for num in range(1500, 2701):
        # Check if the number is divisible by 7 and a multiple of 5
        if num % 7 == 0 and num % 5 == 0:
            result.append(num)

    return result

# Call the function and store the result
numbers = find_numbers()

# Print the numbers that meet the conditions
print("Numbers between 1500 and 2700 (inclusive) that are divisible by 7 and multiples of 5:")
print(numbers)

#6. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.


for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num)

#Q7. Write a Python program to get the Fibonacci series between 0 to 50.

def fibonacci_series(limit):
    # Initialize variables to store the first two numbers of the series
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b
fibonacci_series(50)

#Q8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]

print("\nQ8 ans")
def unq_elements(input_list):
    # Convert the list to a set to remove duplicates, then convert it back to a list
    return list(set(input_list))

# Sample list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Get unique elements
unique_list = unq_elements(sample_list)

print("Sample List:", sample_list)
print("Unique List:", unique_list)




