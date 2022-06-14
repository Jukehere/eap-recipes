from tkinter import *
import sqlite3
from sqlite3 import Error



class Show_rec():
    def __init__(self,RID):
        self.RID = RID
        self.Show_rec_RID()

    
            
    def Show_rec_RID(self):
        insertwindow = Toplevel()
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT Name FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            self.name = aoua2.strip(")").strip("(").strip(",").strip("'")
            insertwindow.title(self.name)
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT Category FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            self.cat = aoua2.strip(")").strip("(").strip(",").strip("'")
            a = Label(insertwindow, text = "Κατηγορία :  " + self.cat)
            a.grid(row = 0, sticky = W)
        except Error as e:
            print(e)


        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT Difficulty FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            self.dif = aoua2.strip(")").strip("(").strip(",").strip("'")
            a = Label(insertwindow, text = "Δυσκολία :  " + self.dif)
            a.grid(row = 1, sticky = W)
        except Error as e:
            print(e)


        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT TimeH FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            self.timeH = aoua2.strip(")").strip("(").strip(",").strip("'")
            a = Label(insertwindow, text = "Χρόνος :  " + self.timeH + " Ώρες και")
            a.grid(row = 2, sticky = W)
        except Error as e:
            print(e)


        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT TimeM FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            self.timeM = aoua2.strip(")").strip("(").strip(",").strip("'")
            a = Label(insertwindow, text = self.timeM + "  λεπτά.")
            a.grid(row = 2, column = 1)
        except Error as e:
            print(e)


        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT NOS FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            aoua = str(rec[0])
            self.nos = aoua.strip(")").strip("(").strip(",")
            my_conn.close()
            a = Label(insertwindow, text = "Αριθμός βημάτων :  " + self.nos)
            a.grid(row = 3, sticky = W)
        except Error as e:
            print(e)


        self.obutton = Button(insertwindow, text = "Εκτέλεση συνταγής", fg = "Green", command = lambda : self.run())
        self.obutton.grid(row = 4, sticky = W)
        self.dbutton = Button(insertwindow, text = "Διαγραφή συνταγής", fg = "Red", command = lambda : self.deleterecipe())
        self.dbutton.grid(row = 4, column = 1)
        self.qbutton = Button(insertwindow, text = "Έξοδος", fg = "Red", command =  insertwindow.destroy)
        self.qbutton.grid(row = 4, column = 2)

    def run(self):
        self.name = self.name + "_STEPS"
        self.timeE = 0
        self.timeT = (int(self.timeH) * 60) + int(self.timeM)
        for i in range(int(self.nos)):
            self.next = False
            yoves = "insertwindow" + str(i + 1)
            yove = "Βήμα Νο" + str(i + 1)
            yoves = Toplevel()
            yoves.title(str(yove))
            try:
                my_conn = sqlite3.connect("dishes.db")
                sql = "SELECT TITLE FROM "+self.name+" WHERE SN="+str(i + 1)+";"
                c = my_conn.cursor()
                records = c.execute(sql)
                rec = records.fetchall()
                my_conn.close()
                yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
                a = Label(yoves, text = "Τίτλος  :  " + yobane)
                a.grid(row = 0, sticky = W)
                          
            except Error as e:
                print(e)

            try:
                my_conn = sqlite3.connect("dishes.db")
                sql = "SELECT DESCRIPTION FROM "+self.name+" WHERE SN="+str(i + 1)+";"
                c = my_conn.cursor()
                records = c.execute(sql)
                rec = records.fetchall()
                my_conn.close()
                yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
                a = Label(yoves, text = "Περιγραφή  :  " + yobane)
                a.grid(row = 1, sticky = W)
                          
            except Error as e:
                print(e)

            try:
                my_conn = sqlite3.connect("dishes.db")
                sql = "SELECT TIMEH FROM "+self.name+" WHERE SN="+str(i + 1)+";"
                c = my_conn.cursor()
                records = c.execute(sql)
                rec = records.fetchall()
                my_conn.close()
                yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
                self.timeSH = int(yobane)
                a = Label(yoves, text = "Χρόνος  :  " + yobane + " ώρες και")
                a.grid(row = 2, sticky = W)
                          
            except Error as e:
                print(e)

            try:
                my_conn = sqlite3.connect("dishes.db")
                sql = "SELECT TIMEM FROM "+self.name+" WHERE SN="+str(i + 1)+";"
                c = my_conn.cursor()
                records = c.execute(sql)
                rec = records.fetchall()
                my_conn.close()
                yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
                self.timeSM = int(yobane)
                a = Label(yoves, text = yobane + "λεπτά.")
                a.grid(row = 2, column = 1)
                          
            except Error as e:
                print(e)

                
            self.timeS = self.timeSH * 60 + self.timeSM
            progress = round((self.timeE / self.timeT) * 100, 1)
            self.timeE = self.timeE + self.timeS
            b = Label(yoves, text = str(progress) + "  % έχει ολοκληρωθεί απο τη συνταγή !")
            b.grid(row = 3, sticky = W)
            self.nextbutton = Button(yoves, text = "Επόμενο βήμα", fg = "Green", command = lambda : self.next())
            self.nextbutton.grid(row = 4, sticky = W)
            
            

                
            

    def deleterecipe(self):
        
        return

    def next(self):
        self.next = True
        return

Show_rec(22)

