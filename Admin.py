import sqlite3
import tkinter
from tkinter import messagebox
from tkinter import ttk

def adminusers(root):
    def search():
        def usermenu(curcheck):
            def seerec():
                def closeshow():
                    show.destroy()
                    adminmenu()
                cursor.execute('SELECT * FROM Recipes WHERE User = ?',(username,))
                curcheck = cursor.fetchall()
                if curcheck == []:
                    messagebox.showerror("Error" , "Ο Χρήστης δεν έχει Συνταγές στο Σύστημα." , parent = umenu)
                if curcheck != []:
                    umenu.destroy()
                    show = tkinter.Tk()
                    show.title('Σύστημα καταγραφής συνταγών μαγειρικής')
                    showlabel = tkinter.Label(show, text=('Συνταγές:'), font=1)
                    showlabel.grid(row=0, column=1)
                    table = ttk.Treeview(show, columns=(1,2,3,4,5,6,7,8), show="headings", height=5)
                    table.grid(row=1, column=1, padx=10, pady=10)
                    table.heading(1, text="Name")
                    table.heading(2, text="User")
                    table.heading(3, text="RID")
                    table.heading(4, text="Category")
                    table.heading(5, text="")
                    table.heading(6, text="Rating")
                    table.heading(7, text="")
                    table.heading(8, text="Views")
                    table.column(1)
                    table.column(2, minwidth=0, width=0)
                    table.column(3)
                    table.column(4)
                    table.column(5, minwidth=0, width=0)
                    table.column(6)
                    table.column(7, minwidth=0, width=0)
                    table.column(8)
                    for i in curcheck:
                        table.insert('', 'end', values=i)
                    backb = tkinter.Button(show, text = "Go Back to Admin Menu", command = closeshow)
                    backb.grid(row=3, column=1, padx=5, pady=5)
            def deleteuser():
                choice = messagebox.askquestion("Choice","Είστε σίγουρος ότι θέλετε να διαγράψετε τον συγκεκριμένο χρήστη?", parent = umenu)
                if choice == "yes":
                    cursor.execute("DELETE FROM Users WHERE Username = ?",(username,))
                    connection.commit()
                    messagebox.showinfo(title="Success", message="Ο χρήστης διαγράφηκε.", parent = umenu)
                    umenu.destroy()
                    adminmenu()
            def closeumenu():
                umenu.destroy()
                adminmenu()
            rank = curcheck[0]
            username = curcheck[1]
            umenu = tkinter.Tk()
            umenu.title('Σύστημα καταγραφής συνταγών μαγειρικής')
            mainlabel = tkinter.Label(umenu, text=(username, "Rank", rank), font=1)
            mainlabel.grid(row=0, column=1)
            recipesb = tkinter.Button(umenu, text="Προβολή Συνταγών Χρήστη", padx=50, command= seerec)
            recipesb.grid(row=1, column=1, padx=5, pady=5)
            deleteb = tkinter.Button(umenu, text="Διαγραφή Χρήστη", padx=50, command= deleteuser)
            deleteb.grid(row=2, column=1, padx=5, pady=5)
            discb = tkinter.Button(umenu, text="Πίσω στο Admin Panel", padx=50, command= closeumenu)
            discb.grid(row=3, column=1, padx=5, pady=5)
        cursor.execute('SELECT * FROM Users WHERE Username = ?', (user.get(),))
        curcheck = cursor.fetchone()
        if curcheck == None:
            messagebox.showerror("Error" , "Το Username δεν βρέθηκε, προσπάθησε ξανά." , parent = user)
        else:
            users.destroy()
            usermenu(curcheck)
    def close():
        users.destroy()
        adminmenu()
    root.destroy()
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    users = tkinter.Tk()
    users.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabelsrid = tkinter.Label(users, text="Αναζήτηση χρήστη", font=1)
    mainlabelsrid.grid(row=0, column=1)
    usernamel = tkinter.Label(users, text="Username:")
    usernamel.grid(row=1, column=0)
    user = tkinter.StringVar()
    user = tkinter.Entry(users, width=30 , textvariable=user)
    user.grid(row=1, column=1)
    searchb = tkinter.Button(users, text = "Search", command = search)
    searchb.grid(row=2, column=2, padx=5, pady=5)
    backb = tkinter.Button(users, text = "Go Back", command = close)
    backb.grid(row=2, column=0, padx=5, pady=5)
                
            

def adminrecipes(root):
    def submitsel(rid):
        def editrec(rid):
            def edittitle(rid):
                def close():
                    titlechange.destroy()
                    adminmenu()
                def changetitle(rid,newtitle):
                    connection = sqlite3.connect('RSD.db')
                    cursor = connection.cursor()
                    cursor.execute("UPDATE Recipes SET Name = ? WHERE RID = ?",(newtitle,rid,))
                    connection.commit()
                    messagebox.showinfo(title="Success", message="Επιτυχής αλλαγή.", parent = titlechange)
                    titlechange.destroy()
                    adminmenu()
                changemenu.destroy()
                titlechange = tkinter.Tk()
                titlechange.title('Σύστημα καταγραφής συνταγών μαγειρικής')
                tcl = tkinter.Label(titlechange, text="Εισάγετε τον νέο τίτλο", font=1)
                tcl.grid(row=0, column=1)
                newtitlel = tkinter.Label(titlechange, text="Νέος τίτλος:")
                newtitlel.grid(row=1, column=0)
                newtitle = tkinter.StringVar()
                newtitle = tkinter.Entry(titlechange, width=30 , textvariable=newtitle)
                newtitle.grid(row=1, column=1)
                changeb = tkinter.Button(titlechange, text = "Change Title", command = lambda: changetitle(rid,newtitle.get()))
                changeb.grid(row=2, column=2, padx=5, pady=5)
                backb = tkinter.Button(titlechange, text = "Go Back", command = close)
                backb.grid(row=2, column=0, padx=5, pady=5)
            def editcategory(rid):
                def changecat(select, rid):
                    cursor.execute('UPDATE Recipes SET Category = ? WHERE RID = ?',(select,rid))
                    connection.commit()
                    messagebox.showinfo(title="Success", message="Επιτυχής αλλαγή.", parent = catchange)
                    catchange.destroy()
                    adminmenu()
                catchange = tkinter.Tk()
                catchange.title('Σύστημα καταγραφής συνταγών μαγειρικής')
                catlabel = tkinter.Label(catchange, text=('Επιλογές κατηγοριών'), font=1)
                catlabel.grid(row=0, column=1)
                selection = tkinter.StringVar()
                selection.set("Βασικές")
                dropdown = tkinter.OptionMenu(catchange, selection, "Βασικές", "Σούπες", "Όσπρια", "Λαχανικά", "Ζύμες", "Κρεατικά", "Ζυμαρικά", "Γλυκά", "Διάφορα")
                dropdown.grid(row=1, column=1, padx=5, pady=5)
                submitb = tkinter.Button(catchange, text="Submit", command = lambda: changecat(selection.get(),rid))
                submitb.grid(row=2, column=1, padx=5, pady=5)
            def editingr(rid):
                def close():
                    ingrchange.destroy()
                    adminmenu()
                def changetitle(rid,newingr):
                    connection = sqlite3.connect('RSD.db')
                    cursor = connection.cursor()
                    cursor.execute("UPDATE Recipes SET Ingredients = ? WHERE RID = ?",(newingr,rid,))
                    connection.commit()
                    messagebox.showinfo(title="Success", message="Επιτυχής αλλαγή.", parent = ingrchange)
                    ingrchange.destroy()
                    adminmenu()
                changemenu.destroy()
                ingrchange = tkinter.Tk()
                ingrchange.title('Σύστημα καταγραφής συνταγών μαγειρικής')
                tcl = tkinter.Label(ingrchange, text="Εισάγεται τα νέα υλικά", font=1)
                tcl.grid(row=0, column=1)
                newingrl = tkinter.Label(ingrchange, text="Νέα υλικά:")
                newingrl.grid(row=1, column=0)
                newingr = tkinter.StringVar()
                newingr = tkinter.Entry(ingrchange, width=30 , textvariable=newingr)
                newingr.grid(row=1, column=1)
                changeb = tkinter.Button(ingrchange, text = "Change Ingredients", command = lambda: changetitle(rid,newingr.get()))
                changeb.grid(row=2, column=2, padx=5, pady=5)
                backb = tkinter.Button(ingrchange, text = "Go Back", command = close)
                backb.grid(row=2, column=0, padx=5, pady=5)
            def bts():
                changemenu.destroy()
                adminmenu()
            editmenu.destroy()
            changemenu = tkinter.Tk()
            changemenu.title('Σύστημα καταγραφής συνταγών μαγειρικής')
            mainlabel = tkinter.Label(changemenu, text=('Επιλογές τροποποίησης:'), font=1)
            mainlabel.grid(row=0, column=1)
            changetb = tkinter.Button(changemenu, text="Αλλαγή Τίτλου", padx=50, command= lambda: edittitle(rid))
            changetb.grid(row=1, column=1, padx=5, pady=5)
            changecb = tkinter.Button(changemenu, text="Αλλαγή Κατηγορίας", padx=50, command= lambda: editcategory(rid))
            changecb.grid(row=2, column=1, padx=5, pady=5)
            changeib = tkinter.Button(changemenu, text="Αλλαγή Υλικών", padx=50, command= lambda: editingr(rid))
            changeib.grid(row=3, column=1, padx=5, pady=5)
            backb = tkinter.Button(changemenu, text="Πίσω στο Admin Panel", padx=50, command= bts)
            backb.grid(row=4, column=1, padx=5, pady=5)
        def deleterec(rid):
            choice = messagebox.askquestion("Choice","Είστε σίγουρος ότι θέλετε να διαγράψετε όλες τη συνταγή αυτή?", parent = editmenu)
            if choice == "yes":
                cursor.execute("DELETE FROM Recipes WHERE RID = ?",(rid,))
                connection.commit()
                messagebox.showinfo(title="Success", message="Η συνταγή διαγράφηκε.", parent = editmenu)
                editmenu.destroy()
                adminmenu()
        def closeeditmenu():
            editmenu.destroy()
            adminmenu()
        connection = sqlite3.connect('RSD.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Recipes WHERE RID = ?', (rid,))
        curcheck = cursor.fetchall()
        if curcheck != []:
            show.destroy()
            editmenu = tkinter.Tk()
            editmenu.title('Σύστημα καταγραφής συνταγών μαγειρικής')
            mainlabel = tkinter.Label(editmenu, text=('Επιλογές Διαχείρισης:'), font=1)
            mainlabel.grid(row=0, column=1)
            editb = tkinter.Button(editmenu, text="Τροποποίηση Συνταγής", padx=50, command= lambda: editrec(rid))
            editb.grid(row=1, column=1, padx=5, pady=5)
            deleteb = tkinter.Button(editmenu, text="Διαγραφή Συνταγής", padx=50, command= lambda: deleterec(rid))
            deleteb.grid(row=2, column=1, padx=5, pady=5)
            discb = tkinter.Button(editmenu, text="Πίσω στο Admin Panel", padx=50, command= closeeditmenu)
            discb.grid(row=3, column=1, padx=5, pady=5)
        if curcheck == []:
            messagebox.showerror("Error" , "Το RID δεν βρέθηκε, προσπάθησε ξανά." , parent = show)
    def closeshow():
        show.destroy()
        adminmenu()
    root.destroy()
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Recipes')
    curcheck = cursor.fetchall()
    show = tkinter.Tk()
    show.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    showlabel = tkinter.Label(show, text=('Επιλέξτε τη συνταγή που θέλετε να τροποποιήσετε:'), font=1)
    showlabel.grid(row=0, column=1)
    table = ttk.Treeview(show, columns=(1,2,3,4,5,6,7,8), show="headings", height=5)
    table.grid(row=1, column=1, padx=10, pady=10)
    table.heading(1, text="Name")
    table.heading(2, text="User")
    table.heading(3, text="RID")
    table.heading(4, text="Category")
    table.heading(5, text="")
    table.heading(6, text="Rating")
    table.heading(7, text="")
    table.heading(8, text="Views")
    table.column(1)
    table.column(2, minwidth=0, width=0)
    table.column(3)
    table.column(4)
    table.column(5, minwidth=0, width=0)
    table.column(6)
    table.column(7, minwidth=0, width=0)
    table.column(8)
    for i in curcheck:
        table.insert('', 'end', values=i)
    selectl = tkinter.Label(show, text="RID:")
    selectl.grid(row=2, column=0)
    select = tkinter.StringVar()
    select = tkinter.Entry(show, width=30 , textvariable=select)
    select.grid(row=2, column=1)
    submitb = tkinter.Button(show, text = "Submit", command = lambda: submitsel(select.get()))
    submitb.grid(row=3, column=2, padx=5, pady=5)
    backb = tkinter.Button(show, text = "Go Back", command = closeshow)
    backb.grid(row=3, column=0, padx=5, pady=5)
    
def adminratings(root):
    def search():
        def ratingsmenu():
            def deletemassratings():
                choice = messagebox.askquestion("Choice","Είστε σίγουρος ότι θέλετε να διαγράψετε όλες τις αξιολογήσεις για το συγκεκριμένο RID?", parent = rmenu)
                if choice == "yes":
                    cursor.execute("DELETE FROM Ratings WHERE RID = ?",(rid.get(),))
                    connection.commit()
                    messagebox.showinfo(title="Success", message="Οι αξιολογίσεις διαγράφηκαν.", parent = rmenu)
                    rmenu.destroy()
                    adminmenu()
            def deleterating():
                def searchratings():
                    cursor.execute('SELECT * FROM Ratings WHERE RID = ? AND Stars = ?',(rid.get(),stars.get(),))
                    curcheck1 = cursor.fetchone()
                    if curcheck1 == []:
                        messagebox.showerror("Error" , "Δεν βρέθηκε αξιολόγηση με τα εξής αστέρια." , parent = rmenu)
                    if curcheck1 != []:
                        cursor.execute("DELETE FROM Ratings WHERE rowid in (select rowid from Ratings WHERE RID = ? AND Stars = ? LIMIT 1)",(rid.get(),stars.get(),))
                        connection.commit()
                        messagebox.showinfo(title="Success", message="Η αξιολόγηση διαγράφηκε.", parent = delratings)
                        delratings.destroy()
                        ratingsmenu()
                delratings = tkinter.Tk()
                delratings.title('Σύστημα καταγραφής συνταγών μαγειρικής')
                mainlabelsrid = tkinter.Label(delratings, text="Αναζήτηση αξιολογήσεων", font=1)
                mainlabelsrid.grid(row=0, column=1)
                starsl = tkinter.Label(delratings, text="Stars:")
                starsl.grid(row=1, column=0)
                stars = tkinter.StringVar()
                stars = tkinter.Entry(delratings, width=30 , textvariable=stars)
                stars.grid(row=1, column=1)
                searchb = tkinter.Button(delratings, text = "Search", command = searchratings)
                searchb.grid(row=2, column=2, padx=5, pady=5)
                backb = tkinter.Button(delratings, text = "Go Back", command = close)
                backb.grid(row=2, column=0, padx=5, pady=5)
            def seeratings():
                def closeshow():
                    show.destroy()
                    ratingsmenu()
                cursor.execute('SELECT * FROM Ratings WHERE RID = ?',(rid.get(),))
                curcheck = cursor.fetchall()
                if curcheck == []:
                    messagebox.showerror("Error" , "Δεν υπάρχουν αξιολογήσεις στο Σύστημα." , parent = rmenu)
                if curcheck != []:
                    rmenu.destroy()
                    show = tkinter.Tk()
                    show.title('Σύστημα καταγραφής συνταγών μαγειρικής')
                    showlabel = tkinter.Label(show, text=('Ratings:'), font=1)
                    showlabel.grid(row=0, column=1)
                    table = ttk.Treeview(show, columns=(1,2), show="headings", height=5)
                    table.grid(row=1, column=1, padx=10, pady=10)
                    table.heading(1, text="RID")
                    table.heading(2, text="Stars")
                    for i in curcheck:
                        table.insert('', 'end', values=i)
                    backb = tkinter.Button(show, text = "Go Back to Admin Ratings Menu", command = closeshow)
                    backb.grid(row=3, column=0, padx=5, pady=5)
            def closemenu():
                rmenu.destroy()
                adminmenu
            cursor.execute('SELECT (SELECT COUNT() FROM Ratings) AS COUNT, * FROM Ratings WHERE RID = ?',(rid.get(),))
            curcheck = cursor.fetchall()
            counter = curcheck[0][0]
            rmenu = tkinter.Tk()
            rmenu.title('Σύστημα καταγραφής συνταγών μαγειρικής')
            mainlabel = tkinter.Label(rmenu, text=("Βρέθηκε/Βρέθηκαν", counter,"Αξιολόγηση/Αξιολογίσεις."), font=1)
            mainlabel.grid(row=0, column=1)
            recipesb = tkinter.Button(rmenu, text="Εμφάνιση Αξιολογίσεων", padx=50, command= seeratings)
            recipesb.grid(row=1, column=1, padx=5, pady=5)
            deleterb = tkinter.Button(rmenu, text="Διαγραφή Αξιολόγησης (Χρειάζεται αριθμός αστεριών)", padx=50, command= deleterating)
            deleterb.grid(row=2, column=1, padx=5, pady=5)
            deleteb = tkinter.Button(rmenu, text="Μαζική Διαγραφή Αξιολογήσεων", padx=50, command= deletemassratings)
            deleteb.grid(row=3, column=1, padx=5, pady=5)
            discb = tkinter.Button(rmenu, text="Πίσω στο Admin Panel", padx=50, command= closemenu)
            discb.grid(row=4, column=1, padx=5, pady=5)
        cursor.execute('SELECT * FROM Ratings WHERE RID = ?', (rid.get(),))
        curcheck = cursor.fetchone()
        if curcheck == None:
            messagebox.showerror("Error" , "Δεν βρέθηκαν αξιολογίσεις για το συγκεκριμένο RID, προσπάθησε ξανά." , parent = ratings)
        else:
            ratings.destroy()
            ratingsmenu(curcheck)
    def close():
        ratings.destroy()
        adminmenu()
    root.destroy()
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    ratings = tkinter.Tk()
    ratings.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabelsrid = tkinter.Label(ratings, text="Αναζήτηση αξιολογήσεων", font=1)
    mainlabelsrid.grid(row=0, column=1)
    ridl = tkinter.Label(ratings, text="RID:")
    ridl.grid(row=1, column=0)
    rid = tkinter.StringVar()
    rid = tkinter.Entry(ratings, width=30 , textvariable=rid)
    rid.grid(row=1, column=1)
    searchb = tkinter.Button(ratings, text = "Search", command = search)
    searchb.grid(row=2, column=2, padx=5, pady=5)
    backb = tkinter.Button(ratings, text = "Go Back", command = close)
    backb.grid(row=2, column=0, padx=5, pady=5)
    
def discbutton(root):
    root.destroy()
    from Start import main

def adminmenu():
    root = tkinter.Tk()
    root.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabel = tkinter.Label(root, text=('Admin Panel'), font=1)
    mainlabel.grid(row=0, column=1)
    recb = tkinter.Button(root, text="Διαχείριση Συνταγών (Χρειάζεται RID)", padx=50, command= lambda: adminrecipes(root))
    recb.grid(row=1, column=1, padx=5, pady=5)
    usersb = tkinter.Button(root, text="Διαχείριση Χρηστών", padx=50, command= lambda: adminusers(root))
    usersb.grid(row=2, column=1, padx=5, pady=5)
    ratingsb = tkinter.Button(root, text="Διαχείριση Αξιολογήσεων", padx=50, command= lambda: adminratings(root))
    ratingsb.grid(row=3, column=1, padx=5, pady=5)
    discb = tkinter.Button(root, text="Αποσύνδεση", padx=50, command= lambda: discbutton(root))
    discb.grid(row=4, column=1, padx=5, pady=5)

