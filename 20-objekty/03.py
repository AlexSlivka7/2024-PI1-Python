class pes:
    def __init__(self,meno,vek):
        self.meno = meno
        self.vek = vek
    
    def stekaj(self):
        print(f"{self.meno} šteká.")

    def narodeniny(self):
        print(f"{self.meno} má teraz {self.vek} roky.")

Pes = pes("Dunčo", 3)
Pes.stekaj()
Pes.narodeniny()