import sqlite3
import tkinter
from tkinter import Button, OptionMenu, StringVar, messagebox
from tkinter import ttk

def searchcat(root):
    def searchcatsel(selection):
        def submitsel(select):
            cursor.execute('SELECT * FROM Recipes WHERE RID = ?',(select,))
            curcheck = cursor.fetchone()
            if curcheck != None:
                #send to showrec.py
                show.destroy()
            if curcheck == None:
                messagebox.showerror("Error" , "Το RID δεν βρέθηκε, προσπάθησε ξανά." , parent = show)
        def close():
            show.destroy()
            searchmenu()
        cursor.execute('SELECT * FROM Recipes WHERE Category = ?',(selection,))
        curcheck = cursor.fetchall()
        if curcheck == []:
            messagebox.showerror("Error" , "Δεν υπάρχουν συνταγές στη συγκεκριμένη κατηγορία." , parent = cat)
        if curcheck != []:
            cat.destroy()
            show = tkinter.Tk()
            show.title('Σύστημα καταγραφής συνταγών μαγειρικής')
            showlabel = tkinter.Label(show, text=('Συνταγές:'), font=1)
            showlabel.grid(row=0, column=1)
            table = ttk.Treeview(show, columns=(1,2,3,4,5,6), show="headings", height=5)
            table.grid(row=1, column=1, padx=10, pady=10)
            table.heading(1, text="Name")
            table.heading(2, text="User")
            table.heading(3, text="RID")
            table.heading(4, text="test")
            table.heading(5, text="test")
            table.heading(6, text="Rating")
            table.column(1)
            table.column(2)
            table.column(3)
            table.column(4, minwidth=0, width=0)
            table.column(5, minwidth=0, width=0)
            table.column(6)
            for i in curcheck:
                table.insert('', 'end', values=i)
            selectl = tkinter.Label(show, text="RID:")
            selectl.grid(row=2, column=0)
            select = tkinter.StringVar()
            select = tkinter.Entry(show, width=30 , textvariable=select)
            select.grid(row=2, column=1)
            submitb = tkinter.Button(show, text = "Submit", command = lambda: submitsel(select.get()))
            submitb.grid(row=3, column=2, padx=5, pady=5)
            backb = tkinter.Button(show, text = "Go Back", command = close)
            backb.grid(row=3, column=0, padx=5, pady=5)
    root.destroy()
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    cat = tkinter.Tk()
    cat.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    catlabel = tkinter.Label(cat, text=('Επιλογές κατηγοριών'), font=1)
    catlabel.grid(row=0, column=1)
    selection = StringVar()
    selection.set("Βασικές")
    dropdown = OptionMenu(cat, selection, "Βασικές", "Σούπες", "Όσπρια", "Λαχανικά", "Ζύμες", "Κρεατικά", "Ζυμαρικά", "Γλυκά", "Διάφορα")
    dropdown.grid(row=1, column=1, padx=5, pady=5)
    submitb = Button(cat, text="Submit", command = lambda: searchcatsel(selection.get()))
    submitb.grid(row=2, column=1, padx=5, pady=5)
                        
def searchrid(root):
    root.destroy()
    def close():
        srid.destroy()
        searchmenu()
    def search():
        cursor.execute('SELECT * FROM Recipes WHERE RID = ?', (rid.get(),))
        curcheck = cursor.fetchone()
        if curcheck == None:
            messagebox.showerror("Error" , "Το RID δεν βρέθηκε, προσπάθησε ξανά." , parent = srid)
        else:
            srid.destroy()
            #send to showrec.py
            pass
        pass
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    srid = tkinter.Tk()
    srid.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabelsrid = tkinter.Label(srid, text="Αναζήτηση συνταγής", font=1)
    mainlabelsrid.grid(row=0, column=1)
    ridl = tkinter.Label(srid, text="RID:")
    ridl.grid(row=1, column=0)
    rid = tkinter.StringVar()
    rid = tkinter.Entry(srid, width=30 , textvariable=rid)
    rid.grid(row=1, column=1)
    searchb = tkinter.Button(srid, text = "Search", command = search)
    searchb.grid(row=2, column=2, padx=5, pady=5)
    backb = tkinter.Button(srid, text = "Go Back", command = close)
    backb.grid(row=2, column=0, padx=5, pady=5)
            
def searchrandom(root):
    root.destroy()
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Recipes ORDER BY RANDOM() LIMIT 1')
    curcheck = cursor.fetchone()
    #send to showrec.py
            


def searchmenu():
    root = tkinter.Tk()
    root.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabel = tkinter.Label(root, text=('Search Menu'), font=1)
    mainlabel.grid(row=0, column=1)
    recchoiceb = tkinter.Button(root, text="Επιλογή κατηγορίας", padx=50, command= lambda: searchcat(root))
    recchoiceb.grid(row=1, column=1, padx=5, pady=5)
    ridsearchb = tkinter.Button(root, text="Εμφάνιση συνταγής μέσω RID", padx=50, command= lambda: searchrid(root))
    ridsearchb.grid(row=2, column=1, padx=5, pady=5)
    randomb = tkinter.Button(root, text="Εμφάνιση τυχαίας συνταγής", padx=50, command= lambda: searchrandom(root))
    randomb.grid(row=3, column=1, padx=5, pady=5)
    closeb = tkinter.Button(root, text="Έξοδος από το πρόγραμμα", padx=50, command= root.destroy)
    closeb.grid(row=4, column=1, padx=5, pady=5)