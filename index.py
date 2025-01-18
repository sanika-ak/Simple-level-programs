def find_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i  # Return the index of the first occurrence
    return -1  # Return -1 if the element is not found

# Test function
input_list = [10, 20, 30, 40, 50]
element_to_find = int(input("Enter an element to find its index: "))
index = find_index(input_list, element_to_find)

if index != -1:
    print(f"The element {element_to_find} is found at index {index}.")
else:
    print(f"The element {element_to_find} is not in the list.")
