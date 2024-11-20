import random #knižnica ktora sluzi na generovanie nahodnych hodnot

náhodné_cislo = random.randint(1,10) # vygeneruje nahodne cislo cele od 1 do 10
print(náhodné_cislo)

nahodna_farba = random.choice(["červená" , "čierna" , "zelená"]) # vygeneruje nahodnu hodnotu zo zoznamu hodnot zoznam ohranicime []
print(nahodna_farba)

nahodne_pismeno = random.choice("aeiouy") #vygeneruje náhodnu samohlasku
print(nahodne_pismeno)