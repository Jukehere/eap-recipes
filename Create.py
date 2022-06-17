from tkinter import *
import Recipes
import sqlite3
from sqlite3 import Error


class Create_():
    def __init__(self):
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT Counter FROM RID_Counter WHERE ID=1"
            c = my_conn.cursor()
            result = c.execute(sql)
            for re in result.fetchall():
                print(re[0])
                self.count = re[0]
                
            my_conn.close()
        except Error as e:
            print(e)
        self.insertwindow_ = Toplevel()
        basis = IntVar()
        basis2 = IntVar()
        self.insertwindow_.title("Δημιουργία συνταγής")
        nl = Label(self.insertwindow_, text = "Όνομα συνταγής")
        nl.grid(row = 0, sticky = W)
        self.ne = Entry(self.insertwindow_)
        self.ne.grid(row = 0, column = 1)
        
        tl = Label(self.insertwindow_, text = "Δυσκολία")
        tl.grid(row = 1, sticky = W)
        self.rt1 = Radiobutton(self.insertwindow_, text = "Εύκολη", value = 1, variable = basis, command = lambda : self.radiofunctionT(1))
        self.rt1.grid(row = 1, column = 1)
        self.rt2 = Radiobutton(self.insertwindow_, text = "Μέτρια", value = 2, variable = basis, command = lambda : self.radiofunctionT(2))
        self.rt2.grid(row = 1, column = 2)
        self.rt3 = Radiobutton(self.insertwindow_, text = "Δύσκολη", value = 3, variable = basis, command = lambda : self.radiofunctionT(3))
        self.rt3.grid(row = 1, column = 3)
        
        dl = Label(self.insertwindow_, text = "Κατηγορία")
        dl.grid(row = 2, sticky = W)
        self.rd1 = Radiobutton(self.insertwindow_, text = "Βασικές", value = 1, variable = basis2, command = lambda : self.radiofunctionD("Βασικές"))
        self.rd1.grid(row = 2, column = 1)
        self.rd2 = Radiobutton(self.insertwindow_, text = "Σούπες", value = 2, variable = basis2, command = lambda : self.radiofunctionD("Σούπες"))
        self.rd2.grid(row = 2, column = 2)
        self.rd3 = Radiobutton(self.insertwindow_, text = "Ζυμαρικά", value = 3, variable = basis2, command = lambda : self.radiofunctionD("Ζυμαρικά"))
        self.rd3.grid(row = 2, column = 3)
        self.rd4 = Radiobutton(self.insertwindow_, text = "Όσπρια", value = 4, variable = basis2, command = lambda : self.radiofunctionD("Όσπρια"))
        self.rd4.grid(row = 2, column = 4)
        self.rd5 = Radiobutton(self.insertwindow_, text = "Λαχανικά", value = 5, variable = basis2, command = lambda : self.radiofunctionD("Λαχανικά"))
        self.rd5.grid(row = 2, column = 5)
        self.rd6 = Radiobutton(self.insertwindow_, text = "Κρεατικά", value = 6, variable = basis2, command = lambda : self.radiofunctionD("Κρεατικά"))
        self.rd6.grid(row = 2, column = 6)
        self.rd7 = Radiobutton(self.insertwindow_, text = "Ζύμες", value = 7, variable = basis2, command = lambda : self.radiofunctionD("Ζύμες"))
        self.rd7.grid(row = 2, column = 7)
        self.rd8 = Radiobutton(self.insertwindow_, text = "Γλυκά", value = 8, variable = basis2, command = lambda : self.radiofunctionD("Γλυκά"))
        self.rd8.grid(row = 2, column = 8)
        self.rd9 = Radiobutton(self.insertwindow_, text = "Διάφορα", value = 9, variable = basis2, command = lambda : self.radiofunctionD("Διάφορα"))
        self.rd9.grid(row = 2, column = 9)

        hl = Label(self.insertwindow_, text = "Ώρες")
        hl.grid(row = 3, sticky = W)
        self.he = Entry(self.insertwindow_)
        self.he.grid(row = 3, column = 1)
        ml = Label(self.insertwindow_, text = "Λεπτά")
        ml.grid(row = 3, column = 2)
        self.me = Entry(self.insertwindow_)
        self.me.grid(row = 3, column = 3)

        al = Label(self.insertwindow_, text = "Αριθμός βημάτων")
        al.grid(row = 4, sticky = W)
        self.ae = Entry(self.insertwindow_)
        self.ae.grid(row = 4, column = 1)
                   


        self.obutton = Button(self.insertwindow_, text = "Ok", fg = "Green", command = lambda : self.submitA())
        self.obutton.grid(row = 5, column = 0)
        self.qbutton = Button(self.insertwindow_, text = "Quit", fg = "Red", command = self.insertwindow_.destroy)
        self.qbutton.grid(row = 5, sticky = E)
        
        

    def radiofunctionT(self, a):
        if a == 1:
            self.difficulty = "Εύκολο"
        elif a == 2:
            self.difficulty = "Μέτριο"
        else:
            self.difficulty = "Δύσκολο"

    def radiofunctionD(self, a):
        self.type = a
        

    def submitA(self):
        Recipes.Recipe(self.ne.get(), 4, self.count, self.type, self.difficulty, self.he.get(), self.me.get(), int(self.ae.get()))
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "INSERT INTO Recipes(RID,Name,Category,Difficulty,TimeH,TimeM,NOS) VALUES ('"+str(self.count)+"',"+"'"+self.ne.get()+"',"+"'"+self.type+"',"+"'"+self.difficulty+"',"+"'"+self.he.get()+"',"+"'"+self.me.get()+"',"+"'"+self.ae.get()+"')"
            c = my_conn.cursor()
            c.execute(sql)
            my_conn.commit()
            my_conn.close()
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "DELETE FROM RID_Counter WHERE ID=1;"
            c = my_conn.cursor()
            res = c.execute(sql)
            my_conn.commit()
            my_conn.close()
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            self.count = self.count + 1
            print(self.count)
            sql = "INSERT INTO RID_Counter (Counter) VALUES ('"+str(self.count)+"')"
            c = my_conn.cursor()
            c.execute(sql)
            my_conn.commit()
            my_conn.close()
        except Error as e:
            print(e)

        self.insertwindow_.destroy()
                                      
            
        
        

Create_()
