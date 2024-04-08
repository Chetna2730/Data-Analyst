def concat_string(input_list):
    concatenated_string = ''.join(str(element) for element in input_list)
    return concatenated_string

# Input
sample_list = ['Hello', ' ', 'world', '!']
# Concatenate list elements into a string
result = concat_string(sample_list)

print("List:", sample_list)
print("Concatenated String:", result)
