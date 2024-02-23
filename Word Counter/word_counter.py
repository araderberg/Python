###Program Name: word_counter.py
###Programmer: Aaliyah Raderberg
###Project: Python Word Counter app

##This script prompts the user to enter some text. It then analyzes the text,
##calculates the frequency of each word, and prints out the word frequency
##along with the total number of words and unique words in the text.
##
##You can use this Word Counter application to analyze any text input
##and gain insights into word frequencies and other statistics.

import string

def word_counter(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split text into words
    words = text.split()

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Calculate total words and unique words
    total_words = len(words)
    unique_words = len(word_freq)

    return word_freq, total_words, unique_words

def main():
    text = input("Enter the text to analyze: ")

    word_freq, total_words, unique_words = word_counter(text)

    print("\nWord Frequency:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

    print("\nTotal Words:", total_words)
    print("Unique Words:", unique_words)

if __name__ == "__main__":
    main()
