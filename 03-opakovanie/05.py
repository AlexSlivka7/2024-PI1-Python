R = int(input("Aký je rok:"))
M = int(input("Ktorý je mesiac:"))
D = int(input("ktorý deň v mesiaci je:"))
a = ((R * 365) + (M * 30) + D) - 2009 * 365 
b = a *24
c = b * 60 * 60
print(f"Od zavedenia eura uplynolo: {a} dní")
print(f"Od zavedenia eura uplynolo: {b} hodín")
print(f"Od zavedenia eura uplynolo: {c} sekúnd")