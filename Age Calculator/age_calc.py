###Program Name: age_calc.py
###Programmer: Aaliyah Raderberg
###Project: Python Age Calculator GUI

##Description: This code creates a simple GUI where the user can input their name
##and date of birth (in the format mm/dd/yyyy). When the user clicks the "Calculate Age" button,
##it calculates the age based on the input date of birth and displays the result below the button.
##If the user enters an invalid date of birth, it displays an error message prompting
##them to enter a valid date of birth.

import tkinter as tk
from datetime import datetime

class AgeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Age Calculator")

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.dob_label = tk.Label(master, text="Date of Birth (mm/dd/yyyy):")
        self.dob_label.grid(row=1, column=0, padx=5, pady=5)
        self.dob_entry = tk.Entry(master)
        self.dob_entry.grid(row=1, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(master, text="Calculate Age", command=self.calculate_age)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.output_label = tk.Label(master, text="")
        self.output_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def calculate_age(self):
        name = self.name_entry.get()
        dob_str = self.dob_entry.get()

        try:
            dob = datetime.strptime(dob_str, "%m/%d/%Y")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            self.output_label.config(text=f"{name}'s age is {age} years.")
        except ValueError:
            self.output_label.config(text="Please enter a valid date of birth in format mm/dd/yyyy.")

def main():
    root = tk.Tk()
    age_calculator = AgeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
