try:
    subor = open("subor.txt", "r") 


    while True:
        riadok = subor.readline()
        if riadok == "":
            break # break preruší cyklus a vyskočí z neho
        print(riadok.strip()) # strip odstráni všetky medzery


    subor.close() # zatvorí súbor
except:
    print("Súbor neexistuje")