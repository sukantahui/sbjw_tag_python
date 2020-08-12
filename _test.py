from tkinter import *

root = Tk()
root.geometry("1300x500")
heading_label = Label(root, text="This is Heading").grid(row=0, column=0)


name = Entry(root, background="pink").grid(row=1, column=1)

mainloop()
