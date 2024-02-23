###Program Name: pwd_generator.py
###Programmer: Aaliyah Raderberg
###Project: Python password generator application

##Description: This code prompts the user to specify the length of the password
##and whether they want to include lowercase letters, uppercase letters, digits,
##and special characters. Based on the user's input, it generates a random password that meets the specified criteria.

import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Pyton Password Generator!")
    print("<...Please specify the criteria for your password below...>")

    length = int(input("Enter the length of the password: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes' 
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes' 
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    if password:
        print("Your generated password is:", password)

if __name__ == "__main__":
    main()
