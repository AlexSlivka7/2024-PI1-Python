# print(bin(255)) #vypíše číslo v binárnej podobe
# print(hex(255)) #vypíše číslo v hexadecimálnej podobe
# print(0b11111111) #vypiše číslo v desiatkovej podobe
# print(0xff) #vypiše číslo v hexadecimálnej podobe
# cislo = int(input("Zadaj cislo: "))
print("Zadaj 1 ak chceš prevádzať do binárnej sústavy")
print("Zadaj 2 ak chceš prevádzať do hexadecimálnej sústavy")
print("Zadaj 3 ak chceš prevádzať do octálnej sústavy")
print("Zadaj 4 ak chceš skončit")
moznost = int(input("Zadaj: "))




def dec_bin(cislo):
    binarne = ""
    while cislo > 0:
        zvysok = cislo % 2
        binarne = str(zvysok) + binarne 
        cislo = cislo // 2
    return binarne


def dec_hex(cislo):
    hexadecimalne = ""
    while cislo > 0:
        zvysok = cislo % 16
        # if zvysok == 10:
        #     zvysok = "A"
        # elif zvysok == 11:
        #     zvysok = "B"
        # elif zvysok == 12:
        #     zvysok = "C"
        # elif zvysok == 13:
        #     zvysok = "D"
        # elif zvysok == 14:
        #     zvysok = "E"
        # elif zvysok == 15:
        #     zvysok = "F"
        if zvysok < 10:
            hexadecimalne = str(zvysok) + hexadecimalne
        else:
            hexadecimalne = chr(55 + zvysok) + hexadecimalne 
        cislo = cislo //16
    return hexadecimalne

def dec_oct(cislo):
    osmickove = ""
    while cislo > 0:
        zvysok = cislo % 8
        osmickove = str(zvysok) + osmickove 
        cislo = cislo // 8
    return osmickove

if moznost == 1:
    cislo = int(input("Zadaj číslo: "))
    print(dec_bin(cislo))

elif moznost == 2:
    cislo = int(input("Zadaj číslo: "))
    print(dec_hex(cislo))

elif moznost == 3:
    cislo = int(input("Zadaj číslo: "))
    print(dec_oct(cislo))

else:
    print("Zadal si zle")



    





