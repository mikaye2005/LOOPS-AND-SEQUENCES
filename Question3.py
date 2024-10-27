def sum_of_list(nums):
    total = 0  # Initialize a variable to store the sum
    for num in nums:
        total += num  # Add each number in the list to the total
    return total  # Return the total sum

# Example usage
nums = [1, 2, 3, 4, 5]
print("The sum of the list is:", sum_of_list(nums))
