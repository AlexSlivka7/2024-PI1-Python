class osoba:
    def __init__(self,meno,vek):
        self.meno = meno
        self.vek = vek
    def predstav_sa(self):
        print(f"Ahoj volám sa {self.meno} a mám {self.vek} rokov")

    def zostarni(self):
        self.vek += 1
        print(f"{self.meno} teraz má {self.vek}")

Samuel_Svoboda = osoba("Samuel Svoboda", 16)
Martin_Mitka = osoba("Martin Mitka", 16)

Samuel_Svoboda.predstav_sa()
Martin_Mitka.predstav_sa()
print(" ")
Samuel_Svoboda.zostarni()
Martin_Mitka.zostarni()