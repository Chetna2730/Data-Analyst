#Q1:
print("\n Q1 ans:")

def generate_list_and_tuple(input_str):
    # Split the input string by commas and strip any leading or trailing spaces
    numbers = input_str.split(',')
    numbers = [number.strip() for number in numbers]

    # Convert the list of numbers into a tuple
    numbers_tuple = tuple(numbers)

    return numbers, numbers_tuple

# Sample data
input_data = input("Enter a sequence of comma-separated numbers: ")

# Generate list and tuple
result_list, result_tuple = generate_list_and_tuple(input_data)

print("List:", result_list)
print("Tuple:", result_tuple)

#Q2: . Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]
print("\nQ2 Ans:")

def display_first_and_last_colors(color_list):
    # Get the first color
    first_color = color_list[0]

    # Get the last color
    last_color = color_list[-1]

    return first_color, last_color

# Given color list
color_list = ["Red", "Green", "White", "Black"]

# Display the first and last colors
first_color, last_color = display_first_and_last_colors(color_list)

print("First color:", first_color)
print("Last color:", last_color)

#Q3. Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]

print("\nQ3 Ans:")
def print_even_numbers(input_list):
    # Initialize an empty list to store even numbers
    even_numbers = []

    # Iterate through the list
    for num in input_list:
        # Check if the number is even
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

# Sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print even numbers from the list
result = print_even_numbers(sample_list)

print("Even numbers:", result)

