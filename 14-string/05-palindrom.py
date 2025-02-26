# palindrom je reťazec ktorý je rovanaký prí čítani alebo od konca
ret = input("Zadaj reťazec: ")
obrateny = ret[::-1]
if ret == obrateny:
    print("reťazec",ret,"je palindrom")
else:
    print("reťazec", ret,"nie je palindrom")