def reverse_strings(strings):
    # Use a list comprehension to reverse each string in the input list
    reversed_list = [string[::-1] for string in strings]
    return reversed_list

# Example usage
input_list = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_strings(input_list))
