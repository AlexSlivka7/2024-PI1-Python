n = int(input("Zadaj pocet: "))
pi = 0
citatel = 4
for menovatel in range(1 ,2 * n , 2):
    pi += citatel/menovatel
    citatel = -citatel
print ("pi =" , pi)
