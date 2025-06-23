"""Entries and Functions"""

from tkinter import *

root = Tk()
root.title("Entry Basics!")
root.geometry("500x500")
root.resizable(0, 0)


# Define Functions
def make_label():
    """Print a label to the app"""
    text = Label(output_frame, text=text_entry.get(), bg="#f00", fg="#fff")
    text.pack()

    text_entry.delete(0, END)


def count_up(number):
    """Count up on the app"""
    global value

    text = Label(output_frame, text=number, bg="#f00")
    text.pack()

    value += 1


# Define Frame
input_frame = Frame(root, bg="blue", width=500, height=100)
output_frame = Frame(root, bg="#f00", width=500, height=400)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10))

# Add Input
text_entry = Entry(input_frame, width=40)
text_entry.focus()
text_entry.grid(row=0, column=0, padx=5, pady=5)
input_frame.grid_propagate(0)

print_button = Button(input_frame, text="Print!", command=make_label)
print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

# Keep outut frame size
output_frame.pack_propagate(0)

# Pass a parameter with lambda
value = 0
count_button = Button(input_frame, text="Count", command=lambda: count_up(value))
count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()
