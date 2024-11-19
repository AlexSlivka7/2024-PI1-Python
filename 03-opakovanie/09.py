číslo = int(input("Zadaj číslo:"))
sucet , i = 0, 1
for znak in str (číslo):
    cifra = int(znak)
    print(f"{i}. cifra {cifra}")
    sucet += cifra
    i += 1
print("ciferný súčet je" , sucet)