def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  
    return reversed_str

# Test function
input_str = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(input_str))
