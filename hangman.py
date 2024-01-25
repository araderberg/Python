###Program Name: Hangman.py
###Programmer: Aaliyah Raderberg
###Class: Python Game

import random

# List of words to choose from
words = ["apple", "banana", "orange", "computer", "python", "hangman"]

# Display stages of the hangman
hangman_pics = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
           ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
           ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
           |
           ''',
    '''
      +---+
      |   |
      O   |
     /|   |
           |
           ''',
    '''
      +---+
      |   |
      O   |
     /    |
           |
           ''',
    '''
      +---+
      |   |
      O   |
           |
           |
           ''',
    '''
      +---+
      |   |
      O   |
           |
           |
           ''',
]

def pick_word():
  # Choose a random word from the list
  word = random.choice(words)
  return word.lower()

def create_display(word, letters_guessed):
  # Create a display with underscores and guessed letters
  display = ["_"] * len(word)
  for letter in letters_guessed:
    for i in range(len(word)):
      if word[i] == letter:
        display[i] = letter
  return " ".join(display)

def play():
  word = pick_word()
  letters_guessed = []
  wrong_guesses = 0

  print("Welcome to Hangman!")

  while wrong_guesses < 6 and "_" in create_display(word, letters_guessed):
    print(hangman_pics[wrong_guesses])
    display = create_display(word, letters_guessed)
    print(display)

    guess = input("Guess a letter: ").lower()

    if guess not in letters_guessed and guess not in "abcdefghijklmnopqrstuvwxyz":
      print("Invalid input. Please enter a letter that you haven't guessed yet.")
      continue

    if guess in letters_guessed:
      print("You already guessed that letter.")
      continue

    letters_guessed.append(guess)

    if guess not in word:
      wrong_guesses += 1
      print("Oops! That letter is not in the word.")

  print(hangman_pics[wrong_guesses])

  if wrong_guesses == 6:
    print("You lose! The word was", word)
  else:
    print("You win! The word was", word)

play()
