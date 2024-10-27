def keys_greater_than_n(d, n):
    result = []  # Initialize an empty list to store keys with values greater than n
    for key, value in d.items():
        if value > n:  # Check if the value is greater than n
            result.append(key)  # Add the key to the result list if condition is met
    return result

# Example usage
sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print("Keys with values greater than", n, ":", keys_greater_than_n(sample_dict, n))
