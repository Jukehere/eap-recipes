def startmenu():
    check = 1
    while check == 1:
        print("Σύστημα καταγραφής συνταγών μαγειρικής")
        print("1. Είσοδος με στοιχεία χρήστη")
        print("2. Εγγραφή")
        print("3. Είσοδος ως επισκέπτης")
        print("4. Έξοδος από το πρόγραμμα")
        c = input('Διαλέξτε από τις παραπάνω επιλογές: ')
        if c == '1':
            check = 0
        if c == '2':
            check = 0
        if c == '3':
            check = 0
        if c == '4': break
        

startmenu()
