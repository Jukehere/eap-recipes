import sqlite3
from sqlite3 import Error


class Ingredients():
    def __init__(self, name, quantity, unit, sn, tn):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.sn = sn
        self.tn = tn
        self.Saveingredients()


    def Saveingredients(self):

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT INGREDIENTS FROM "+str(self.tn)+" WHERE SN="+str(self.sn)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            yobane = str(rec[0]).strip('(').strip(')').strip("'").strip("None").strip(',')
            print(yobane)
            self.name = self.name + "," + yobane
            self.name = self.name.strip("'")
            print(self.name)    
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT INGQ FROM "+str(self.tn)+" WHERE SN="+str(self.sn)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            yobane = str(rec[0]).strip('(').strip(')').strip("'").strip("None").strip(',')
            print(yobane)
            self.quantity = self.quantity + "," + yobane
            self.quantity = self.quantity.strip("'")
            print(self.quantity)    
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT INGU FROM "+str(self.tn)+" WHERE SN="+str(self.sn)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            yobane = str(rec[0]).strip('(').strip(')').strip("'").strip("None").strip(',')
            print(yobane)
            self.unit = self.unit + "," + yobane
            self.unit = self.unit.strip("'")
            print(self.unit)    
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "UPDATE "+ self.tn +" SET INGREDIENTS = '"+str(self.name)+"', INGQ = '"+str(self.quantity)+"', INGU = '"+str(self.unit)+"' WHERE SN="+str(self.sn)+";"
            c = my_conn.cursor()
            c.execute(sql)
            my_conn.commit()
            my_conn.close()
        except Error as e:
            print(e)

        

