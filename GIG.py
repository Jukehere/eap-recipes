from tkinter import *
import ShowRec as SR


insertwindow = Toplevel()
a = Label(insertwindow, text = "RID")
a.grid(row = 1, sticky = W)
b = Entry(insertwindow)
b.grid(row = 1, column = 1)
okbutton = Button(insertwindow, text = "Ok", command = lambda : ok())
okbutton.grid(row = 2, sticky = W)
def ok ():
    re = b.get()
    SR.Show_rec(int(re))
    

