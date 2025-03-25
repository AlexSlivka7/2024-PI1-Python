retazec = input("Zadaj reťazec: ")
print(f"Dĺžka reťazca je {len(retazec)}")

for znak in retazec:
    print(znak)

print("\n")
for i in range(len(retazec)-1, -1, -1,):
    print(retazec[i])

print("\n")
for znak in retazec:
    print(znak*3)
    
    