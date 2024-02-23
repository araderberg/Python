###Program Name: vending.py
###Programmer: Aaliyah Raderberg
###Project: Python Vending Machine

##Description: This program defines a VendingMachine class with methods to display available items,
##select an item, and process payment. When the program is run, it displays the available items,
##prompts the user to select an item, and then prompts the user to insert the payment.
##If the payment is sufficient, it calculates the change and dispenses the chosen product.
##Otherwise, it prompts the user to insert the correct amount.

class VendingMachine:
    def __init__(self):
        self.items = {
            "Coke": 2.25,
            "Snacks": 2.50,
            "Water": 1.50
        }

    def display_items(self):
        print("Available Items:")
        for item, price in self.items.items():
            print(f"{item}: ${price}")

    def select_item(self):
        selected_item = input("Enter the item you want to purchase: ")
        if selected_item in self.items:
            return selected_item
        else:
            print("Invalid item. Please select from the available items.")
            return None

    def process_payment(self, selected_item):
        item_price = self.items[selected_item]
        payment_amount = float(input(f"Insert ${item_price}: "))
        if payment_amount >= item_price:
            change = payment_amount - item_price
            print(f"Thank you for your purchase! Your change is ${change:.2f}. Enjoy your {selected_item}!")
        else:
            print("Insufficient payment. Please insert the correct amount.")

def main():
    vending_machine = VendingMachine()

    vending_machine.display_items()
    selected_item = vending_machine.select_item()
    if selected_item:
        vending_machine.process_payment(selected_item)

if __name__ == "__main__":
    main()
