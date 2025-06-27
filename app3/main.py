"""CALCULATOR PROJECT"""

from tkinter import *

# Define colors and fonts
dark_green = "#93af22"
light_green = "#acc253"
white_green = "#edefe0"
button_font = ("Arial", 18)
display_font = ("Arial", 30)

# Define the Window
root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.iconbitmap("calc.ico")
root.resizable(0, 0)


# Define the functions
def submit_number(number):
    """Add a number or decimal to the display"""
    # Insert the number or decimal pressed to the end of the display
    input_digits.insert(END, number)

    # If decimal was pressed, disable the decimal button so it cannot be pressed twice
    if "." in input_digits.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    """Store the first number of the expression and the operation to be used"""
    global first_number
    global operation

    # Get the operator pressed and the current value of the display. This is the first number in the calculation
    operation = operator
    first_number = input_digits.get()

    # Delete the value(first number) from entry display
    input_digits.delete(0, END)

    # Disable all operator buttons until equal or clear is pressed
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    # Return decimal button to normal state
    decimal_button.config(state=NORMAL)


def equal():
    """Run the store operation for two number"""
    # Perform the desired mathematics
    if operation == "add":
        value = float(first_number) + float(input_digits.get())
    elif operation == "subtract":
        value = float(first_number) - float(input_digits.get())
    elif operation == "multiply":
        value = float(first_number) * float(input_digits.get())
    elif operation == "divide":
        if input_digits.get() == 0:
            value = "ERROR"
        else:
            value = float(first_number) / float(input_digits.get())
    elif operation == "exponent":
        value = float(first_number) ** float(input_digits.get())

    # Remove the current value of the display and update it with the answer
    input_digits.delete(0, END)
    input_digits.insert(0, value)

    # Return buttons to normal states
    enable_button()


def enable_button():
    """Enable all buttons on the calculated"""
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    decimal_button.config(state=NORMAL)


def clear():
    """Clear the display"""
    input_digits.delete(0, END)

    # Return buttons to normal state
    enable_button()


def inverse():
    """Calculate the inverse of a given number."""
    # Do not allow  for 1/0
    if input_digits.get() == 0:
        value = "ERROR"
    else:
        value = 1 / float(input_digits.get())

    # Remove the current value in the display and update it with the answer
    input_digits.delete(0, END)
    input_digits.insert(0, value)


def square():
    """Calculate the square of a given number."""
    value = float(input_digits.get()) ** 2

    # Remove the current value in the display and update it with the answer
    input_digits.delete(0, END)
    input_digits.insert(0, value)


def negate():
    """Negate a given number."""
    value = -1 * float(input_digits.get())

    # Remove the current value in the display and update it with the answer
    input_digits.delete(0, END)
    input_digits.insert(0, value)


# Create the Frames
input_frame = LabelFrame(root)
digit_frame = LabelFrame(root)

input_frame.pack(padx=2, pady=(5, 20))
digit_frame.pack(padx=2, pady=5)

# Create the input
input_digits = Entry(
    input_frame,
    borderwidth=5,
    width=50,
    font=display_font,
    bg=white_green,
    justify=RIGHT,
)
input_digits.pack(padx=5, pady=5)

# The digits buttons
clear_button = Button(
    digit_frame, text="Clear", bg=dark_green, font=button_font, command=clear
)
quit_button = Button(
    digit_frame, text="Quit", bg=dark_green, font=button_font, command=root.destroy
)

clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")

inverse_button = Button(
    digit_frame, text="1/x", bg=light_green, font=button_font, command=inverse
)
square_button = Button(
    digit_frame, text="x^2", bg=light_green, font=button_font, command=square
)
exponent_button = Button(
    digit_frame,
    text="x^n",
    bg=light_green,
    font=button_font,
    command=lambda: operate("exponent"),
)
divide_button = Button(
    digit_frame,
    text="/",
    bg=light_green,
    font=button_font,
    command=lambda: operate("divide"),
)

inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")

number7 = Button(
    digit_frame,
    text="7",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(7),
)
number8 = Button(
    digit_frame,
    text="8",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(8),
)
number9 = Button(
    digit_frame,
    text="9",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(9),
)
multiply_button = Button(
    digit_frame,
    text="*",
    bg=light_green,
    font=button_font,
    command=lambda: operate("multiply"),
)

number7.grid(row=2, column=0, sticky="WE", pady=1, ipadx=20)
number8.grid(row=2, column=1, sticky="WE", pady=1, ipadx=20)
number9.grid(row=2, column=2, sticky="WE", pady=1, ipadx=20)
multiply_button.grid(row=2, column=3, sticky="WE", pady=1, ipadx=20)

number4 = Button(
    digit_frame,
    text="4",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(4),
)
number5 = Button(
    digit_frame,
    text="5",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(5),
)
number6 = Button(
    digit_frame,
    text="6",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(6),
)
subtract_button = Button(
    digit_frame,
    text="-",
    bg=light_green,
    font=button_font,
    command=lambda: operate("subtract"),
)

number4.grid(row=3, column=0, sticky="WE", pady=1)
number5.grid(row=3, column=1, sticky="WE", pady=1)
number6.grid(row=3, column=2, sticky="WE", pady=1)
subtract_button.grid(row=3, column=3, sticky="WE", pady=1)

number1 = Button(
    digit_frame,
    text="1",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(1),
)
number2 = Button(
    digit_frame,
    text="2",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(2),
)
number3 = Button(
    digit_frame,
    text="3",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(3),
)
add_button = Button(
    digit_frame,
    text="+",
    bg=light_green,
    font=button_font,
    command=lambda: operate("add"),
)

number1.grid(row=4, column=0, sticky="WE", pady=1)
number2.grid(row=4, column=1, sticky="WE", pady=1)
number3.grid(row=4, column=2, sticky="WE", pady=1)
add_button.grid(row=4, column=3, sticky="WE", pady=1)

negate_button = Button(
    digit_frame, text="+/-", bg="#000", fg="#fff", font=button_font, command=negate
)
number0 = Button(
    digit_frame,
    text="0",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number(0),
)
decimal_button = Button(
    digit_frame,
    text=".",
    bg="#000",
    fg="#fff",
    font=button_font,
    command=lambda: submit_number("."),
)
equal_button = Button(
    digit_frame, text="=", bg=dark_green, font=button_font, command=equal
)

negate_button.grid(row=5, column=0, sticky="WE", pady=1)
number0.grid(row=5, column=1, sticky="WE", pady=1)
decimal_button.grid(row=5, column=2, sticky="WE", pady=1)
equal_button.grid(row=5, column=3, sticky="WE", pady=1)


# Run the Window
root.mainloop()
