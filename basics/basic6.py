"""IMAGES"""

from tkinter import *
from PIL import ImageTk, Image

# Define Window
root = Tk()
root.title("Image Basics")
root.iconbitmap("thinking.ico")
root.geometry("700x700")


# Define functions
def make_image():
    global cat_img

    # Using PIL for jpg
    cat_img = ImageTk.PhotoImage(Image.open("./cat.jpg"))
    cat_label = Label(root, image=cat_img)
    cat_label.pack()


# Basics...work with png
img = PhotoImage(file="shield.png")
my_label = Label(image=img)
my_label.pack()

my_button = Button(root, image=img)
my_button.pack()

# Not for jpeg
# cat_img = PhotoImage(file="./cat.jpg")
# cat_label = Label(root, image=cat_img)
# cat_label.pack()

make_image()
root.mainloop()
