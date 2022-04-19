def startmenu():
    check = 0
    print("Σύστημα καταγραφής συνταγών μαγειρικής\n")
    while check == 0:
        print("1. Είσοδος με στοιχεία χρήστη")
        print("2. Εγγραφή")
        print("3. Είσοδος ως επισκέπτης")
        print("4. Έξοδος από το πρόγραμμα")
        c = input('\nΔιαλέξτε από τις παραπάνω επιλογές: ')
        if c == '1':
            check = 1
        if c == '2':
            from Signup import signupproccess
            signupproccess()
            check = 1
        if c == '3':
            check = 1
            username = "Επισκέπτης"
            rank = 1
            from Menu import mainmenu
            mainmenu(username, rank)
        if c == '4': 
            break
        elif c != '1' and c != '2' and c != '3' and c != '4':
            print("Άγνωστη επιλογή, προσπάθησε ξανά\n")
        

startmenu()
