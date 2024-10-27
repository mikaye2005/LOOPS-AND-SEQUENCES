def find_max_in_tuple(numbers):
    max_num = numbers[0]  # Start with the first element as the initial maximum
    for num in numbers:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num

# Example usage
numbers = (10, 20, 30, 40, 50)
print("The largest number is:", find_max_in_tuple(numbers))
