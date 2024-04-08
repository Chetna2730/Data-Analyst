'''#QWrite a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

def concatenate_dictionaries(*dictionaries):
    # Create an empty dictionary to store the concatenated result
    concatenated_dict = {}

    # Iterate through each dictionary and update the concatenated_dict
    for dictionary in dictionaries:
        concatenated_dict.update(dictionary)

    return concatenated_dict

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
result_dict = concatenate_dictionaries(dic1, dic2, dic3)

print("Concatenated Dictionary:", result_dict)
