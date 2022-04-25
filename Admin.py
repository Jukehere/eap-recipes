from hashlib import new
from itertools import count
import sqlite3
from unicodedata import category

def adminusers():
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check1 = 0
    while check1 == 0:
        username = input('\nUsername (- για έξοδο): ')
        if username != '-':
            cursor.execute('SELECT * FROM Users WHERE Username = ?', (username,))
            curcheck = cursor.fetchone()
            if curcheck == None:
                print("Δεν βρέθηκε το Username. Προσπάθησε ξανά.")
            if curcheck != None:
                if curcheck != '-':
                    check2 = 0
                    while check2 == 0:
                        print("\nΣτοιχεία χρήστη:\n")
                        print("Rank:", curcheck[0])
                        print("Username:", curcheck[1])
                        print("\nΕπιλογές Διαχείρισης:\n")
                        print("1. Προβολή Συνταγών Χρήστη")
                        print("2. Διαγραφή Χρήστη")
                        print("3. Πίσω στο Admin Panel")
                        choice = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
                        if choice == '1':
                            cursor.execute('SELECT (SELECT COUNT() FROM Recipes) AS COUNT, * FROM Recipes WHERE User = ?',(username,))
                            count = cursor.fetchall()
                            if count != []:
                                counter = count[0][0]
                                print("Βρέθηκε/Βρέθηκαν", counter,"Συνταγή/Συνταγές.")
                                i = 1
                                for i in range(counter-1):
                                    print("\n",i+1,"η Συνταγή:\n")
                                    print("Τίτλος:", count[i - int(1)][1])
                                    print("Κατηγορία:", count[i - int(1)][4])
                                    print("Βαθμολογία:", count[i - int(1)][6])
                                    print("Προβολές:", count[i - int(1)][8])
                                    print("RID:", count[i - int(1)][3])
                            if count == []:
                                print("\nΟ Χρήστης δεν έχει Συνταγές στο Σύστημα.")
                        if choice == '2':
                            print("\nΕίστε σίγουρος ότι θέλετε να διαγράψετε τον χρήστη", username,"?")
                            impchoice = input("Πατήστε 1 για Ναι, 2 για Όχι: ")
                            if impchoice == '1':
                                cursor.execute("DELETE FROM Users WHERE Username = ?",(username,))
                                connection.commit()
                                print("\nΟ χρήστης διαγράφηκε.\n")
                                check2 = 1
                                check1 = 1
                            if impchoice == '2':
                                pass
                            elif choice != '1' and choice != '2':
                                print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
                        if choice == '3':
                            check2 = 1
                            check1 = 1
                        elif choice != '1' and choice != '2' and choice != '3':
                            print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
                if curcheck == '-':
                    check1 = 1
        if username == "-":
            check1 = 1
    connection.close()
                
            

def adminrecipes():
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check1 = 0
    while check1 == 0:
        rid = input('\nRID (- για έξοδο): ')
        if rid != '-':
            cursor.execute('SELECT * FROM Recipes WHERE RID = ?', (rid,))
            curcheck = cursor.fetchone()
            if curcheck == None:
                print("Δεν βρέθηκε το RID. Προσπάθησε ξανά.")
            if curcheck != None:
                check2 = 0
                while check2 == 0:
                    print("\nΒρέθηκε η εξής συνταγή:\n")
                    print("Τίτλος:", curcheck[0])
                    print("Χρήστης:", curcheck[1])
                    print("Κατηγορία:", curcheck[3])
                    print("Βαθμολογία:", curcheck[5])
                    print("Προβολές:", curcheck[7])
                    print("\nΕπιλογές Διαχείρισης:\n")
                    print("1. Τροποποίηση Συνταγής")
                    print("2. Διαγραφή Συνταγής")
                    print("3. Πίσω στο Admin Panel")
                    choice = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
                    if choice == '1':
                        check3 = 0
                        while check3 == 0:
                            print("\nΕπιλογές τροποποίησης:\n")
                            print("1. Αλλαγή Τίτλου")
                            print("2. Αλλαγή Κατηγορίας")
                            print("3. Αλλαγή Συγκεκριμένου Βήματος")
                            print("4. Αλλαγή Υλικών")
                            print("5. Πίσω στη διαχείριση")
                            choice1 = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
                            if choice1 == '1':
                                newtitle = input('\nΕισάγετε τον νέο τίτλο (- για έξοδος): ')
                                if newtitle != '-':
                                    cursor.execute("UPDATE Recipes SET Name = ? WHERE RID = ?",(newtitle,rid))
                                    connection.commit()
                                    print("\nΕπιτυχής αλλαγή τίτλου από", curcheck[0], "σε", newtitle)
                                if newtitle == '-':
                                    check3 = 1
                            if choice1 == '2':
                                print("\nΕπιλογές κατηγοριών:\n")
                                check6 = 0
                                while check6 == 0:
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
                                        check6 = 1
                                    if choice2 == '2':
                                        category = "Σούπες"
                                        check6 = 1
                                    if choice2 == '3':
                                        category = "Όσπρια"
                                        check6 = 1
                                    if choice2 == '4':
                                        category = "Λαχανικά"
                                        check6 = 1
                                    if choice2 == '5':
                                        category = "Ζύμες"
                                        check6 = 1
                                    if choice2 == '6':
                                        category = "Κρεατικά"
                                        check6 = 1
                                    if choice2 == '7':
                                        category = "Ζυμαρικά"
                                        check6 = 1
                                    if choice2 == '8':
                                        category = "Γλυκά"
                                        check6 = 1
                                    if choice2 == '9':
                                        category = "Διάφορα"
                                        check6 = 1
                                    elif choice2 != '1' and choice2 != '2' and choice2 != '3' and choice2 != '4' and choice2 != '5' and choice2 != '6'and choice2 != '7' and choice2 != '8' and choice2 != '9':
                                        print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
                                cursor.execute("""UPDATE Recipes SET Category = ? WHERE RID = ?""",(category,rid))
                                connection.commit()
                                print("\nΗ αλλαγή κατηγορίας σε", category,"ήταν επιτυχής.")
                            if choice1 == '3':
                                cursor.execute('SELECT (SELECT COUNT() FROM Steps) AS COUNT, * FROM Recipes WHERE RID = ?',(rid,))
                                countsteps = cursor.fetchall()
                                countersteps = int(countsteps[0][0])
                                check4 = 0
                                while check4 == 0:
                                    print("Υπάρχουν", countersteps,"βήματα.")
                                    stepno = int(input('\nΕισάγετε τον αριθμό του βήματος (- για έξοδος): '))
                                    if stepno != '-':
                                        if stepno < 1 or stepno > countersteps:
                                            print("Το βήμα δεν υπάρχει. Προσπάθησε ξανά.")
                                        if stepno >=1 and stepno <= countersteps:
                                            check5 = 0
                                            while check5 == 0:
                                                cursor.execute("""SELECT * FROM Steps WHERE RID = ? AND StepNo = ?""",(rid,stepno,))
                                                step = cursor.fetchone()
                                                step = step[2]
                                                print("Περιεχόμενο Βήματος:", step)
                                                print("\nΕπιλογές τροποποίησης:\n")
                                                print("1. Αλλαγή περιεχομένου")
                                                print("2. Διαγραφή βήματος (Διαθέσιμο μόνο για το τελευταίο βήμα)")
                                                print("3. Πίσω στις επιλογές")
                                                choice3 = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
                                                if choice3 == '1':
                                                    content = input("\nΝέο περιεχόμενο (- για έξοδο): ")
                                                    if content != '-':
                                                        cursor.execute("UPDATE Steps SET Content = ? WHERE RID = ? AND StepNo = ?",(content,rid,stepno,))
                                                        connection.commit()
                                                        print("Επιτυχής αλλαγή.")
                                                    if content == '-':
                                                        pass
                                                if choice3 == '2':
                                                    print(countersteps)
                                                    if stepno == countersteps:
                                                        cursor.execute("DELETE FROM Steps WHERE RID = ? AND StepNo = ?",(rid,stepno,))
                                                        connection.commit()
                                                        print("\nΤο βήμα διαγράφηκε.")
                                                        check5 = 1
                                                        check4 = 1
                                                    if stepno != countersteps:
                                                        print("Δεν μπορείτε να διαγράψετε άλλα βήματα εκτός από το τελευταίο. Πηγαίνετε πίσω εάν θέλετε να αλλάξετε βήμα.")
                                                if choice3 == '3':
                                                    check5 = 1
                                                    check4 = 1
                                                elif choice != '1' and choice != '2' and choice != '3':
                                                    print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
                            if choice1 == '4':
                                ingredients = curcheck[8]
                                print("\nΥλικά:\n")
                                print(ingredients)
                                newingredients = input("\nΕισάγεται τα νέα υλικά (- για έξοδος): ")
                                if newingredients != '-':
                                    cursor.execute("UPDATE Recipes SET Ingredients = ? WHERE RID = ?",(newingredients,rid,))
                                    connection.commit()
                                    print("Επιτυχής αλλαγή.")
                            if choice1 == '5':
                                check3 = 1
                            elif choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
                                print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
                    if choice == '2':
                        cursor.execute("DELETE FROM Recipes WHERE RID = ?",(rid))
                        connection.commit()
                        print("\nΗ συνταγή διαγράφηκε.\n")
                        check2 = 1
                        check1 = 1
                    if choice == '3':
                        check2 = 1
                        check1 = 1
                    elif choice != '1' and choice != '2' and choice != '3':
                        print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
        if rid == '-':
            check1 = 1
    connection.close()
    
def adminratings():
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check = 0
    while check == 0:
        rid = input('\nRID (- για έξοδο): ')
        if rid != '-':
            cursor.execute('SELECT (SELECT COUNT() FROM Ratings) AS COUNT, * FROM Ratings WHERE RID = ?',(rid,))
            curcheck = cursor.fetchall()
            if curcheck == []:
                print("Δεν βρέθηκε το RID ή δεν υπάρχουν αξιολογίσεις για το συγκεκριμένο RID.")
            if curcheck != []:
                check1 = 0
                while check1 == 0:
                    cursor.execute('SELECT (SELECT COUNT() FROM Ratings) AS COUNT, * FROM Ratings WHERE RID = ?',(rid,))
                    curcheck = cursor.fetchall()
                    counter = curcheck[0][0]
                    print("Βρέθηκε/Βρέθηκαν", counter,"Αξιολόγηση/Αξιολογίσεις.")
                    i = 1
                    print("\n1. Εμφάνιση Αξιολογίσεων")
                    print("2. Διαγραφή Αξιολόγησης (Χρειάζεται αριθμός αστεριών)")
                    print("3. Μαζική Διαγραφή Αξιολογήσεων")
                    print("4. Πίσω στο Admin Panel")
                    choice = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
                    if choice == '1':
                        for i in range(counter):
                            print("\n",i+1,"η Αξιολόγηση:\n")
                            print("RID:", curcheck[i - int(1)][1])
                            print("Αστέρια:", curcheck[i - int(1)][2])
                    if choice == '2':
                        check2 = 0
                        while check2 == 0:
                            stars = input('\nΑστέρια (- για έξοδο): ')
                            if stars != '-':
                                cursor.execute('SELECT * FROM Ratings WHERE RID = ? AND Stars = ?',(rid,stars,))
                                curcheck1 = cursor.fetchone()
                                if curcheck1 == []:
                                    print("Δεν βρέθηκε αξιολόγηση με τα εξής αστέρια.")
                                if curcheck1 != []:
                                    cursor.execute("DELETE FROM Ratings WHERE rowid in (select rowid from Ratings WHERE RID = ? AND Stars = ? LIMIT 1)",(rid,stars,))
                                    connection.commit()
                                    print("\nΗ αξιολόγηση διαγράφηκε.\n")
                            if stars == '-':
                                check2 = 1
                    if choice == '3':
                        print("\nΕίστε σίγουρος ότι θέλετε να διαγράψετε", counter,"αξιολογήσεις?")
                        impchoice = input("Πατήστε 1 για Ναι, 2 για Όχι: ")
                        if impchoice == '1':
                            cursor.execute("DELETE FROM Ratings WHERE RID = ?",(rid,))
                            connection.commit()
                            print("\nΟι αξιολογήσεις διαγράφηκαν.\n")
                            check1 = 1
                            check = 1
                        if impchoice == '2':
                            pass
                    if choice == '4':
                        check1 = 1
                        check = 1
        if rid == '-':
            check = 1
    connection.close()

def adminmenu():
    print("\nAdmin Panel")
    check = 0
    while check == 0:
        print("\n1. Διαχείριση Συνταγών (Χρειάζεται RID)")
        print("2. Διαχείριση Χρηστών")
        print("3. Διαχείριση Αξιολογήσεων")
        print("4. Αποσύνδεση")
        mc = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
        if mc == '1':
            adminrecipes()
        if mc == '2':
            adminusers()
        if mc == '3':
            adminratings()
        if mc == '4': 
            check = 1
            from Start import startmenu
        elif mc != '1' and mc != '2' and mc != '3' and mc != '4':
            print("Άγνωστη επιλογή, προσπάθησε ξανά\n")

