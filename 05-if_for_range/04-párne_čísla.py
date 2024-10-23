cislo = int(input("Zadaj číslo:"))

# vypis párnych čísiel
print(f"Párne čísla do {cislo}:")
for i in range(2, cislo+1 , 2):
    print(i)

print(f"Nepárne čísla do {cislo}:")
# výpis nepárnych čísiel
for i in range(1 , cislo+1 , 2):
    print(i)

if cislo % 2 == 0:
    print(f"Číslo {cislo} je párne")
else:
    print(f"Číslo {cislo} je nepárne")