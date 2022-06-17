import Steps
from tkinter import *
import sqlite3
from sqlite3 import Error

class Recipe():
    def __init__(self, name, user, RID, category, difficulty, timeh, timem, nos):
        self.name = name
        self.user = user
        self.RID = RID
        self.category = category
        self.timeh = timeh
        self.timem = timem
        self.nos = nos
        self.difficulty = difficulty
        self.createsteps()

    def createsteps(self):
        self.insertwindow2 = Toplevel()
        self.insertwindow2.title("Δημιουργία Βημάτων")
        self.nl = []
        self.ne = []
        self.ql = []
        self.qe = []
        self.dl = []
        self.de = []
        self.ml = []
        self.me = []
        self.ol = []
        self.oe = []
        for i in range(self.nos):
            a = Label(self.insertwindow2, text = "Τίτλος βήματος")
            self.nl.append(a)
            self.nl[i].grid(row = i, sticky = W)
            b = Entry(self.insertwindow2)
            self.ne.append(b)
            self.ne[i].grid(row = i, column = 1)
            c = Label(self.insertwindow2, text = "Περιγραφή")
            self.ql.append(c)
            self.ql[i].grid(row = i, column = 2)
            d = Entry(self.insertwindow2)
            self.qe.append(d)
            self.qe[i].grid(row = i, column = 3)
            e = Label(self.insertwindow2, text = "Χρόνος σε ώρες")
            self.dl.append(e)
            self.dl[i].grid(row = i, column = 4)
            f = Entry(self.insertwindow2)
            self.de.append(f)
            self.de[i].grid(row = i, column = 5)
            g = Label(self.insertwindow2, text = "Χρόνος σε λεπτά")
            self.ml.append(g)
            self.ml[i].grid(row = i, column = 6)
            h = Entry(self.insertwindow2)
            self.me.append(h)
            self.me[i].grid(row = i, column = 7)
            j = Label(self.insertwindow2, text = "Αριθμός υλικών")
            self.ol.append(j)
            self.ol[i].grid(row = i, column = 8)
            k = Entry(self.insertwindow2)
            self.oe.append(k)
            self.oe[i].grid(row = i, column = 9)         

        
        self.obutton = Button(self.insertwindow2, text = "Ok", fg = "Green", command = lambda : self.Submit_())
        self.obutton.grid(row = self.nos, column = 0)
        self.qbutton = Button(self.insertwindow2, text = "Quit", fg = "Red", command = self.insertwindow2.destroy)
        self.qbutton.grid(row = self.nos, column = 5)

    def Submit_(self):
        tn = self.name + "_STEPS"
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "CREATE TABLE " + tn+ " (SN INTEGER PRIMARY KEY , TITLE VARCHAR(128), DESCRIPTION VARCHAR(128),INGREDIENTS VARCHAR(128),INGQ VARCHAR(128),INGU VARCHAR (128),TIMEH INTEGER,TIMEM INTEGER)"
            print(sql)
            c = my_conn.cursor()
            c.execute(sql)
            my_conn.close()
        except Error as e:
            print(e)

        for i in range(self.nos):
            a = Steps.Step(self.me[i].get(), self.qe[i].get(), int(self.oe[i].get()), self.de[i].get(), self.me[i].get(), i + 1, tn)
            my_conn = None
            j = i + 1
            try:
                my_conn = sqlite3.connect("dishes.db")
                sql = "INSERT INTO " + tn+ " (SN, TITLE, DESCRIPTION, TIMEH, TIMEM) VALUES ('"+str(j)+"',"+"'"+self.ne[i].get()+"',"+"'"+self.qe[i].get()+"',"+"'"+self.de[i].get()+"',"+"'"+self.me[i].get()+"')"
                c = my_conn.cursor()
                c.execute(sql)
                my_conn.commit()
                my_conn.close()
            except Error as e:
                print(e)
                
        
        self.insertwindow2.destroy()
             

  



        

    
