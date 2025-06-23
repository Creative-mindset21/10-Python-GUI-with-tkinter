from tkinter import *

# Define Window
window = Tk()
window.title("Label Basics!")
window.geometry("400x400")
window.resizable(0, 0)
window.config(bg="blue")

# Create widgets
name_label_1 = Label(text="My name is King")
name_label_1.pack()

name_label_2 = Label(text="Hello, my name is John", font=("Arial", 18, "bold"))
name_label_2.pack()

name_label_3 = Label(text="Hello, my name is Paul.", font=("Cambria", 10), bg="#f00")
name_label_3.pack(padx=10, pady=50)

name_label_4 = Label(text="Hello, my name is Sue", bg="#000", fg="green")
name_label_4.pack(pady=(0, 10), ipadx=50, ipady=10, anchor="w")

name_label_5 = Label(text="Hello, my name is Pat", bg="#fff", fg="#123456")
name_label_5.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Run the window
window.mainloop()
