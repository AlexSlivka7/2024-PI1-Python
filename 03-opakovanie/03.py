r = float(input("zadaj polomer: "))
obvod = 2 * 3.14 * r
obsah = 3.14 * (r * r)
print("obvod je:" , obvod)
print("obsah je." , obsah)
a = float(input("zadaj veľkosť strany kocky: "))
S = ((a**2) + (a**2))
U = S **(1/2.0)
TU = U * a**2 
T = TU **(1/2.0)
print("Stenová uhlopriečka je:", round(U, 2))
print("Telesová uhlopriečka je:",round(T, 2))
