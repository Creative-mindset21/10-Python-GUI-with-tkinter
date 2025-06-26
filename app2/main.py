from tkinter import *

# Constants
BACKGROUND = "#6C1CBC"
FONT = ("Times New Roman", 12)
BUTTON_COLOR = "#E2CFF4"

# Define the Window
root = Tk()
root.title("Simple Checklist")
root.iconbitmap("./1.1 check.ico")
root.resizable(0, 0)
root.config(bg=BACKGROUND, padx=5, pady=5)


# Define Functions
def add_item():
    """Add an individual to the listbox"""
    my_list.insert(END, input_text.get())
    input_text.delete(0, END)
    input_text.focus()


def remove_item():
    """Remove the selected item fron the listbox"""
    my_list.delete(ANCHOR)


def clear_list():
    """Delete all the items from the listbox"""
    my_list.delete(0, END)


def save_list():
    """Save the list to a simple text file"""
    with open("checklist.txt", "w") as f:
        list_tuple = my_list.get(0, END)
        for item in list_tuple:
            # Take proper precautions to include only one \n for formatting purposes
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(f"{item}\n")


def open_list():
    """Open the list upon starting the program if there is one"""
    try:
        with open("checklist.txt", "r") as f:
            for line in f:
                my_list.insert(END, line)
    except:
        return


# Define the Frames
input_frame = Frame(root, bg=BACKGROUND)
text_frame = LabelFrame(root, height=50, bg=BACKGROUND)
button_frame = Frame(root, bg=BACKGROUND)

input_frame.pack()
text_frame.pack()
button_frame.pack()

# Define the Input Section
input_text = Entry(input_frame, width=35, borderwidth=3, font=FONT)
input_text.focus()
add_button = Button(input_frame, text="Add Item", font=FONT, command=add_item)

input_text.grid(row=0, column=0, pady=5, padx=5)
add_button.grid(row=0, column=1, pady=5, padx=5, ipadx=5)

# Define the text area
my_scrollbar = Scrollbar(text_frame)
my_list = Listbox(
    text_frame,
    height=15,
    width=45,
    borderwidth=3,
    font=FONT,
    yscrollcommand=my_scrollbar.set,
)
# Link scrollbar to listbox
my_scrollbar.config(command=my_list.yview)

my_list.grid(row=0, column=0, padx=5)
my_scrollbar.grid(row=0, column=1, sticky=NS)

# Button
remove_button = Button(
    button_frame,
    text="Remove Item",
    borderwidth=2,
    font=FONT,
    bg=BUTTON_COLOR,
    command=remove_item,
)
clear_button = Button(
    button_frame,
    text="Clear List",
    borderwidth=2,
    font=FONT,
    bg=BUTTON_COLOR,
    command=clear_list,
)
save_button = Button(
    button_frame,
    text="Save List",
    borderwidth=2,
    font=FONT,
    bg=BUTTON_COLOR,
    command=save_list,
)
quit_button = Button(
    button_frame,
    text="Quit",
    borderwidth=2,
    font=FONT,
    bg=BUTTON_COLOR,
    command=root.destroy,
)

remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)


# Open the previous list if available
open_list()

# Run the Window
root.mainloop()
