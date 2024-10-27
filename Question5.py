def print_even_value_keys(d):
    # Iterate over each key-value pair in the dictionary
    for key, value in d.items():
        # Check if the value is an even number
        if value % 2 == 0:
            print(key)  # Print the key if the value is even

# Example usage
sample_dict = {'a': 2, 'b': 3, 'c': 4}
print("Keys with even values:")
print_even_value_keys(sample_dict)
