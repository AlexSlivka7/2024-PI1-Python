print("Ahoj vitaj v rulete")
print("----------------------")
print("Môžeš vsádzať na:")
print("--------------------------------------")
print("Farba(čierna, červená)")
print("číslo(0-36)")
print("párne čísla alebo nepárne čísla")
print("tretiny: 1/3 , 2/3 , 3/3")
print("rady: 1, 2, 3")
print("---------------------------------------")



import random
farby = ("čierna" , "červená")
čísla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
párnosť = ("párne čísla" , "nepárne čísla")

konto = 0

while True:
    
    try:
        typ_vsadenia = str(input("Zadaj načo chceš vsadiť: "))

        if typ_vsadenia == "koniec":
            break
        #farby:
        elif typ_vsadenia == "farba":
            farba = input("Zadaj na akú farbu chceš vsadiť: ")
            bet = int(input("Zadaj koľko chceš vsadiť od 1 do 10 000€: "))
            random_farba = random.choice(farby)
            if farba == random_farba:
                konto = konto + (bet * 2)
                print(f"Vyhral si gratulujem padla {random_farba} tvoje konto je {konto}€")
            else:
                konto = konto - bet
                print(f"Prehral si škoda padla {random_farba} tvoje konto je {konto}€")
        #čísla:
        elif typ_vsadenia =="číslo":
            číslo = input("Zadaj na aké číslo chceš vsadiť: ")
            bet = int(input("Zadaj koľko chceš vsadiť od 1 do 10 000€: "))
            random_číslo = random.randint(0,36)
            if číslo == random_číslo:
                if konto < 1:
                    konto = (konto + 1) * 36
                    print(f"Vyhral si gratulujem padlo číslo {random_číslo} tvoje konto je {konto}€")
                else:
                    konto = konto * 36
                    print(f"Vyhral si gratulujem padlo číslo {random_číslo} tvoje konto je {konto}€")
            else:
               konto = konto - bet
               print(f"Prehral si škoda padlo číslo {random_číslo} tvoje konto je {konto}€") 
        #párne čísla
        elif typ_vsadenia == "párne čísla":
            bet = int(input("Zadaj koľko chceš vsadiť od 1 do 10 000€: "))
            random_párnosť = random.choice(párnosť)
            if typ_vsadenia == random_párnosť:
                konto = konto + (bet * 2)
                print(f"Vyhral si gratulujem padli {random_párnosť} tvoje konto je {konto}€")
            else:
                konto = konto - bet
                print(f"Prehral si škoda padli {random_párnosť} tvoje konto je {konto}€")
        #nepárne čísla
        elif typ_vsadenia == "nepárne čísla":
            bet = int(input("Zadaj koľko chceš vsadiť od 1 do 10 000€: "))
            random_párnosť = random.choice(párnosť)
            if typ_vsadenia == random_párnosť:
                konto = konto + (bet * 2)
                print(f"Vyhral si gratulujem padli {random_párnosť} tvoje konto je {konto}€")
            else:
                konto = konto - bet
                print(f"Prehral si škoda padli {random_párnosť} tvoje konto je {konto}€")   
        

        
    except ValueError:
        print("zadaj slovo prosím!!!!")

print(f"Tvoje konečné konto je {konto}€ gratulujem")