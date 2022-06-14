from tkinter import *
from Ingredients import Ingredients
import sqlite3  
from sqlite3 import Error



class Step():
    def __init__(self, title, description, noi, timeh, timem, stepno): ##noi = number of ingredients
        self.stepno = stepno
        self.title = title
        self.description = description
        self.noi = noi
        self.timeh = timeh
        self.timem = timem
        self.createingredientlist()

    def createingredientlist(self):
        insertwindow = Toplevel()
        insertwindow.title("Υλικά βήματος " + str(self.stepno))
        self.nl = []
        self.ne = []
        self.ql = []
        self.qe = []
        self.ul = []
        self.ue = []
        for i in range(self.noi):
            a = Label(insertwindow, text = "Ονομα υλικού")
            self.nl.append(a)
            self.nl[i].grid(row = i, sticky = W)
            b = Entry(insertwindow)
            self.ne.append(b)
            self.ne[i].grid(row = i, column = 1)
            c = Label(insertwindow, text = "Ποσότητα")
            self.ql.append(c)
            self.ql[i].grid(row = i, column = 2)
            d = Entry(insertwindow)
            self.qe.append(d)
            self.qe[i].grid(row = i, column = 3)
            e = Label(insertwindow, text = "Μονάδα μέτρησης")
            self.ul.append(e)
            self.ul[i].grid(row = i, column = 4)
            f = Entry(insertwindow)
            self.ue.append(f)
            self.ue[i].grid(row = i, column = 5)

        
        self.obutton = Button(insertwindow, text = "Ok", fg = "Green", command = lambda : self.Submit())
        self.obutton.grid(row = self.noi, column = 0)
        self.qbutton = Button(insertwindow, text = "Quit", fg = "Red", command = insertwindow.destroy)
        self.qbutton.grid(row = self.noi, column = 5)


    def Submit(self):
        loi = []
        for i in range(self.noi):
            a = Ingredients(self.ne[i].get(), self.qe[i].get(), self.ue[i].get())
            a.opprinter()
            loi.append(a)
            loi[i].opprinter()
        

                
def show_records(table):
    my_conn = None
    try: 
        my_conn = sqlite3.connect("dishes.db")
        c = my_conn.cursor()
        sql="SELECT * FROM " + table 
        records = c.execute(sql)
        for rec in records.fetchall():
            print(rec)
        my_conn.close()
    except Error as e:
        print(e)
    





show_records("Dishes")


            
