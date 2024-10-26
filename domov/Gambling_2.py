počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať: "))
konto = 0
import random
if počet_kôl == 0:
    print("Zadal si počet kôl 0 zadaj aspoň jeno kolo!!!!")
else:
     for i in range(počet_kôl):
       suma = int(input("Zadaj koľko € chceš vsadiť: "))
       tip = int(input("Zadaj číslo od 1 do 5 ktore tipuješ: "))
       b = (random.randint(1,5))
       počet_kôl = počet_kôl - 1
       if tip == b:
            konto = konto + suma
            print(f"Vyhral si tvoje konto je {konto}€ uhádol si správne číslo {b} počet ostávajúcih pokusov:{počet_kôl}")
       else:
            konto = konto - suma
            print(f"Prehral si tvoje konto je {konto}€ číslo bolo {b} skús ešte raz :) počet ostávajúcih pokusov:{počet_kôl}")
     print(f"Celkovo si vyhral {konto}€ gratulujem") 