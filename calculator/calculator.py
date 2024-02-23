###Program Name: calculator.py
###Programmer: Aaliyah Raderberg
###Project: Python Basic Calculator

##Description: This code creates a simple calculator GUI using Tkinter with buttons for digits (0-9),
##clear button ('C'), arithmetic operators (+, -, *, /), and an equal sign (=) to compute the result.
##The calculations are performed using the eval() function, and the result is displayed in the entry widget.

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Basic Calculator")

        self.display = tk.Entry(master, width=20, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=column)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
