###Program Name: guess_number.py
###Programmer: Aaliyah Raderberg
###Project: Python Guess number game

def get_validated_number():
    """Prompts the user for a number until a valid integer is entered."""
    while True:
        try:
            user_input = input("Guess the number I'm thinking of: ")
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Set the correct number with a more descriptive name
secret_number = 33

# Guessing loop
while True:
    guessed_number = get_validated_number()

    if guessed_number == secret_number:
        print("Congratulations, you guessed the correct number!")
        break
    elif guessed_number < secret_number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

print("You win!")  # Move this outside the loop to print only once

