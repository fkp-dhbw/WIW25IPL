from tkinter import *
from tkinter import ttk

def get_text():
    print(textfeld.get())

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
textfeld = ttk.Entry(frm)
textfeld.grid(column=0, row=1)
ttk.Checkbutton(frm, text="Check me!").grid(column=0, row=2)

get_btn = ttk.Button(frm, text="Get Text", command=get_text)
get_btn.grid(column=0, row=3)

btn = ttk.Button(frm, text="Quit", command=root.destroy)
btn.grid(column=0, row=4)
btn.config(text="Exit")

root.mainloop()