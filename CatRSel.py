import sqlite3
from tkinter import *
from tkinter import messagebox
import Showrec as SR



def maincatrsel():
    def ok ():
        connection = sqlite3.connect('dishes.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Recipes WHERE RID = ?',(b.get(),))
        curcheck = cursor.fetchone()
        if curcheck != None:
            re = b.get()
            insertwindow.destroy()
            SR.Show_rec(int(re))
        if curcheck == None:
            messagebox.showerror("Error" , "Το RID δεν βρέθηκε, προσπάθησε ξανά." , parent = insertwindow)
    insertwindow = Toplevel()
    a = Label(insertwindow, text = "RID")
    a.grid(row = 1, sticky = W)
    b = Entry(insertwindow)
    b.grid(row = 1, column = 1)
    okbutton = Button(insertwindow, text = "Ok", command = lambda : ok())
    okbutton.grid(row = 2, sticky = W)
    

