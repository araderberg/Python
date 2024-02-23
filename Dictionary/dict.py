###Program Name: dict.py
###Programmer: Aaliyah Raderberg
###Project: Python Dictionary to allow users to add, remove, and search for entries in a dictionary

##This script provides a menu-driven interface where users can choose to add, remove, search for
##entries in the dictionary, or exit the application. The dictionary is maintained in memory during the program's execution.


def add_entry(dictionary):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dictionary[key] = value
    print("Entry added successfully.")

def remove_entry(dictionary):
    key = input("Enter the key of the entry to remove: ")
    if key in dictionary:
        del dictionary[key]
        print("Entry removed successfully.")
    else:
        print("Key not found in the dictionary.")

def search_entry(dictionary):
    key = input("Enter the key to search for: ")
    if key in dictionary:
        print(f"Value for key '{key}': {dictionary[key]}")
    else:
        print("Key not found in the dictionary.")

def main():
    dictionary = {}

    while True:
        print("\nDictionary Application Menu:")
        print("1. Add Entry")
        print("2. Remove Entry")
        print("3. Search Entry")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_entry(dictionary)
        elif choice == '2':
            remove_entry(dictionary)
        elif choice == '3':
            search_entry(dictionary)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
