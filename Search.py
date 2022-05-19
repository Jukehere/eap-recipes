import sqlite3
import tkinter

def searchcat():
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    print("\nΕπιλογές κατηγοριών:\n")
    check1 = 0
    while check1 == 0:
        print("1. Βασικές")
        print("2. Σούπες")
        print("3. Όσπρια")
        print("4. Λαχανικά")
        print("5. Ζύμες")
        print("6. Κρεατικά")
        print("7. Ζυμαρικά")
        print("8. Γλυκά")
        print("9. Διάφορα")
        choice2 = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
        if choice2 == '1':
            category = "Βασικές"
        if choice2 == '2':
            category = "Σούπες"
        if choice2 == '3':
            category = "Όσπρια"
        if choice2 == '4':
            category = "Λαχανικά"
        if choice2 == '5':
            category = "Ζύμες"
        if choice2 == '6':
            category = "Κρεατικά"
        if choice2 == '7':
            category = "Ζυμαρικά"
        if choice2 == '8':
            category = "Γλυκά"
        if choice2 == '9':
            category = "Διάφορα"
        elif choice2 != '1' and choice2 != '2' and choice2 != '3' and choice2 != '4' and choice2 != '5' and choice2 != '6'and choice2 != '7' and choice2 != '8' and choice2 != '9':
            print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
        cursor.execute('SELECT (SELECT COUNT() FROM Steps) AS COUNT, * FROM Recipes WHERE Category = ?',(category,))
        curcheck = cursor.fetchall()
        if curcheck == []:
            print("Δεν υπάρχουν συνταγές στη συγκεκριμένη κατηγορία.")
        if curcheck != []:
            curcount = int(curcheck[0][0])
            i = 1
            for i in range(curcount-2):
                print(i+1,". ",curcheck[i][1], " Βαθμολογία: ", curcheck[i][6])
            check2 = 0
            while check2 == 0:
                choice3 = input("Επιλέξτε συνταγή: (- για έξοδος)")
                if choice3 == "-":
                    check1 = 1
                    check2 = 1
                if choice3 != "-":
                    if int(choice3) >= 1 and int(choice3) <= i+1:
                        #send to showrec.py
                        check1 = 1
                        check2 = 1
                    if int(choice3) < 1 or int(choice3) > i+1:
                        print("Λάθος επιλογή, προσπάθησε ξανά.")
                        
def searchrid():
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check = 0
    while check == 0:
        rid = input('\nRID (- για έξοδο): ')
        if rid != '-':
            cursor.execute('SELECT * FROM Recipes WHERE RID = ?', (rid,))
            curcheck = cursor.fetchone()
            if curcheck == None:
                print("Δεν βρέθηκε το RID. Προσπάθησε ξανά.")
            if curcheck != None:
                #send to showrec.py
                check = 0
        if rid == '-':
            check = 1
            
def searchrandom():
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Recipes ORDER BY RANDOM() LIMIT 1')
    curcheck = cursor.fetchone()
    #send to showrec.py
            


def searchmenu():
    mainlabel = tkinter.Label(root, text=('Search Menu'), font=1)
    mainlabel.grid(row=0, column=1)
    recchoiceb = tkinter.Button(root, text="Επιλογή κατηγορίας", padx=50, command= searchcat)
    recchoiceb.grid(row=1, column=1, padx=5, pady=5)
    ridsearchb = tkinter.Button(root, text="Εμφάνιση συνταγής μέσω RID", padx=50, command= searchrid)
    ridsearchb.grid(row=2, column=1, padx=5, pady=5)
    randomb = tkinter.Button(root, text="Εμφάνιση τυχαίας συνταγής", padx=50, command= searchrandom)
    randomb.grid(row=3, column=1, padx=5, pady=5)
    closeb = tkinter.Button(root, text="Έξοδος από το πρόγραμμα", padx=50, command= root.destroy)
    closeb.grid(row=4, column=1, padx=5, pady=5)
    #print("\nSearch Menu\n")
    #check = 0
    #while check == 0:
    #    print("1. Επιλογή κατηγορίας")
    #    print("2. Εμφάνιση συνταγής μέσω RID")
    #    print("3. Εμφάνιση τυχαίας συνταγής")
    #    print("4. Έξοδος από το πρόγραμμα")
    #    choice = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
    #    if choice == '1':
    #        searchcat()
    #    if choice == '2':
    #        searchrid()
    #    if choice == '3':
    #        searchrandom()
    #    if choice == '4': 
    #        break
    #    elif choice != '1' and choice != '2' and choice != '3' and choice != '4':
    #        print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
    
root = tkinter.Tk()
root.title('Σύστημα καταγραφής συνταγών μαγειρικής')