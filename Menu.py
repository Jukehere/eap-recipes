from tracemalloc import start
import sqlite3


def mainmenu(username, rank):
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check = 1
    print("\nΚαλωσόρισες", username,"\n")
    if username != 'Επισκέπτης':
        cursor.execute("""SELECT Rank FROM Users WHERE Username = (?)""",(username,))
        temp = cursor.fetchone()
        rank = str(temp[0])
    while check == 1:
        print("1. Προβολή Συνταγών")
        print("2. Δημιουργία Συνταγών")
        print("3. Οι Συνταγές μου")
        if rank != 2:
            print("4. Αποσύνδεση")
            mc = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
            if mc == '1':
                check = 0
            if mc == '2':
                if username == 'Επισκέπτης':
                    print("\n ΣΦΑΛΜΑ: ΔΕΝ ΜΠΟΡΕΙΣ ΝΑ ΔΗΜΙΟΥΡΓΗΣΕΙΣ ΣΥΝΤΑΓΕΣ ΩΣ ΕΠΙΣΚΕΠΤΗΣ.\n")
                elif username != 'Επισκέπτης':
                    check = 0
            if mc == '3':
                if username == 'Επισκέπτης':
                    print("\n ΣΦΑΛΜΑ: ΑΥΤΗ Η ΔΥΝΑΤΟΤΗΤΑ ΕΙΝΑΙ ΜΟΝΟ ΓΙΑ ΕΓΓΕΓΡΑΜΜΕΝΟΥΣ ΧΡΗΣΤΕΣ.\n")
                elif username != 'Επισκέπτης':
                    check = 0
            if mc == '4': 
                check = 0
                from Start import startmenu
            elif mc != '1' and mc != '2' and mc != '3' and mc != '4':
                print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
        if rank == 2:
            print("4. Admin Panel")
            mc = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
            if mc == '1':
                check = 0
            if mc == '2':
                check = 0
            if mc == '3':
                check = 0
            if mc == '4': 
                check = 0
                from Admin import adminmenu
                adminmenu()
            elif mc != '1' and mc != '2' and mc != '3' and mc != '4':
                print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
