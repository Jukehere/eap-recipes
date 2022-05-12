import tkinter

def signinbutton():
    from Authentication import sgnpvrfctn
    root.destroy()
    sgnpvrfctn()

def signupbutton():
    from Signup import signupproccess
    root.destroy()
    signupproccess()
    
def guestbutton():
    username = "Επισκέπτης"
    rank = 1
    from Menu import mainmenu
    root.destroy()
    mainmenu(username, rank)
    
root = tkinter.Tk()
mainlabel = tkinter.Label(root, text="Σύστημα καταγραφής συνταγών μαγειρικής")
mainlabel.grid(row=0, column=0)
signinb = tkinter.Button(root, text="Είσοδος με στοιχεία χρήστη", padx=50, command= signinbutton)
signinb.grid(row=1, column=0)
signupb = tkinter.Button(root, text="Εγγραφή", padx=50, command= signupbutton)
signupb.grid(row=2, column=0)
gurstb = tkinter.Button(root, text="Είσοδος ως επισκέπτης", padx=50, command= guestbutton)
gurstb.grid(row=3, column=0)
closeb = tkinter.Button(root, text="Έξοδος από το πρόγραμμα", padx=50, command= root.destroy)
closeb.grid(row=4, column=0)
root.mainloop()
