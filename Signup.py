import sqlite3

def signupproccess():
    print("\nΔημιουργία λογαριασμού:\n")
    checkempty = 0
    connection = sqlite3.connect('RSD.db')
    cursor = connection.cursor()
    while checkempty == 0:
        username = input("Όνομα χρήστη: ")
        password = input("Κωδικός Πρόσβασης: ")
        checkempty = 1
        if username == '' or password == '':
            print("Βρέθηκε κενό πεδίο. Προσπάθησε ξανά.")
            checkempty = 0
        cursor.execute('SELECT * FROM Users WHERE Username = ?', (username,))
        curcheck = cursor.fetchone()
        if curcheck != None:
            print("Υπάρχει ήδη χρήστης με το username", username,". Προσπάθησε ξανά.")
            checkempty = 0
    cursor.execute("""INSERT INTO "Users" VALUES (0, ?, ?)""", (username, password))
    connection.commit()
    print("\nΤώρα μπορείτε να εισέλθετε.\n")
    connection.close
    from Authentication import sgnpvrfctn
    sgnpvrfctn()
    