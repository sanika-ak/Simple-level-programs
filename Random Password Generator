import random
import string

def gen_password(length, use_digits, use_special_chars):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    spl_chars = string.punctuation if use_special_chars else ""

    all_chars = letters + digits + spl_chars
    if length < 4:
        return "Password length must be at least 4 characters!"

    password = ''.join(random.choices(all_chars, k=length))
    return password

print("Welcome to the Random Password Generator!")
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate and display the password
    generated_password = gen_password(length, use_digits, use_special_chars)
    print("\nYour Randomly Generated Password:")
    print(generated_password)

except ValueError:
    print("Please enter a valid number for the password length.")
