import sqlite3


my_conn = sqlite3.connect("dishes.db")
sql = "INSERT INTO RID_Counter (Counter) VALUES ('7');"
c = my_conn.cursor()
c.execute(sql)
my_conn.commit()
my_conn.close()
