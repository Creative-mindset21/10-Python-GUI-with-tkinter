from tkinter import *
from tkinter import ttk

# Constants
BACKGROUND = "#c75c5c"
BUTTON_COLOR = "#f5cf87"
field_font = "Cambria, 10"

# Define the Windows
root = Tk()
root.iconbitmap("./1.2 ruler.ico")
root.resizable(0, 0)


# Define Functions
def convert():
    """Convert from one metric prefix to another"""
    metric_values = {
        "femto": 10**-15,
        "pico": 10**-12,
        "nano": 10**-9,
        "micro": 10**-6,
        "milli": 10**-3,
        "centi": 10**-2,
        "deci": 10**-1,
        "base value": 10**0,
        "deca": 10**1,
        "hecto": 10**2,
        "kilo": 10**3,
        "mega": 10**6,
        "giga": 10**9,
        "tera": 10**12,
        "peta": 10**15,
    }

    # Clear the output field
    output_quantity.delete(0, END)

    # Get all user information
    start_value = float(input_quantity.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    # Convert to the base unit first
    base_value = start_value * metric_values[start_prefix]

    # Convert to new metric vlue
    end_value = base_value / metric_values[end_prefix]

    # Update output field with answer
    output_quantity.insert(0, str(end_value))


# Define Frame
input_frame = Frame(root, bg=BACKGROUND, padx=20, pady=20)
input_frame.pack(fill=BOTH, expand=True)

# Define the Widgets
input_quantity = Entry(input_frame, width=20, font=field_font, borderwidth=3)
input_quantity.insert(0, "Enter your quantity")
equal_label = Label(input_frame, text="=", bg=BACKGROUND, font=field_font)
output_quantity = Entry(input_frame, width=20, font=field_font, borderwidth=3)

input_quantity.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=(0, 10), pady=10)
output_quantity.grid(row=0, column=2, padx=10, pady=10)

# Create combobox for metric values
metric_list = [
    "femto",
    "pico",
    "nano",
    "micro",
    "milli",
    "centi",
    "deci",
    "base value",
    "deca",
    "hecto",
    "kilo",
    "mega",
    "giga",
    "tera",
    "peta",
]

input_combobox = ttk.Combobox(
    input_frame, value=metric_list, font=field_font, justify="center"
)
output_combobox = ttk.Combobox(
    input_frame, value=metric_list, font=field_font, justify="center"
)
to_label = Label(input_frame, text="to", font=field_font, bg=BACKGROUND)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set("base value")
output_combobox.set("base value")

# Button
convert_button = Button(
    input_frame, text="Convert", font=field_font, bg=BUTTON_COLOR, command=convert
)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

# Run the Window
root.mainloop()
#
