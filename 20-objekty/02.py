class pes:
    def __init__(self,meno):
        self.meno = meno
    
    def stekaj(self):
        print(f"Haf! Moje meno je {self.meno}")

moj_pes = pes("Dunčo")
moj_pes.stekaj()

