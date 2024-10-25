a = int(input("Zadaj ćislo od 1 do 5 :"))
import random
b = (random.randint(0,5))
if a == b:
    print(f"Uhádol si správne ćislo {a}")
else:
    print("neuhádol si skús ešte raz :(")
    print(f"číslo bolo {b}")