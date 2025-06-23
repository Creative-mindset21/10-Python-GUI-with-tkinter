"""BUTTONS AND GRID"""

from tkinter import *

# Define Window
root = Tk()
root.title("Button Basics")
root.geometry("500x500")
root.resizable(0, 0)

# Define Buttons
name_button = Button(text="Name")
name_button.grid(row=0, column=0)

time_button = Button(text="Time", bg="#0ff")
time_button.grid(row=0, column=1)

place_button = Button(text="Place", bg="#0ff", activebackground="#f00")
place_button.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

day_button = Button(text="Day", bg="black", fg="white", borderwidth=5)
day_button.grid(row=1, column=0, columnspan=3, sticky="WE")

test_1 = Button(text="test")
test_2 = Button(text="test")
test_3 = Button(text="test")
test_4 = Button(text="test")
test_5 = Button(text="test")
test_6 = Button(text="test")

test_1.grid(row=2, column=0, padx=5, pady=5)
test_2.grid(row=2, column=1, padx=5, pady=5)
test_3.grid(row=2, column=2, padx=5, pady=5, sticky="E")
test_4.grid(row=3, column=0, padx=5, pady=5)
test_5.grid(row=3, column=1, padx=5, pady=5)
test_6.grid(row=3, column=2, padx=5, pady=5, sticky="E")


root.mainloop()
