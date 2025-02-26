moznost = input("Ak chceš šifrovať zadaj 1 ak chceš dešifrovať zadaj 2 : ")
if moznost == str(1):
    ret = input("Zadaj slovo ktoré chceš zašifrovať: ")
    za_ret = (ord(ret)+1)
    print(chr(za_ret))