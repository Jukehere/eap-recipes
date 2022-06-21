from tkinter import *
import sqlite3
from sqlite3 import Error
import DeleteRecipe as DR


class Show_rec():
    def __init__(self,RID):
        self.RID = RID
        self.index = 1
        self.timeE = 0
        self.Show_rec_RID()
        

    
            
    def Show_rec_RID(self):
        self.insertwindow = Tk()
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT Name FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            self.name = aoua2.strip(")").strip("(").strip(",").strip("'")
            self.name = self.name + "_STEPS"
            self.insertwindow.title(self.name)
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
            a = Label(self.insertwindow, text = "Κατηγορία :  " + self.cat)
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
            a = Label(self.insertwindow, text = "Δυσκολία :  " + self.dif)
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
            a = Label(self.insertwindow, text = "Χρόνος :  " + self.timeH + " Ώρες και")
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
            self.timeT = (int(self.timeH) * 60) + int(self.timeM)
            a = Label(self.insertwindow, text = self.timeM + "  λεπτά.")
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
            a = Label(self.insertwindow, text = "Αριθμός βημάτων :  " + self.nos)
            a.grid(row = 3, sticky = W)
        except Error as e:
            print(e)


        self.obutton = Button(self.insertwindow, text = "Εκτέλεση συνταγής", fg = "Green", command = lambda : self.run())
        self.obutton.grid(row = 4, sticky = W)
        self.dbutton = Button(self.insertwindow, text = "Διαγραφή συνταγής", fg = "Red", command = lambda : self.deleterecipe())
        self.dbutton.grid(row = 4, column = 1)
        self.qbutton = Button(self.insertwindow, text = "Έξοδος", fg = "Red", command =  self.insertwindow.destroy)
        self.qbutton.grid(row = 4, column = 2)

    def run(self):
        self.yoves = "insertwindow" + str(self.index)
        self.yove = "Βήμα Νο" + str(self.index)
        self.yoves = Tk()
        self.yoves.title(str(self.yove))
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT TITLE FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            a = Label(self.yoves, text = "Τίτλος  :  " + yobane)
            a.grid(row = 0, sticky = W)
                          
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT DESCRIPTION FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            a = Label(self.yoves, text = "Περιγραφή  :  " + yobane)
            a.grid(row = 1, sticky = W)
                          
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT TIMEH FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            self.timeSH = int(yobane)
            a = Label(self.yoves, text = "Χρόνος  :  " + yobane + " ώρες και")
            a.grid(row = 2, sticky = W)
                          
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT TIMEM FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            self.timeSM = int(yobane)
            a = Label(self.yoves, text = yobane + " λεπτά.")
            a.grid(row = 2, column = 1)
                          
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT INGREDIENTS FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            print(yobane)
            yoves = yobane.split(",")
            a = []
            self.ababa = len(yoves)
            for i in range(len(yoves) - 1):
                print(i)
                print(yoves[i])
                b = Label(self.yoves, text = "Υλικό Νο  " + str(i + 1) + "     " +  str(yoves[i]))
                a.append(b)
                a[i].grid(row = 3 + i, sticky = W)                   
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT INGQ FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            print(yobane)
            lmao = yobane.split(",")
            a = []
            b = []
            for i in range(len(lmao) - 1):
                print(i)
                bee = Label(self.yoves, text = "Ποσότητα:  ")
                a.append(bee)
                a[i].grid(row = 3 + i, column = 1)
                bee = Label(self.yoves, text = str(lmao[i]))
                b.append(bee)
                b[i].grid(row = 3 + i, column = 2)
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT INGU FROM "+self.name+" WHERE SN="+str(self.index)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            yobane = str(rec[0]).strip("[").strip("]").strip("(").strip(")").strip(",").strip("'")
            print(yobane)
            yoves = yobane.split(",")
            a = []
            for i in range(len(yoves) - 1):
                print(yoves[i])
                b = Label(self.yoves, text = "Μονάδα μέτρησης  :  "  +  str(yoves[i]))
                a.append(b)
                a[i].grid(row = 3 + i, column = 3)                   
        except Error as e:
            print(e)

        
    
        self.timeS = self.timeSH * 60 + self.timeSM
        progress = round((self.timeE / self.timeT) * 100, 1)
        self.timeE = self.timeE + self.timeS
        b = Label(self.yoves, text = str(progress) + "  % έχει ολοκληρωθεί απο τη συνταγή !")
        b.grid(row = 4 + self.ababa, sticky = W)
        self.nextbutton = Button(self.yoves, text = "Επόμενο βήμα", fg = "Green", command = lambda : self.next())
        self.nextbutton.grid(row = 5 + self.ababa, sticky = W)
            
       

                
            

    def deleterecipe(self):
        DR.DeleteRecipe(self.RID)
        self.insertwindow.destroy()




    def next(self):
        self.yoves.destroy()
        if int(self.index) < int(self.nos):
            self.index = int(self.index) + 1
            self.run()
        else:
            self.yoves = "completewindow"
            self.yoves = Tk()
            self.yoves.title("Τέλος Συνταγής")
            a = Label(self.yoves, text = " Η Συνταγή Ολοκληρώθηκε ! ")
            a.grid(row = 1, sticky = W)
            self.endbutton = Button(self.yoves, text = "Τέλος", fg = "Black", command = lambda : self.yoves.destroy())
            self.endbutton.grid(row = 2, sticky = W)
            self.insertwindow.destroy()
           


