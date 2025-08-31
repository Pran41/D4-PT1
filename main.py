from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

win = Tk()
win.title("Text Editor")
win.geometry("800x600")  # More reasonable initial size
win.rowconfigure(0, weight=1)  # Simplified grid configuration
win.columnconfigure(1, weight=1)

def open_file():
    "open a file for editing"
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        win.title(f"PKS Code - {filepath}")  # Fixed typo: tittle -> title

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)  # Removed duplicate write
        win.title(f"PKS Code - {filepath}")  # Fixed typo: tittle -> title

txt_edit = Text(win)
fr_btns = Frame(win, relief=RAISED, bd=2)
btn_save = Button(fr_btns, text="Save As...", command=save_file)
btn_open = Button(fr_btns, text="Open", command=open_file)
btn_save.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open.grid(row=1, column=0, sticky="ew", padx=5)
fr_btns.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

win.mainloop()