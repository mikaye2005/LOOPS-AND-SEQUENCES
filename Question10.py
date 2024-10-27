def tuples_to_dict(tuples_list):
    result_dict = {}  # Initialize an empty dictionary
    for string, number in tuples_list:  # Loop through each tuple in the list
        result_dict[string] = number  # Assign the integer to the corresponding string key
    return result_dict  # Return the resulting dictionary

# Example usage
input_tuples = [("apple", 5), ("banana", 3), ("cherry", 8)]
result = tuples_to_dict(input_tuples)
print("Resulting dictionary:", result)
