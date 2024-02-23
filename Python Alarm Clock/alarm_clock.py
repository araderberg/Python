###Program Name: alarm_clock.py
###Programmer: Aaliyah Raderberg
###Project: Python Alarm Clock / Alarma

##Description: This code creates a simple GUI alarm clock where you can enter the hour, minute, second,
##and date for the alarm. When you click "Set Alarm", it calculates the time difference between the current time
##and the alarm time, and then displays a message box indicating how long until the alarm rings.

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Python Alarm Clock / Alarma")

        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.second = tk.StringVar()
        self.date = tk.StringVar()

        self.hour_label = tk.Label(master, text="Hour:")
        self.hour_label.grid(row=0, column=0)
        self.hour_entry = tk.Entry(master, textvariable=self.hour, width=2)
        self.hour_entry.grid(row=0, column=1, padx=5, pady=5)

        self.minute_label = tk.Label(master, text="Minute:")
        self.minute_label.grid(row=0, column=2)
        self.minute_entry = tk.Entry(master, textvariable=self.minute, width=2)
        self.minute_entry.grid(row=0, column=3, padx=5, pady=5)

        self.second_label = tk.Label(master, text="Second:")
        self.second_label.grid(row=0, column=4)
        self.second_entry = tk.Entry(master, textvariable=self.second, width=2)
        self.second_entry.grid(row=0, column=5, padx=5, pady=5)

        self.date_label = tk.Label(master, text="Date (dd/mm/yyyy):")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(master, textvariable=self.date, width=10)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        self.set_alarm_button = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.grid(row=1, column=2, columnspan=4, padx=5, pady=5)

    def set_alarm(self):
        try:
            hour = int(self.hour.get())
            minute = int(self.minute.get())
            second = int(self.second.get())
            date_str = self.date.get()
            alarm_time = datetime.strptime(date_str, '%d/%m/%Y').replace(hour=hour, minute=minute, second=second)
            current_time = datetime.now()
            if alarm_time < current_time:
                messagebox.showwarning("Invalid Time", "Please enter a future time.")
                return
            delta_time = alarm_time - current_time
            seconds = delta_time.total_seconds()
            messagebox.showinfo("Alarm Set", f"Alarm will ring in {seconds} seconds.")
            # Here you can implement the logic to ring the alarm when the time comes.
            # For simplicity, let's just print a message after the given seconds.
            self.master.after(int(seconds * 1000), self.ring_alarm)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for time and a valid date format.")

    def ring_alarm(self):
        messagebox.showinfo("Alarm", "Time's up! Alarm is ringing.")

def main():
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
