def has_pair_with_sum(numbers, target_sum):
    seen = set()  # Initialize an empty set to store numbers we have seen so far
    for num in numbers:
        complement = target_sum - num  # Calculate the complement of the current number
        if complement in seen:  # Check if the complement is in the set
            return True  # If found, we have a pair that sums to target_sum
        seen.add(num)  # Add the current number to the set
    return False  # Return False if no such pair exists

# Example usage
numbers = [2, 7, 11, 15]
target_sum = 9
print("Pair found:", has_pair_with_sum(numbers, target_sum))
