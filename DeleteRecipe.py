import sqlite3
from sqlite3 import Error


class DeleteRecipe():
    def __init__(self,RID):
        self.RID = RID
        self.Delete()

    def Delete(self):

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "SELECT Name FROM Recipes WHERE RID="+str(self.RID)+";"
            c = my_conn.cursor()
            records = c.execute(sql)
            rec = records.fetchall()
            my_conn.close()
            aoua2 = str(rec[0])
            name = aoua2.strip(")").strip("(").strip(",").strip("'")
            name = name + "_STEPS"
        except Error as e:
            print(e)
        
        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "DELETE FROM Recipes WHERE RID='"+str(self.RID)+"';"
            c = my_conn.cursor()
            rez = c.execute(sql)
            my_conn.commit()
            my_conn.close()
        except Error as e:
            print(e)

        try:
            my_conn = sqlite3.connect("dishes.db")
            sql = "DROP TABLE "+ name
            c = my_conn.cursor()
            yobane = c.execute(sql)
            my_conn.commit()
            my_conn.close()
        except Error as e:
            print(e)



