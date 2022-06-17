import tkinter

def signinbutton():
    from Authentication import loginroccess
    root.destroy()
    loginroccess()

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
    
def main():
    pass
    
root = tkinter.Tk()
root.title('Σύστημα καταγραφής συνταγών μαγειρικής')
mainlabel = tkinter.Label(root, text="Σύστημα καταγραφής συνταγών μαγειρικής", font=1)
mainlabel.grid(row=0, column=1)
signinb = tkinter.Button(root, text="Είσοδος με στοιχεία χρήστη", padx=50, command= signinbutton)
signinb.grid(row=1, column=1, padx=5, pady=5)
signupb = tkinter.Button(root, text="Εγγραφή", padx=50, command= signupbutton)
signupb.grid(row=2, column=1, padx=5, pady=5)
gurstb = tkinter.Button(root, text="Είσοδος ως επισκέπτης", padx=50, command= guestbutton)
gurstb.grid(row=3, column=1, padx=5, pady=5)
closeb = tkinter.Button(root, text="Έξοδος από το πρόγραμμα", padx=50, command= root.destroy)
closeb.grid(row=4, column=1, padx=5, pady=5)
root.mainloop()
