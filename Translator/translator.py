###Program Name: translator.py
###Programmer: Aaliyah Raderberg
###Project: Python Translate

##This script provides a simple command-line interface where users can enter the text they want to translate
##and specify the destination language. The program detects the language of the input text
##and then translates it into the specified destination language using the Google Translate API.
##
##You can run this script in your terminal, and it will prompt you to enter the text
##and the destination language. After translation, it will display the detected language
##and the translated text. Users can continue translating text until they choose to exit the program.

#install the googletrans library
#pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def main():
    print("Welcome to the Language Translator!")
    while True:
        text = input("Enter the text to translate: ")
        dest_language = input("Enter the destination language (e.g., 'fr' for French, 'es' for Spanish): ")

        # Perform language detection
        translator = Translator()
        detected_language = translator.detect(text).lang

        # Perform translation
        translated_text = translate_text(text, dest_language)

        print(f"\nDetected Language: {detected_language}")
        print(f"Translated Text: {translated_text}")

        choice = input("\nDo you want to translate another text? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
