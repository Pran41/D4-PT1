from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main")

def topwin():
    top = Toplevel()
    top.geometry("1800x100")
    top.title("Top Window")
    12 = Label(top, text="This is a top level window")
    12.pack()

    top.mainloop()    


l = Label(root, text="This is root window")
btn = Button(root, text="Open Top Window", command=topwin())

l.pack()
btn.pack()