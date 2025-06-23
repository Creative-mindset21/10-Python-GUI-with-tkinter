"""RADIO BUTTONS"""

from tkinter import *

root = Tk()
root.title("Radio Button Basics")
root.geometry("350x350")
root.resizable(0, 0)


# Define functions
def make_label():
    """Print to the screen"""
    num_label = (
        Label(output_frame, text="1 one 1")
        if number.get() == 1
        else Label(output_frame, text="2 two 2")
    )
    num_label.pack()


input_frame = LabelFrame(root, width=350, height=50, text="This is fun!")
output_frame = Frame(root, width=350, height=250)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10))

# Define Widgets
# Define radio buttons
number = IntVar()
number.set(1)
radio_1 = Radiobutton(
    input_frame, text="Print the number one!", variable=number, value=1
)

radio_2 = Radiobutton(
    input_frame, text="Print the number two!", variable=number, value=2
)

print_button = Button(input_frame, text="Print the number!", command=make_label)


radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()
