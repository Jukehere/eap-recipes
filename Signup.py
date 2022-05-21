import sqlite3
import tkinter
from tkinter import messagebox

def close():
    root.destroy()
    from Start import main
    main()

def signup():
    if username.get()=="" or password.get()=="":
        messagebox.showerror("Error" , "Βρέθηκαν κενά πεδία. Προσπάθησε ξανά." , parent = root)
    else:
        connection = sqlite3.connect('RSD.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Users WHERE Username = ?', (username.get(),))
        curcheck = cursor.fetchone()
        if curcheck != None:
            messagebox.showerror("Error" , "Το όνομα χρήστη υπάρχει ήδη, προσπάθησε ξανά." , parent = root)
        else:
            cursor.execute("""INSERT INTO "Users" VALUES (0, ?, ?)""", (username.get(), password.get()))
            connection.commit()
            messagebox.showinfo("Success", "Η εγγραφή σας ήταν επιτυχής. Μπορείτε να εισέλθετε.", parent = root)
            connection.close()   
            from Authentication import sgnpvrfctn
            root.destroy()
            sgnpvrfctn()

def signupproccess():
    pass

root = tkinter.Tk()
root.title('Σύστημα καταγραφής συνταγών μαγειρικής')
mainlabel = tkinter.Label(root, text="Δημιουργία λογαριασμού:", font=1)
mainlabel.grid(row=0, column=1)
usernamel = tkinter.Label(root, text="Όνομα χρήστη:")
usernamel.grid(row=1, column=0)
passwordl = tkinter.Label(root, text="Κωδικός Πρόσβασης:")
passwordl.grid(row=2, column=0)
username = tkinter.StringVar()
password = tkinter.StringVar()
username = tkinter.Entry(root, width=30 , textvariable=username)
username.grid(row=1, column=1)
password = tkinter.Entry(root, width=30 , textvariable=password)
password.grid(row=2, column=1)
signupb = tkinter.Button(root, text = "Signup", command = signup)
signupb.grid(row=3, column=2, padx=5, pady=5)
backb = tkinter.Button(root, text = "Go Back", command = close)
backb.grid(row=3, column=0, padx=5, pady=5)