import datetime

class Osoba:    # triedy vzdy píseme prvým veľkým písmenom
    def __init__(self, meno, priezvisko, rok):  #konstruktor zavola sa pri vzniku objektu 
        self.meno = meno    #atribút objektu (vlastnosť)
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):  # metóda (co vie objekt robit)
        print(f"Ahoj ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov.")

    def vypis_meno(self):
        print(self.meno,self.priezvisko)

    def vypis_vek(self):
        print(self.vek)

    def vypis_rok(self):
        print(self.rok)


class Student(Osoba):   #trieda Student zdedi atributy a metody od triedy Osoba
    def __init__(self, meno, priezvisko, rok,trieda):
        super().__init__(meno, priezvisko, rok) # super - znamena ze pouzije atributy z rodicovsekj triedy (Osoba)
        #Osoba.__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        super().pozdrav()
        print(f"Som študentom {self.trieda} triedy.")
        # polymorfizmus - meníme metódu pozdrav z rodičovskej triedy

# alex = Osoba("Alex", "Slivka", 2009) #vzikne objekt alex vytvoreny pomocou triedy Osoba
# alex.pozdrav() # voláme metódu objektu pozdrav
# fero = Osoba("František", "Mikloško", 1990)
# fero.pozdrav()

# alex.vypis_meno()
# alex.vypis_rok()
# alex.vypis_vek()

student = Student("Ján","Študent", 2008, "I.AT")
student.pozdrav()
student.vypis_meno()
student.vypis_rok()
student.vypis_vek()


clovek = Osoba("Jurko", "Mrkvička", 2000)
clovek.pozdrav()