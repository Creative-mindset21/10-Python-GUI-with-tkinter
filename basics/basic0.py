from tkinter import *


# Define Windows
windows = Tk()
windows.title("Windows Basics!")
windows.geometry("250x700")
windows.resizable(0, 0)
windows.config(bg="blue")

# Second Window
top = Toplevel()
top.title("Second Window")
top.config(bg="#123456")
top.geometry("200x200+500+500")

windows.mainloop()
