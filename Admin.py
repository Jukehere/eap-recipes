def adminmenu():
    print("\nAdmin Panel\n")
    check = 1
    while check == 1:
        print("1. Διαχείριση Συνταγών")
        print("2. Διαχείριση Χρηστών")
        print("3. Διαχείριση Αξιολογήσεων")
        print("4. Αποσύνδεση")
        mc = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
        if mc == '1':
            check = 0
        if mc == '2':
            check = 0
        if mc == '3':
            check = 0
        if mc == '4': 
            check = 0
            from Start import startmenu
        elif mc != '1' and mc != '2' and mc != '3' and mc != '4':
            print("Άγνωστη επιλογή, προσπάθησε ξανά\n")