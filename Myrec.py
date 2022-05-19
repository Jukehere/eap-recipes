import sqlite3

def myrecdelete(username):
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check2 = 0
    while check2 == 0:
        impchoice = input("Νέος κωδικός πρόσβασης: (1 για διαγραφή, 2 για έξοδος)")
        if impchoice == '2':
            check2 = 1
        if impchoice == '1':
            cursor.execute("DELETE FROM Users WHERE Username = ?",(username,))
            connection.commit()
            print("\nΟ λογαριασμός σας διαγράφηκε.")
            check2 = 1
    connection.close()

def myrecpass(username):
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    check1 = 0
    while check1 == 0:
        newpass = input("Νέος κωδικός πρόσβασης: (- για έξοδος)")
        if newpass == '-':
            check1 = 1
        if newpass != '-':
            cursor.execute("UPDATE Users SET Password = ? WHERE Username = ?",(newpass,username,))
            connection.commit()
            print("Επιτυχής αλλαγή.")
            check1 = 1
    connection.close()

def myrecrecipes(username):
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    cursor.execute('SELECT (SELECT COUNT() FROM Steps) AS COUNT, * FROM Recipes WHERE User = ?',(username,))
    curcheck = cursor.fetchall()
    if curcheck == []:
        print("Δεν έχεις συνταγές στο σύστημα.")
    if curcheck != []:
        curcount = int(curcheck[0][0])
        i = 1
        for i in range(curcount-2):
            print(i+1,". ",curcheck[i][1], " Βαθμολογία: ", curcheck[i][6])
        check = 0
        while check == 0:
            choice = input("Επιλέξτε συνταγή: (- για έξοδος)")
            if choice == "-":
                check = 1
            if choice != "-":
                if int(choice) >= 1 and int(choice) <= i+1:
                    #send to showrec.py
                    pass
                if int(choice) < 1 or int(choice) > i+1:
                    print("Λάθος επιλογή, προσπάθησε ξανά.")
    connection.close()

def myrecmenu(username):
    print("\nMy Recipes\n")
    check = 0
    while check == 0:
        print("1. Προβολή συνταγών μου")
        print("2. Αλλαγή Password")
        print("3. Διαγραφή λογαριασμού")
        print("4. Έξοδος από το πρόγραμμα")
        choice = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
        if choice == '1':
            myrecrecipes(username)
        if choice == '2':
            myrecpass(username)
        if choice == '3':
            myrecdelete(username)
            check = 1
        if choice == '4': 
            break
        elif choice != '1' and choice != '2' and choice != '3' and choice != '4':
            print("Άγνωστη επιλογή, προσπάθησε ξανά\n")