class Auto:
    def __init__(self, znacka, farba):
        self.znacka = znacka
        self.farba = farba

    def zapni_motor(self):
        print(f"{self.znacka} naštartovalo motor.")

# vytvorenie objektu
moje_auto = Auto("Škoda", "modrá")

print(moje_auto.znacka)       # → Škoda
moje_auto.zapni_motor()       # → Škoda naštartovalo motor.

class Kolac:
    def __init__(self, prichut):
        self.prichut = prichut

    def zjedz(self):
        print(f"Mňam! {self.prichut} koláč je zjedený.")

moj_kolac = Kolac("čokoládový")
moj_kolac.zjedz()
