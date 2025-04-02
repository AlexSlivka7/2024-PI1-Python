import random

teploty = []
pocet_dni = 30
#naplni list teploty náhodnými teplotami v rozsahu od 10 do 30
for i in range(pocet_dni):
    # teploty[i] = random.randint(10,30) # vrati chybu lebo prvky este neexistuju 
    teploty.append(random.randint(10,30))

for i in range(pocet_dni):
    print(f"{i+1}.deň - {teploty[i]} °C")

#vypočitá a vypíše priemernu teplotu
# priemerna_teploty = sum(teploty)/pocet_dni
# print(priemerna_teploty)
sucet = 0
for i in range(pocet_dni):
    sucet += teploty[i]

priemerna_teplota = sucet/pocet_dni
print(f"Priemerna teplota v mesiaci je {priemerna_teplota}°C")


for i in range(pocet_dni):
    if teploty[i] < priemerna_teplota:
        print(f"{i+1}.deň - {teploty[i]} °C")

