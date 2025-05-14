class Ziak:
    def __init__(self,meno,vek,známka):
        self.meno = meno
        self.vek = int(vek)
        self.známka = float(známka)
    
    def predstav_sa(self):
        print(f"Volám sa {self.meno}, mám {self.vek} rokov a priemernú známku mám {self.známka}")

zoznam_ziakov = []

for i in range(3):
    print(f"\nZadávam žiaka č. {i+1}")
    meno = input("Zadaj meno žiaka: ")
    vek = input("Zadaj vek žiaka: ")
    znamka = input("Zadaj známku žiaka: ")
   
    ziak = Ziak(meno,vek,znamka)
    zoznam_ziakov.append(ziak)

print("\nZoznam všetkých žiakov: ")
for ziak in zoznam_ziakov:
    ziak.predstav_sa()
    
sucet_vek = sum(ziak.vek for ziak in zoznam_ziakov)
sucet_znamok = sum(ziak.známka for ziak in zoznam_ziakov)

priemerny_vek = sucet_vek / len(zoznam_ziakov)
priemerna_znamka = sucet_znamok / len(zoznam_ziakov)

print(f"\nPriemerný vek v triede: {priemerny_vek:.1f} rokov")
print(f"Priemerná známka v triede: {priemerna_znamka:.2f}")