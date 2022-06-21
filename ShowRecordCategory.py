import sqlite3
from tkinter import *
from sqlite3 import Error
from Showrec import *

class SHOW_REC_CAT():
    def __init__(self,Cat):
        self.Cat = Cat
        self.Show_rec_Cat()

    def select(self,RID):
        Show_rec(RID)
        
        
    def Show_rec_Cat(self):
        insertwindow = Toplevel()
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT * FROM Recipes ;"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            listRID = []
            for i in range(len(rec)):
                babou = str(rec[i]).split(",")
                babou1 = int(babou[0].strip("("))
                babou2 = str(babou[2])
                babou3 = babou2.strip("' '")
                print(babou1)
                print(babou3)
                if babou3 == self.Cat:
                    listRID.append(babou1)

            selectbuttonlist = []
            for i in range(len(listRID)):
                try:
                    my_conn = sqlite3.connect("dishes.db")
                    sql = "SELECT Name FROM Recipes WHERE RID="+str(listRID[i])+";"
                    c = my_conn.cursor()
                    records = c.execute(sql)
                    rec = records.fetchall()
                    my_conn.close()
                    aoua2 = str(rec[0])
                    name = aoua2.strip(")").strip("(").strip(",").strip("'")
                    a = Label(insertwindow, text = name)
                    a.grid(row = i, sticky = W)
                    a = "selectbutton" + str(i)
                    selectbuttonlist.append(a)
                    selectbuttonlist[i] = Button(insertwindow, text = "Επιλογή συνταγής", fg = "Black", command = lambda : self.select(listRID[i]))
                    selectbuttonlist[i].grid(row = i, column = 1)
                    
                    
                    
                              
                except Error as e:
                    print(e)
                
                
        except Error as e:
            print(e)
    


SHOW_REC_CAT("Κρεατικά")
