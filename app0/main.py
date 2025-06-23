from tkinter import *
from PIL import Image, ImageTk

# Define Window
root = Tk()
root.title("Hello GUI World")
root.iconbitmap("./1.3 wave.ico")
root.geometry("400x400")
root.resizable(0, 0)


# Functions
def submit_name():
    text = f"Hello {name.get()}, continue to learn tkinter"
    output_message = (
        Label(output_frame, text=text, bg=output_color, font=("Arial", 10, "bold"))
        if case_style.get() == "normal"
        else Label(
            output_frame, text=text.upper(), bg=output_color, font=("Arial", 10, "bold")
        )
    )
    output_message.pack()


# COLORS AND FONT
bg_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
text_color = "#fff"
root.config(bg=bg_color)

# Create Frames
input_frame = LabelFrame(root, bg=input_color)
output_frame = LabelFrame(root, bg=output_color)
input_frame.pack(pady=(10, 0))
output_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Define Widgets
name = Entry(input_frame, text="Enter your name", width=20)
name.focus()
submit_btn = Button(input_frame, text="Submit", command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_btn.grid(row=0, column=1, padx=10, pady=10, ipadx=20)


# Radio Buttons
case_style = StringVar(value="normal")

radio_1 = Radiobutton(
    input_frame,
    text="Normal Case",
    variable=case_style,
    bg=input_color,
    value="normal",
)
radio_2 = Radiobutton(
    input_frame,
    text="Upper Case",
    variable=case_style,
    bg=input_color,
    value="upper",
)
radio_1.grid(row=1, column=0, padx=2, pady=2)
radio_2.grid(row=1, column=1, padx=2, pady=2)

# Image
img = ImageTk.PhotoImage(Image.open("1.2 smile.png"))
img_label = Label(output_frame, image=img, bg=output_color)
img_label.pack()

# Run the Window
root.mainloop()
