from tkinter import *
# creating a window
from tkinter import messagebox
from src.Models import *
from src.KNNCore import *
from src.DataProvider import *
from tkinter.messagebox import showinfo

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

new_p = None
def popupmsg():
    global new_p
    new_p = Product(e1.get(), e2.get(), "", {"ecran": e3.get(), "os": e4.get(), "cpu": e5.get(),
                                             "memory": e6.get(), "ram": e7.get(), "reseau": e8.get(),
                                             "batterie": e9.get(),
                                             "cam": e10.get()})
    datatrain = readData()
    t = knnModel(datatrain, new_p, 5).upper()
    new_p.type=t
    messagebox.showinfo("This Product is a", t)


# ******************************
window = Tk()
window.title("IAD Project")

window.geometry("1260x500")  # You want the size of the app to be 500x500
window.resizable(0, 0)  # Don't allow resizing in the x or y direction


# creating a menu bar
def alert():
    global new_p
    showinfo("alertedf",  new_p.type)


menubar = Menu(window)

# creatinf a menu
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Import", command=alert)
menu1.add_command(label="Export", command=alert)
menu1.add_separator()
menu1.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Edit", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About", command=alert)
menubar.add_cascade(label="Help", menu=menu3)

window.config(menu=menubar)
# frame 1
f1 = LabelFrame(window, text="New Product input", padx=5, pady=20, width=800)
f1.grid(columnspan=9, row=0, column=0)
f1.pack(fill="both", expand="yes")
lf1 = Label(f1, text="Please put  the requested values:")
lf1.grid(columnspan=9, row=0, column=0, pady=20, sticky="w")

le1 = Label(f1, text="Name:")
le2 = Label(f1, text="Producer:")
le3 = Label(f1, text="Screen:")
le4 = Label(f1, text="OS:")
le5 = Label(f1, text="CPU:")
le6 = Label(f1, text="Memory:")
le7 = Label(f1, text="RAM:")
le8 = Label(f1, text="Network:")
le9 = Label(f1, text="Energy:")
le10 = Label(f1, text="CAM:")

e1 = Entry(f1)
e2 = Entry(f1)
e3 = Entry(f1)
e4 = Entry(f1)
e5 = Entry(f1)
e6 = Entry(f1)
e7 = Entry(f1)
e8 = Entry(f1)
e9 = Entry(f1)
e10 = Entry(f1)
le1.grid(row=1, column=0)
le2.grid(row=1, column=1)
le3.grid(row=1, column=2)
le4.grid(row=1, column=3)
le5.grid(row=1, column=4)
le6.grid(row=1, column=5)
le7.grid(row=1, column=6)
le8.grid(row=1, column=7)
le9.grid(row=1, column=8)
le10.grid(row=1, column=9)
e1.grid(row=2, column=0)
e2.grid(row=2, column=1)
e3.grid(row=2, column=2)
e4.grid(row=2, column=3)
e5.grid(row=2, column=4)
e6.grid(row=2, column=5)
e7.grid(row=2, column=6)
e8.grid(row=2, column=7)
e9.grid(row=2, column=8)
e10.grid(row=2, column=9)

b1 = Button(f1, text='Guess', command=lambda: popupmsg(), height=2, width=20).grid(row=4, column=0,
                                                                                   pady=50)
b2 = Button(f1, text='Save to dataset', command=lambda: alert(), height=2, width=20).grid(row=4, column=8,
                                                                                             pady=50)

window.mainloop()
