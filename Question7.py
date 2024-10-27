def remove_duplicates(input_list):
    unique_list = []  # Initialize an empty list to store unique elements
    for item in input_list:
        if item not in unique_list:  # Check if item is not already in unique_list
            unique_list.append(item)  # Add the item if it's not a duplicate
    return unique_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
print("List without duplicates:", remove_duplicates(input_list))
