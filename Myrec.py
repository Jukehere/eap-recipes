import sqlite3
import tkinter
from tkinter import messagebox
from tkinter import ttk

def myrecdelete(username,root):
    def close(username):
        delete.destroy()
        myrecmenu(username)
    def deleteacc(username):
        connection = sqlite3.connect('RSD.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Users WHERE Username = ?",(username,))
        connection.commit()
        messagebox.showinfo(title="Success", message="Ο λογαριασμός σας διαγράφηκε.", parent = delete)
        delete.destroy()
        myrecmenu(username)
    delete = tkinter.Tk()
    delete.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabel = tkinter.Label(delete, text="Διαγραφή Λογαριασμού?", font=1)
    mainlabel.grid(row=0, column=1)
    signupb = tkinter.Button(delete, text = "Ναι", command = lambda: deleteacc(username))
    signupb.grid(row=2, column=2, padx=5, pady=5)
    backb = tkinter.Button(delete, text = "Όχι", command = lambda: close(username))
    backb.grid(row=2, column=0, padx=5, pady=5)

def myrecpass(username,root):
    def close(username):
        mrp.destroy()
        myrecmenu(username)
    def changepass(newpass,username):
        connection = sqlite3.connect('RSD.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE Users SET Password = ? WHERE Username = ?",(newpass,username,))
        connection.commit()
        messagebox.showinfo(title="Success", message="Επιτυχής αλλαγή.", parent = mrp)
        mrp.destroy()
        myrecmenu(username)
    root.destroy()
    mrp = tkinter.Tk()
    mrp.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mrpl = tkinter.Label(mrp, text="Αλλαγή Password", font=1)
    mrpl.grid(row=0, column=1)
    newpassl = tkinter.Label(mrp, text="Νέος κωδικός πρόσβασης:")
    newpassl.grid(row=1, column=0)
    newpass = tkinter.StringVar()
    newpass = tkinter.Entry(mrp, width=30 , textvariable=newpass)
    newpass.grid(row=1, column=1)
    changeb = tkinter.Button(mrp, text = "Change Pass", command = lambda: changepass(username,newpass.get()))
    changeb.grid(row=2, column=2, padx=5, pady=5)
    backb = tkinter.Button(mrp, text = "Go Back", command = lambda: close(username))
    backb.grid(row=2, column=0, padx=5, pady=5)

def myrecrecipes(username,root):
    def submitsel(select,username):
        cursor.execute('SELECT * FROM Recipes WHERE RID = ? AND User = ?',(select,username,))
        curcheck = cursor.fetchone()
        if curcheck != None:
            from Showrec import Show_rec
            Show_rec(select)
            show.destroy()
        if curcheck == None:
            messagebox.showerror("Error" , "Το RID δεν βρέθηκε, προσπάθησε ξανά." , parent = show)
    def close(username):
        show.destroy()
        myrecmenu(username)
    connection = sqlite3.connect('dishes.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Recipes WHERE User = ?',(username,))
    curcheck = cursor.fetchall()
    if curcheck == []:
        messagebox.showerror("Error" , "Δεν υπάρχουν συνταγές σας στο σύστημα." , parent = root)
    if curcheck != []:
        root.destroy()
        show = tkinter.Tk()
        show.title('Σύστημα καταγραφής συνταγών μαγειρικής')
        showlabel = tkinter.Label(show, text=('Συνταγές:'), font=1)
        showlabel.grid(row=0, column=1)
        table = ttk.Treeview(show, columns=(1,2,3,4,5,6,7,8,9), show="headings", height=5)
        table.grid(row=1, column=1, padx=10, pady=10)
        table.heading(1, text="RID")
        table.heading(2, text="Name")
        table.heading(3, text="Category")
        table.heading(4, text="Difficulty")
        table.heading(5, text="TimeH")
        table.heading(6, text="TimeM")
        table.heading(7, text="NOI")
        table.heading(8, text="NOS")
        table.heading(9, text="User")
        table.column(1)
        table.column(2)
        table.column(3)
        table.column(4)
        table.column(5, minwidth=0, width=0)
        table.column(6, minwidth=0, width=0)
        table.column(7, minwidth=0, width=0)
        table.column(8, minwidth=0, width=0)
        table.column(9)
        for i in curcheck:
            table.insert('', 'end', values=i)
        selectl = tkinter.Label(show, text="RID:")
        selectl.grid(row=2, column=0)
        select = tkinter.StringVar()
        select = tkinter.Entry(show, width=30 , textvariable=select)
        select.grid(row=2, column=1)
        submitb = tkinter.Button(show, text = "Submit", command = lambda: submitsel(select.get(),username))
        submitb.grid(row=3, column=2, padx=5, pady=5)
        backb = tkinter.Button(show, text = "Go Back", command = lambda: close(username))
        backb.grid(row=3, column=0, padx=5, pady=5)

def myrecmenu(username):
    root = tkinter.Tk()
    root.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabel = tkinter.Label(root, text=('My Recipes'), font=1)
    mainlabel.grid(row=0, column=1)
    myrecb = tkinter.Button(root, text="Προβολή συνταγών μου", padx=50, command= lambda: myrecrecipes(username,root))
    myrecb.grid(row=1, column=1, padx=5, pady=5)
    passwordb = tkinter.Button(root, text="Αλλαγή Password", padx=50, command= lambda: myrecpass(username,root))
    passwordb.grid(row=2, column=1, padx=5, pady=5)
    deleteb = tkinter.Button(root, text="Διαγραφή λογαριασμού", padx=50, command= lambda: myrecdelete(username,root))
    deleteb.grid(row=3, column=1, padx=5, pady=5)
    closeb = tkinter.Button(root, text="Έξοδος από το πρόγραμμα", padx=50, command= root.destroy)
    closeb.grid(row=4, column=1, padx=5, pady=5)