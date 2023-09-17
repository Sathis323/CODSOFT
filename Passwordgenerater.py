import random
import string

def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting random characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")

