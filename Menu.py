import tkinter
from tkinter import messagebox

def recbutton(root):
    root.destroy()
    from Search import searchmenu
    searchmenu()

def createbutton(rank,root):
    if rank != 1:
        root.destroy()
        from Create import Create_
    if rank == 1:
        messagebox.showerror("Error" , "ΔΕΝ ΜΠΟΡΕΙΣ ΝΑ ΔΗΜΙΟΥΡΓΗΣΕΙΣ ΣΥΝΤΑΓΕΣ ΩΣ ΕΠΙΣΚΕΠΤΗΣ." , parent = root)

def myrecbutton(username,rank,root):
    if rank != 1:
        root.destroy()
        from Myrec import myrecmenu
        myrecmenu(username)
    if rank == 1:
        messagebox.showerror("Error" , "ΑΥΤΗ Η ΔΥΝΑΤΟΤΗΤΑ ΕΙΝΑΙ ΜΟΝΟ ΓΙΑ ΕΓΓΕΓΡΑΜΜΕΝΟΥΣ ΧΡΗΣΤΕΣ." , parent = root)

def discbutton(root):
    root.destroy()
    from Start import main
    main()

def adminbutton(root):
    root.destroy()
    from Admin import adminmenu
    adminmenu()

def mainmenu(username, rank):
    root = tkinter.Tk()
    root.title('Σύστημα καταγραφής συνταγών μαγειρικής')
    mainlabel = tkinter.Label(root, text=('Καλοσόρισες',username), font=1)
    mainlabel.grid(row=0, column=1)
    recb = tkinter.Button(root, text="Προβολή Συνταγών", padx=50, command= lambda: recbutton(root))
    recb.grid(row=1, column=1, padx=5, pady=5)
    createb = tkinter.Button(root, text="Δημιουργία Συνταγών", padx=50, command= lambda: createbutton(rank,root))
    createb.grid(row=2, column=1, padx=5, pady=5)
    myrecb = tkinter.Button(root, text="Οι Συνταγές μου", padx=50, command= lambda: myrecbutton(username,rank,root))
    myrecb.grid(row=3, column=1, padx=5, pady=5)
    if rank != 2:
        discb = tkinter.Button(root, text="Αποσύνδεση", padx=50, command= lambda: discbutton(root))
        discb.grid(row=4, column=1, padx=5, pady=5)
    if rank == 2:
        adminb = tkinter.Button(root, text="Admin Panel", padx=50, command= lambda: adminbutton(root))
        adminb.grid(row=4, column=1, padx=5, pady=5)
    pass

