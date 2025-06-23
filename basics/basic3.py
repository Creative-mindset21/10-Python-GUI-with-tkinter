"""FRAMES"""

from tkinter import *

# Defind Window
root = Tk()
root.title("Frame Basic!")
root.geometry("500x500")

# name_label = Label(text="Enter your name")
# name_label.pack()
# name_button = Button(text="Submit your name")
# name_button.grid(row=0, column=1)

# Define Frames
pack_frame = Frame(bg="red")
grid_frame_1 = Frame(bg="blue")
grid_frame_2 = LabelFrame(text="Grid system rules!", borderwidth=5)

pack_frame.pack(fill=BOTH, expand=True)
grid_frame_1.pack(fill="x", expand=True)
grid_frame_2.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Pack Frame
Label(pack_frame, text="text").pack()
Label(pack_frame, text="text").pack()
Label(pack_frame, text="text").pack()

# Grd 1 layout
Label(grid_frame_1, text="text").grid(
    row=0,
    column=0,
)
Label(grid_frame_1, text="text").grid(row=1, column=1)
Label(grid_frame_1, text="text").grid(row=2, column=2)
# Label(grid_frame_1, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row=3, column=0)

# Grid 2 Layout
Label(grid_frame_2, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row=0, column=0)

root.mainloop()
