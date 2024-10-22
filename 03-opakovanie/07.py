n = int(input("Zadaj počet políčok:"))
if n < 2:
    print(f"Na {n}. políčku je {n} zrnko ryže")
else:
    a = 1
    for i in range(n - 1):
        a = a * 2
    print(f"Na {n}. políčku je {a} zrniek ryže")
