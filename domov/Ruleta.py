#Úvod:

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

while True:
        
        vsadenie = input("Načo chceš vsadiť: ")
        if vsadenie == ("koniec"):
                break
        if vsadenie == ("farba"):
               
               farba = input("Na akú farbu chceš vsadiť (čierna alebo červená): ")
               bet = int(input("Zadaj koľko chceš vsadiť(min. 1 max.1000): "))
               random_farba = random.choice(farby)
               if farba == random_farba:
                       
                       konto =bet + bet
                       print(f"vyhral si farba bola {random_farba}")
                       
                       print(f"Tvoje konto je {konto}€")
               else:
                       
                       konto = bet -bet - bet 
                       print(f"prehral si farba bola {random_farba}")
                       print(f"tvoje konto je {konto}€")
            

print(f"Skončil si tvoje konečné konto bolo {konto}€")
         