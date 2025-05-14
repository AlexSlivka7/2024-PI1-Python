class Bankovy_ucet:
    def __init__(self,meno,):
        self.meno = meno
        self.zostatok = 0

    def vloz(self,peniaze):
        self.zostatok += peniaze
        print(f"Na účet bolo vlozené {peniaze} €")

    def vyber(self,peniaze):
        if peniaze > self.zostatok:
            print("Nemaš peňoži!!!")

        elif peniaze <= 0:
            print("Nemôžeš vybrať zápornú alebo nulovú sumu!")
       
        else:
            self.zostatok -= peniaze
            print(f"Z účtu bolo vybraných {peniaze} €")

    def zobraz_stav(self):
        print(f"Majiteľ účtu: {self.meno}, Zostatok: {self.zostatok}")

    def zmena_mena(self,nove_meno):
        self.meno = nove_meno
        print(f"Meno majiteľa bolo zmenené na: {self.meno}")


bankovy_ucet = Bankovy_ucet("Samuel")
bankovy_ucet.vloz(100)
bankovy_ucet.vyber(30)
bankovy_ucet.zobraz_stav()
bankovy_ucet.zmena_mena("Martin")
bankovy_ucet.vloz(50)
bankovy_ucet.zobraz_stav()
        