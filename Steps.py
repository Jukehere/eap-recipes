from tkinter import *
from Ingredients import Ingredients
import sqlite3  
from sqlite3 import Error



class Step():
    def __init__(self, title, description, noi, timeh, timem, stepno, tablename): ##noi = number of ingredients
        self.stepno = stepno
        self.title = title
        self.description = description
        self.noi = noi
        self.timeh = timeh
        self.timem = timem
        self.tn = tablename
        self.counter = 1
        self.createingredientlist()
        

    def createingredientlist(self):
        self.insertwindow = Toplevel()
        self.insertwindow.title("Υλικά βήματος " + str(self.counter))
        self.nl = []
        self.ne = []
        self.ql = []
        self.qe = []
        self.ul = []
        self.ue = []
        for i in range(self.noi):
            a = Label(self.insertwindow, text = "Ονομα υλικού")
            self.nl.append(a)
            self.nl[i].grid(row = i, sticky = W)
            b = Entry(self.insertwindow)
            self.ne.append(b)
            self.ne[i].grid(row = i, column = 1)
            c = Label(self.insertwindow, text = "Ποσότητα")
            self.ql.append(c)
            self.ql[i].grid(row = i, column = 2)
            d = Entry(self.insertwindow)
            self.qe.append(d)
            self.qe[i].grid(row = i, column = 3)
            e = Label(self.insertwindow, text = "Μονάδα μέτρησης")
            self.ul.append(e)
            self.ul[i].grid(row = i, column = 4)
            f = Entry(self.insertwindow)
            self.ue.append(f)
            self.ue[i].grid(row = i, column = 5)

        
        self.obutton = Button(self.insertwindow, text = "Ok", fg = "Green", command = lambda : self.Submit())
        self.obutton.grid(row = self.noi, column = 0)
        self.qbutton = Button(self.insertwindow, text = "Quit", fg = "Red", command = self.insertwindow.destroy)
        self.qbutton.grid(row = self.noi, column = 5)


    def Submit(self):
        if self.counter < self.stepno:
            self.counter = self.counter + 1
            for i in range(self.noi):
                Ingredients(self.ne[i].get(), self.qe[i].get(), self.ue[i].get(), self.stepno, self.tn)
            self.insertwindow.destroy()
            self.createingredientlist()
        else:
            self.insertwindow.destroy()

        

                

    








            
