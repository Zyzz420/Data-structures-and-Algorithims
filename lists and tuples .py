def remove_duplicates(sequence):
    unique_elements = []
    for element in sequence:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


# Test the function
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
    
    
 